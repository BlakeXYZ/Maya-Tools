# # This code sample uses the 'requests' library:
# # http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json
# from auth import auth_token


# url = "https://artificialblakek.atlassian.net/rest/api/2/search?jql=project=TP01&maxResults=1000"

# auth = HTTPBasicAuth("artificialblakek@gmail.com", auth_token)

# headers = {
#   "Accept": "application/json"
# }

# query = {
#   'query': '{query}'
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    params=query,
#    auth=auth
# )

# # Get all project issues,by using the 
# # json loads method. 
# json_dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))



####################
####################
####################
####################


import requests
from requests.auth import HTTPBasicAuth
import json
from auth import auth_token

url_projects = "https://artificialblakek.atlassian.net/rest/api/2/project"
url_search = "https://artificialblakek.atlassian.net/rest/api/2/search"

auth = HTTPBasicAuth("artificialblakek@gmail.com", auth_token)

headers = {
    "Accept": "application/json"
}

# Get all projects
response_projects = requests.get(url_projects, headers=headers, auth=auth)
projects_data = json.loads(response_projects.text)

# Extract and print project names and keys
for project in projects_data:
    print("Project Name:", project["name"])
    print("Project Key:", project["key"])
    print("Project ID:", project["id"])
    print("---")

# Now, you can switch between projects by using their keys in the search query
selected_project_key = "TP02"

# JQL query as a string
jql_query = f'project={selected_project_key}' # adding 'AND maxResults=1000' does not work

# Include the JQL query as a parameter
query = {'jql': jql_query}

# Make the request
response_search = requests.get(url_search, headers=headers, params=query, auth=auth)

# Get and print search results
search_results = json.loads(response_search.text)
print("Search Results:")



####################
####################
####################
####################


# The JSON response received, using 
# the requests object, is an intricate nested object. 
# Convert the output to a dictionary object. 
dict_of_dump = json.loads(json.dumps(search_results, sort_keys=True, indent=4, separators=(",", ": ")))

# Iterate through each issue in the response
for issue in dict_of_dump["issues"]:
    # Retrieve issue key
    issue_key = issue["key"]

    issue_type = issue["fields"]["issuetype"]["name"]

    issue_status = issue["fields"]["status"]["name"]

    # Retrieve issue summary
    issue_summary = issue["fields"]["summary"]

    # Retrieve assignee information (if assigned)
    assignee_info = issue["fields"]["assignee"]
    
    # Check if assignee exists
    if assignee_info:
        assignee_name = assignee_info["displayName"]
    else:
        assignee_name = "Unassigned"

    # Print or use the retrieved information
    print(f"Issue Key: {issue_key}")
    print(f"Summary: {issue_summary}")
    print(f'Issue Type: {issue_type}')
    print(f'Issue Status: {issue_status}')
    print(f"Assignee: {assignee_name}")
    print("-------------------------")