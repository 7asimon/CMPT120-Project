# GREYWALKER
# Author: Abel Simon
# Date : October 23, 2017

score = 0
userAction = None
moves = 0

def showIntro():
    print("GREYWALKER")
    print('')
    # store input name in a variable and return it to them
    playerName = input("Your name is...you cannot seem to recall it. Try to remember your name: ")
    print("Ah, yes, " + playerName + ", that was it. You are a sleepwalker"
          " and an insomniac who is attempting to master lucid dreaming."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input("You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          " You must collect all items and visit every location before the final encounter of the game."
          " Once the game begins, type help to view the list of usable commands.")
    print('')
    
# store all 10 locations in a list to be used later
locDescrips = ["You find yourself in a vaguely familiar meadow filled with wilted daisies."
          " Looking forward, you can see a village engulfed in flames."
          " There appears to be areas of interest to the east, west, and south as well.",
            "The village is completely vacant as the buildings crumble and burn around you."
            " However, in front of you lies one house that is completely unaffected by the fire,"
            " and a sign in front of it that reads: WHY HAVE YOU CAUSED US SUCH AGONY?",
            "You arrive in a grey room with random burned objects scattered about."
            " As you walk into the room, the color fades from your skin and you notice everything you see is in black and white." ,
             "You arrive at a dinner table with a mirror image of yourself. No matter what you do, he does not speak to you.",
             "You arrive at the edge of a cliff with a dark abyss below it. There is nothing of interest here.",
             "Inside the house, you find that the walls are covered with black and white pictures of your family"
                " that were taken before they died mysteriously years ago."
                " Eerily enough, you are missing from all the pictures as if you were cropped out of them.",
             "You come across a wall with seemingly meaningless inscribings on them."
               "You cannot make out what the strange drawings say. You hear people shuffling around on the other side",
             "Walking down the path, you witness many villagers screaming in agony and running down the street."
             " There appears to be an endless number of them",
             "At the end of the path of agony, people gather around a small shrine",
             "As you approach the wall, it crumbles, reavealing a balcony where a blank faced woman stands."
             " The woman is missing all facial features as if they have been erased from her face."]

hasBeenThere = [False, False, False, False, False, False, False, False, False, False]
hasBeenSearched = [False, False, False, False, False, False, False, False, False, False]
locationCheck = [False, False, False, False, False, False, False, False, False, False]
items = [None, None, "Map", None, None, "Necklace", None, None, "Strange Gem", None]
inventory = []

locNames = ["The Meadow", "Burning Village", "Grey Room",
           "Dinner Table", "Cliff", "House Interior", 
           "Strange Wall", "Path Of Agony", "Shrine" , "Balcony"]

 
def gameEnd():
    print("Suddenly, before you could discover all you needed to, you awaken from the dream."
          "You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the cryptic message on the sign"
" To Be Continued In Future Game Versions...")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)

meadow = 0
village = 1
greyRoom = 2
dinnerTable = 3
cliff = 4
houseInterior = 5
strangeWall = 6
pathOfAgony = 7
shrine = 8
balcony = 9
locInfo = 0
         # N     S     E      W
world = [[2,  None,     1,  None] # meadow
        ,[3,     1,     4,     2] # village
        ,[5,     0,     3,  None] # grey room
        ,[7,     1,     4,     2] # dinner table
        ,[6,  None,  None,     3] # cliff
        ,[None,  2,     6,  None] # house interior
        ,[9,     3,     7,     5] # strange wall
        ,[None,  4,     8,     6] # path of agony
        ,[None,  None,   None, 7] # shrine
        ,[None,  6,  None,  None] # balcony
        ]
