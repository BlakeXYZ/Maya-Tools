import random
import datetime 
import json
from pathlib import Path
import sys, os
import inspect

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 181)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 55))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(466, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.btn_closeWindow = QPushButton(self.centralwidget)
        self.btn_closeWindow.setObjectName(u"btn_closeWindow")
        self.btn_closeWindow.setMinimumSize(QSize(0, 32))
        font1 = QFont()
        font1.setPointSize(8)
        self.btn_closeWindow.setFont(font1)

        self.gridLayout.addWidget(self.btn_closeWindow, 6, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_fun_fact = QLabel(self.centralwidget)
        self.label_fun_fact.setObjectName(u"label_fun_fact")
        sizePolicy.setHeightForWidth(self.label_fun_fact.sizePolicy().hasHeightForWidth())
        self.label_fun_fact.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        self.label_fun_fact.setFont(font2)
        self.label_fun_fact.setAlignment(Qt.AlignCenter)
        self.label_fun_fact.setWordWrap(True)
        self.label_fun_fact.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.label_fun_fact)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Here's your daily fun fact!", None))
        self.btn_closeWindow.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_fun_fact.setText(QCoreApplication.translate("MainWindow", u"Fun Fact Goes Here", None))
    # retranslateUi

snippet = """A crocodile cannot stick its tongue out.
A shrimp's heart is in its head.
The "sixth sick sheik's sixth sheep's sick" is believed to be the toughest tongue twister in the English language.
Wearing headphones for just an hour could increase the bacteria in your ear by 700 times.
Some lipsticks contain fish scales.
Cat urine glows under a black-light.
Rubber bands last longer when refrigerated.
There are 293 ways to make change for a dollar.
A shark is the only known fish that can blink with both eyes.
"Dreamt" is the only English word that ends in the letters "mt".
Almonds are a member of the peach family.
Maine is the only state that has a one-syllable name.
There are only four words in the English language which end in "dous": tremendous, horrendous, stupendous, and hazardous.
A cat has 32 muscles in each ear.
An ostrich's eye is bigger than its brain.
Tigers have striped skin, not just striped fur.
In many advertisements, the time displayed on a watch is 10:10.
A dime has 118 ridges around the edge.
The giant squid has the largest eyes in the world.
"Stewardesses" is the longest word that is typed with only the left hand.
A blue whale's tongue is heavier than an elephant.
A crab's taste buds are on their feet.
Octopi have three hearts.
The American lobster can live to be 20 years old.
No two spot patterns on a whale shark are the same — they are as unique as fingerprints.
The United States has the fourth-longest water system in the world.
Alaska is the state with the longest coastline.
The tallest monument in the United States is the Gateway Arch in St. Louis.
Kansas City, Missouri, has more fountains than any other city in the world besides Rome.
Tennessee and Missouri each share borders with eight states.
AB negative is the rarest blood type.
On average, the human heart beats 100,000 times a day.
The strongest muscle in the body is the jaw.
Fingernails grow faster than toenails.
The average tongue is about three inches long.
Strawberries and raspberries wear their seeds on the outside. 
Potatoes were the first vegetable to be grown in space. 
Bananas are technically herbs. 
Tomatoes are the most eaten fruit in the world. 
Apples are in the rose family.
Dinosaur fossils have been found on all seven continents. 
The dinosaur with the longest name is Micropachycephalosaurus.
A Nigersaurus has an unusual skull containing as many as 500 slender teeth.
Snakes, crocodiles and bees were just a few of the animals who lived alongside dinosaurs.
Both the width and the height of the Gateway Arch in St. Louis are 630 feet.
The Washington Monument is the tallest unreinforced stone masonry structure in the world.
President Theodore Roosevelt is responsible for giving The White House its name.
Elvis Presley was one of the largest private donors to the Pearl Harbor memorial.
The longest tennis match lasted 11 hours and five minutes at Wimbledon in 2010.
Women first competed in the Olympic Games in 1900 in Paris.
Wrestling was the world's first sport.
Golf is the only sport to be played on the moon.
The FIFA World Cup (soccer) is one of the most viewed sporting events on television.
The Empire State Building gets struck by lightning an average of 25 times a year.
In 1899, it was so cold that the Mississippi River froze.
Clouds can travel at more than 100 mph with the jet stream.
Hurricanes north of the Earth's equator spin counterclockwise.
Hurricanes south of the Earth's equator spin clockwise.
Abraham Lincoln stood at 6 feet 4 inches making him one of the tallest U.S. presidents.
Bill Clinton has two Grammy Awards.
Three of the nation's five founding fathers — John Adams, Thomas Jefferson and James Monroe — died on July 4th (Adams and Jefferson in 1826 and Monroe in 1831).
The shortest-serving president was William Henry Harrison, who was the ninth president of the United States for 31 days in 1841.
Franklin D. Roosevelt is the only American president to have served more than two terms.
Tiger roars were used for The Lion King as lions weren't loud enough.
Walt Disney World resort is about the same size as San Francisco.
Mickey Mouse was the first animated character to receive a star on the Hollywood Walk of Fame.
Pocahontas is the only Disney princess with a tattoo.
Disney's Beauty and the Beast was the first animated film in history to be nominated for Best Picture at the Academy Awards.
Ears of corn generally have an even number of rows.
Although Froot Loops cereal signature "O's" come in many colors, they're all the same flavor.
Applesauce was the first food eaten in space.
The Caesar salad was born in Tijuana, Mexico.
One out of every four hazelnuts on the planet makes its way into a jar of Nutella.
The "Guinness Book of World Records" was first published in 1955.
The Simpsons is the longest-running animated television show (based on episodes).
The world's largest wedding cake weighed 15,032 pounds.
Ashrita Furman is the person with the most Guinness World Records titles.
The largest gathering of people dressed as Superman was 867, achieved by a group in the U.K.
Wombat Poop is Cubic.
A Group of Flamingos is a Flamboyance.
The moon is moving away from the Earth at a tiny, although measurable, rate every year. 85 million years ago, it was orbiting the Earth about 35 feet from the planet's surface.
The star Antares is 60,000 times larger than our sun. If our sun were the size of a softball, the star Antares would be as large as a house.
In Calama, a town in the Atacama Desert of Chile, it has never rained.
At any given time, there are 1,800 thunderstorms in progress over the earth's atmosphere.
Erosion at the base of Niagara Falls has caused the falls to recede approximately seven miles over the past 10,000 years.
A ten-year-old mattress weighs double what it did when it was new due to debris that it absorbs over time. That debris includes dust mites (their droppings and decaying bodies), mold, millions of dead skin cells, dandruff, animal and human hair, secretions, excretions, lint, pollen, dust, soil, sand, and a lot of perspiration, which the average person loses at a rate of a quart a day. Good night!
Every year, 16 million gallons of oil run off pavement into streams, rivers, and, eventually, oceans in the United States. This is more oil than was spilled by the Exxon Valdez.
In space, astronauts cannot cry because there is no gravity, and tears can't flow.
Most lipstick contains fish scales.
A "jiffy" is an actual unit of time: 1/100th of a second.
If you have three quarters, four dimes, and four pennies, you have $1.19. You also have the largest possible amount of money in coins without being able to make change for a dollar.
Leonardo Da Vinci invented scissors.
Recycling one glass jar saves enough energy to operate a television for three hours.
The cigarette lighter was invented before the match.
The main library at Indiana University sinks over an inch a year. When it was designed, engineers failed to take into account the weight of all the books that would occupy the building.
A category three hurricane releases more energy in ten minutes than all the world's nuclear weapons combined.
There is enough fuel in a full jumbo jet tank to drive an average car four times around the world.
An average of 100 people choke to death on ballpoint pens every year.
Antarctica is the only continent without reptiles or snakes.
The cruise liner Queen Elizabeth 2 moves only six inches for each gallon of fuel it burns.
San Francisco cable cars are the only National Monuments that can move.
February 1865 is the only month in recorded history not to have a full moon.
Nutmeg is extremely poisonous if injected intravenously.
A rainbow can be seen only in the morning or late afternoon. It can occur only when the sun is 40 degrees or less above the horizon.
Lightning strikes the Earth 100 times every second.
La Paz, Bolivia, has an average annual temperature below 50 degrees Fahrenheit. However, it has never recorded a zero-degree temperature. Same for Stanley, the Falkland Islands, and Punta Arenas, Chile.
There are over 87,000 Americans on waiting lists for organ transplants.
Catsup leaves the bottle at a rate of 25 miles per year.
Toxic house plants poison more children than household chemicals do.
You are more likely to be infected by flesh-eating bacteria than you are to be struck by lightning.
According to Genesis 1:20-22, the chicken came before the egg.
When opossums are "playing 'possum,'" they are not playing. They actually pass out from sheer terror.
The two-foot-long bird called a Kea that lives in New Zealand likes to eat the strips of rubber around car windows.
Snakes are true carnivores as they eat nothing but other animals. They do not eat any type of plant material.
The Weddell seal can travel underwater for seven miles without surfacing for air.
An iguana can stay underwater for 28 minutes.
Horses can't vomit.
A crocodile cannot stick its tongue out.
Butterflies taste with their feet.
Penguins can jump as high as six feet in the air.
All polar bears are left-handed.
An eagle can kill a young deer and fly carrying it.
The leg bones of a bat are so thin that no bat can walk.
The katydid bug hears through holes in its hind legs.
Slugs have four noses.
Ostriches stick their heads in the sand to look for water.
In a study of 200,000 ostriches over a period of 80 years, there were no reported cases of an ostrich burying its head in the sand.
It's possible to lead a cow upstairs but not downstairs.
A shrimp's heart is in its head.
A snail can sleep for three years.
The chicken is one of the few things that man eats before it's born and after it's dead.
A pregnant goldfish is called a twit.
Rats multiply so quickly that in 18 months, two rats could have over a million descendants.
There are only three types of snakes on the island of Tasmania and all three are deadly poisonous.
It is physically impossible for pigs to look up into the sky.
Dolphins sleep with one eye open.
A goldfish has a memory span of three seconds.
A shark is the only fish that can blink with both eyes.
Emus and kangaroos cannot walk backwards and are on the Australian coat of arms for that reason.
The jellyfish is 95% water.
A hippo can open its mouth wide enough to fit a 4-foot-tall child inside.
Only female mosquitoes bite.
Most elephants weigh less than the tongue of the blue whale.
The microwave was invented after a researcher walked by a radar tube and the chocolate bar in his pocket melted.
23% of all photocopier faults worldwide are caused by people sitting on them and photocopying their butts.
"Stewardesses" is the longest word that is typed using only the left hand.
71% of office workers stopped on the street for a survey agreed to give up their computer passwords in exchange for a chocolate bar.
The electric chair was invented by a dentist.
A Boeing 767 airliner is made of 3,100,000 separate parts.
The first FAX machine was patented in 1843, 33 years before Alexander Graham Bell demonstrated the telephone.
Hershey's Kisses are called that because the machine that makes them looks like it's kissing the conveyor belt.
"Typewriter" is the longest word that can be made using the keys on only one row of the keyboard.
In 1980, there was only one country in the world with no telephones: Bhutan.
More than 50% of the people in the world have never made or received a telephone call.
Montpelier, Vermont, is the only U.S. state capital without a McDonalds.
There is a bar in London that sells vaporized vodka, which is inhaled instead of sipped.
In the White House, there are 13,092 knives, forks, and spoons.
Americans, on average, eat 18 acres of pizza every day.
Coca-Cola was originally green.
The only food that does not spoil: honey.
The Pilgrims ate popcorn at the first Thanksgiving dinner.
Iceland consumes more Coca-Cola per capita than any other nation.
Almonds are members of the peach family.
Cranberry is the only Jell-O flavor that contains real fruit flavoring.
The drive-through line on opening day at the McDonald's restaurant in Kuwait City, Kuwait, was seven miles long at its peak.
American Airlines saved $40,000 in 1987 by eliminating one olive from each salad served first class.
Celery has negative calories! It takes more calories to eat a piece of celery than the celery has in it to begin with.
The average American drinks about 600 sodas per year.
Mailmen in Russia now carry revolvers after a recent decision by the government.
One out of five people in the world (1.1 billion people) live on less than $1 per day.
Quebec City, Canada, has about as much street crime as Disney World.
The largest ocean liners pay a $250,000 toll for each trip through the Panama Canal. The canal generates fully one-third of Panama's entire economy.
In every episode of Seinfeld, there is a Superman somewhere.
The Spanish word esposa means "wife." The plural, esposas, means "wives," but also "handcuffs."
City with the most Rolls Royces per capita: Hong Kong.
Of the six men who made up the Three Stooges, three of them were real brothers (Moe, Curly and Shemp).
If Barbie were life-size, her measurements would be 39-23-33. She would stand 7 feet, 2 inches tall.
On average, people fear spiders more than they do death.
Thirty-five percent of the people who use personal ads for dating are already married.
In Tokyo, you can buy a toupee for your dog.
A dime has 118 ridges around the edge."""

class ValidationError(Exception):
    pass

def last_launched_threshold() -> bool:

    # Get Current Working Directory
    # script_directory passed from userSetup!

    # Set Absolute path to the JSON file using forward slashes
    datetime_json_path = os.path.join(script_directory, 'yourDailyFunFact_DB.json')
    print(f'datetime_json_path {datetime_json_path}')

    # SET hour_time_threshold for launching fun fact tool 
    hour_time_threshold = 12

    # retrieve stored time in json
    try:
        with open(datetime_json_path, "r") as json_file:
            data = json.load(json_file)
        stored_time = data["stored_time"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        raise ValidationError(f'Unable to load the JSON file.')
    # get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current Time: {current_time} --- Stored Time: {stored_time}')

    # compare current against stored time
    current_time_int = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    stored_time_int = datetime.datetime.strptime(stored_time, "%Y-%m-%d %H:%M:%S")
    time_difference = current_time_int - stored_time_int
    # set time difference threshold 
    time_threshold = datetime.timedelta(hours=hour_time_threshold)

    # if less than time_threshold, do not launch
    if time_difference < time_threshold:
        print(f'Time difference is LESS than {time_threshold}')
        return False
    else:
    # if greater than 4 hour difference, launch and rewrite
        print(f'Time difference is GREATER than {time_threshold}')

    # Update stored_time in the JSON file
        with open(datetime_json_path, "w") as json_file:
            json.dump({"stored_time": current_time}, json_file)
        # print("Updated stored_time in path: ", datetime_json_path)
        return True

def get_random_fact(snippet: str) -> str:

    lines = snippet.splitlines()
    list_of_facts = []

    for line in lines:
        list_of_facts.append(line)

    random_fact = random.choice(list_of_facts)

    return random_fact

class yourDailyFunFact(QtWidgets.QMainWindow):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, my_random_fact, parent = None):
        """
        Initialize class.
        """
        super(yourDailyFunFact, self).__init__(parent = parent)

        # Set window flags to create a standalone window
        self.setWindowFlags(QtCore.Qt.Window)

        # Set up the UI within this widget
        self.mainWidget = Ui_MainWindow()
        self.mainWidget.setupUi(self)  

        # Set initial Window Size
        self.resize(577, 210)

        ###
        ###
        # find interactive elements of UI

        self.label_fun_fact = self.findChild(QtWidgets.QLabel, 'label_fun_fact')
        self.btn_closeWindow = self.findChild(QtWidgets.QPushButton, 'btn_closeWindow')

        ###
        ###
        # assign clicked handler to buttons
        self.btn_closeWindow.clicked.connect(self.closeWindow)

        # Set label_fun_fact Text 
        self.label_fun_fact.setText(my_random_fact)

        # Resize mainWidget Window to fit dynamic text 
        content_size = self.sizeHint()
        self.resize(content_size.width(), content_size.height() + 100)

        
    def closeWindow(self):
        """
        Close window.
        """
        print ('closing window')
        self.destroy()
    
def openWindow(my_random_fact):
    """
    ID Maya and attach tool window.
    """
    # Maya uses this so it should always return True
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'Your Daily Fun Fact' in win.objectName(): # update this name to match name below
                win.destroy()

    #QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    yourDailyFunFact.window = yourDailyFunFact(my_random_fact, parent = mayaMainWindow)
    yourDailyFunFact.window.setObjectName('Your Daily Fun Fact') # code above uses this to ID any existing windows
    yourDailyFunFact.window.setWindowTitle('Your Daily Fun Fact')
    yourDailyFunFact.window.show()
    
def run():

    if last_launched_threshold():
        my_random_fact = get_random_fact(snippet)
        openWindow(my_random_fact)

if __name__ == "__main__":
    run()



