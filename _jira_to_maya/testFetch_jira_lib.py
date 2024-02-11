from jira import JIRA 
import json
from auth import auth_token

from pprint import pprint

# Specify a server key. It should be your 
# domain name link. yourdomainname.atlassian.net 

jiraOptions = {'server': "https://artificialblakek.atlassian.net"} 

# Some Authentication Methods
jira = JIRA(
    options=jiraOptions,
    basic_auth=("artificialblakek@gmail.com", auth_token),  # Jira Cloud: a username/token tuple
)


# # Search all issues mentioned against a project name. 

# for singleIssue in jira.search_issues(jql_str='project = TP01'): 

#     print(f'''key: {singleIssue.key}
#         summary:    {singleIssue.fields.summary}
#         issuetype:  {singleIssue.fields.issuetype.name}
#         status:     {singleIssue.fields.status.name}
#         assignee:   {singleIssue.fields.assignee}
#         label:      {singleIssue.fields.labels}
#         ''')


issue_key = 'TP01-4'

# Replace 'your_issue_key' with the actual issue key you want to update
issue = jira.issue(issue_key)

####
#### PRINT INFO ABOUT CURRENT Issue

DICT_issue_fields_info = {
    'key': issue.key,
    'summary': issue.fields.summary,
    'issuetype': issue.fields.issuetype.name,
    'status': issue.fields.status.name,
    'assignee': issue.fields.assignee,
    'label': issue.fields.labels
}


#### 
####   GET + ADD COMMENTS

# comments = issue.fields.comment.comments

# print(comments)


# # Print each comment
# for comment in comments:
#     print("---")
#     print(f"Author: {comment.author.displayName}")
#     print(f"Created: {comment.created}")
#     print(f"Comment: {comment.body}")
#     print("---")


# # Add a comment using add_comment base method
# jira.add_comment(issue, 'hello there, this is a comment added from python!')
    

#### 
####   SET TRANSITIONS (Sprint Board Column)

# # Find the transition ID for the specified status
transitions = jira.transitions(issue)

# # Format available transitions for clean printing
# formatted_transitions = json.dumps(transitions, indent=4)
# print(f"Available Transitions for {issue_key}: {formatted_transitions}")

DICT_issue_transitions_info = {}

for transition in transitions:

    # Store Currently Set Transition
    if transition['name'] == issue.fields.status.name:
        set_transition = True
    else:
        set_transition = False
    
    transition_info = {
        'name' : transition['name'],
        'set_transition' : set_transition
    }

    DICT_issue_transitions_info[transition['id']] = transition_info

# Now DICT_transitions contains the transitions information
pprint(DICT_issue_transitions_info)
    



def push_transition_to_jira(selected_transition_id):

    # Perform the transition
    jira.transition_issue(issue, selected_transition_id)


# # Find the next status transition
# next_status_transition = next((transition for transition in transitions if transition['to']['name'] != issue.fields.status.name), None)

# print(issue.fields.status.name)
# print(next_status_transition['name'])

# if next_status_transition:
#     next_status_name = next_status_transition['to']['name']
#     print(f"Transitioning {issue_key} to {next_status_name} (ID: {next_status_transition['id']})")
#     # Perform the transition
#     jira.transition_issue(issue, next_status_transition['id'])
#     print(f"Transition successful!")
# else:
    # print(f"No next status found for {issue_key}")


# jira.transition_issue(issue, 'To Do')