def gameLoop():
    global locInfo
    global hasBeenSearched
    global world
    while True:
        showLocation(locInfo)
        userAction = input("Enter Command: ").lower()
        if userAction == "north" or userAction == "east" or userAction == "south" or userAction == "west":
            whereTo(locInfo, userAction)
        if userAction == "score":
            print(score)
        if userAction == "moves":
            print("You have", 16 - moves ,"moves left")
        if userAction == "look":
            print(locDescrips[locInfo])
        if userAction == "help":
            print("Use <north>, <south>, <east>, and <west> to navigate \n"
                  "Once you find the map, type <map> to view it \n"
                  "Type <score> to view your current score \n"
                  "Type <moves> to see how many moves you have left \n"
                  "Type <quit> to exit the game \n"
                  "Type <search> to look for an item in your location \n"
                  "Type <take> to take an item once you find it \n"
                  "Type <inv> to view your inventory \n"
                  "Type <stuck> to be given tips on how to win the game.")
        if userAction == "quit":
            quit()
        if userAction == "search":
            playerSearch(locInfo)
        if userAction == "take":
            retrieve(locInfo)
        if userAction[0:3] == "inv":
            print(inventory)
        if userAction == "stuck":
            print("There are 10 locations. Each one must be visited in order to win. \n"
                  "Type <search> at every location and then <take> if something is found. \n"
                  "You must find all items, except the map, to pass the final stage of the game. \n"
                  "Do not try to interact with the blank-faced woman without having all the necessary items. "
                  "You can tell if you have all the items needed based on how she responds to your presence. \n")
        if userAction == "map":
            if "Map" in inventory:
                print("                              Balcony                                 \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "House Interior ========= Strange Wall ========== Path of Agony ===== Shrine \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       " Grey Room ============== Dinner Table ============= Cliff     \n"
                       "     ||                         ||                                   \n"                  
                       "     ||                         ||                                   \n"
                       "     ||                         ||                                   \n"
                       "     ||                         ||                                   \n"
                       "   Meadow =================== Village                                 \n"
                      )
            else:
                print("You have not yet found the map")
                
            

def goTo(x):
    global score
    global hasBeenThere
    global countHasBeen
    global locNames
    global moves
    global locInfo
    global locationCheck
    moves = moves + 1
    curLocation = locNames[x]
    if hasBeenThere[x] == False:
        score = score + 5
        hasBeenThere[x] = True
    if curLocation == locNames[9]:
        finalEncounter(locInfo)
        

def finalEncounter(location):
    global score
    global hasBeenThere
    global countHasBeen
    global locNames
    global moves
    global locInfo
    global locationCheck
    if locationCheck[location] == False:
        print(locDescrips[locInfo])
        print('')
        locationCheck[location] = True
    else:
        print(locNames[locInfo])
        print('')
    if "Necklace" not in inventory and "Strange Gem" not in inventory:
        print("The blank faced woman on the balcony grabs a dagger, clearly intending to attack you if you approach. Do you proceed?") 
    else:
        print("A woman stretches her arms out towards you, beckoning you to come forward. Do you comply?")
    finalDecision = input()
    if finalDecision == "yes":
        if "Necklace" in inventory and "Strange Gem" in inventory and score == 45 or score == 50:
            gameEnd()
        elif "Necklace" in inventory and "Strange Gem" in inventory and score != 45 or score != 50:
            print("Once you get close to her, the woman takes a closer look at you and then pushes you away")
        else:
            input("The woman slaughters you for the sins of your past. You die within the dream and never wake up from it.")
            quit()
    else:
        return
                    
def whereTo(location,userAction):
    global world
    global locInfo
    direction = None
    if userAction == "north":
        direction = 0
    elif userAction == "south":
        direction = 1
    elif userAction  == "east":
        direction = 2
    elif userAction == "west":
        direction = 3
    nextLocation = world[location][direction]
    if nextLocation is None:
        print("There is nothing in that direction.")
    else:
        locInfo = nextLocation
        goTo(nextLocation)

def showLocation(location):
    global locInfo
    global hasBeenThere
    global locationCheck
    global moves
    if moves == 16:
        print("You run out of time and the dream has ended")
        input()
        quit()
    if locationCheck[location] == False:
        print(locDescrips[locInfo])
        locationCheck[location] = True
    else:
        print(locNames[locInfo])

def playerSearch(s):
    global locInfo
    global hasBeenSearched
    global items
    global world
    if hasBeenSearched[s] == False and items[locInfo] != None:
        print("While searching the area, you find a", items[locInfo], "for the taking.")
        hasBeenSearched[s] = True
    else:
        print("You find nothing worth taking in this area.")

def retrieve(locInfo):
    if hasBeenSearched[locInfo] is True:
        inventory.append(items[locInfo])
        print("You have picked up a", items[locInfo]+".")
    else:
        print("You find nothing worth taking in this area. Try <search> if you have not already")

def gameEnd():
    print("The woman takes the necklace and the gem from you and then promptly disappears, leaving you without any answers." 
" To Be Continued In Future Game Versions...")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)
    
def main():
    showIntro()
    gameLoop()

main()
