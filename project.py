# GREYWALKER
# Author: Abel Simon
# Date : November 28, 2017

score = 0
moves = 0
userAction = None
questionThreeAsked = False
morality = 0
guardianRequest = 0
necklace = 0
garments = 0
coldManState = 0
guardianState = 0
shrineState = 0
shrineOpen = True

#player name is retrieved outside of functions first, otherwise it is difficult to use it in location descriptions
print("FIVE YEARS OF AGONY")
print('')
playerName = input("Your name is...you cannot seem to recall it. \nTry to remember your name: ")
print("Ah, yes, " + playerName + ", that was it.")
print('')
        
#classes

class Player:
    def __init__(self, name, score, curLocation, moveCount, inventory):
        self.name = name
        self.score = score
        self.curLocation = curLocation
        self.moveCount = moveCount
        self.inventory = inventory
    def changeScore(self):
        score = score + 5

class Locale:
    def __init__(self, name, locDescrip, locName, hasBeenThere, hasBeenSearched, items):
        self.name = name
        self.locDescrip = locDescrip
        self.locName = locName
        self.hasBeenThere = hasBeenThere
        self.items = items

#initiate classes
        
player = Player('', 0, "Meadow", 20, [])
Locales = [
    Locale("meadow", "You find yourself in a vaguely familiar meadow filled with wilted daisies."
               " Looking forward, you can see a village engulfed in flames."
               " There appears to be areas of interest to the east, west, and south as well.", "The Meadow",
           False, False, None),
    Locale("burning village", "The village is completely vacant as the buildings crumble and burn around you."
               " However, in front of you lies one house that is completely unaffected by the fire,"
               " and a sign in front of it that reads: WHY HAVE YOU CAUSED US SUCH AGONY?", "The Burning Village",
           False, False, None),
    Locale("grey room", "You arrive in a grey room with random burned objects scattered about."
               " As you walk into the room, the color fades from your skin and you notice everything you see is in black and white.",
           "Grey Room", False, False, "Map"),
    Locale("dinner table", "You arrive at a dinner table with a mirror image of yourself. No matter what you do, he does not speak to you.",
           "Dinner Table", False, False, "Exotic Garments"),
    Locale("cliff", "You arrive at the edge of a cliff with a dark abyss below it. There is nothing of interest here.", "Cliff",
           False, False, "Ornament"),
    Locale("house interior", "Inside the house, you find that the walls are covered with black and white pictures of your family"
               " that were taken before they died mysteriously years ago."
               " Eerily enough, you are missing from all the pictures as if you were cropped out of them.", "House Interior",
           False, False, "Family Photo"),
    Locale("guardian's lair", "You come across a wall with seemingly meaningless inscribings on them."
               " You cannot make out what the strange drawings say. You hear people shuffling around on the other side.", "Guardian's Lair",
           False, False, None),
    Locale("path of agony", "Walking down the path, you witness many villagers screaming in agony and running down the street."
               " There appears to be an endless number of them", "Path of Agony", False, False, None),
    Locale("shrine", "At the end of the path of agony, people gather around a small shrine", "Shrine", False, False, "Strange Gem"),
    Locale("balcony", "As you approach the wall, it crumbles, reavealing a balcony", "Balcony", False, False, "Dream Shard"),
    Locale("water", "Using a ladder, you climb down from the balcony into the black water. Proceeding without visiting every location and without the dream shard is ill advised", "Water", False, False, None),
    Locale("land", "As you wade out of the water onto the land, you realize that the water surrounds you."
               " You must find a way out of this dream.", "Land", False, False, None)]
    

    

def showIntro():
    global playerName
    global score
    print("STORY:\n \n"
          "You are a sleepwalker and an insomniac with the uncanny ability to bring items you find in your dreams into the real world. "
          "5 years ago, you woke up lying down on the front lawn of your home feeling almost paralyzed. "
          "Your entire house was engulfed in flames and your wife, son, and daughter all perished in the fire. "
          "You immediately went into hiding and eventually fled the country out of fear that you would be blamed. "
          "To this day, you still do not have a clue why it occurred or why whoever did it left you alive. "
          "Perhaps someone planned to ruin your life by killing everyone you loved and framing you just by striking a match. \n \n"
          "Recently, you have been having very detailed dreams containing strange details about your past and the day of the fire. "
          "You continue on in hopes that you will find something that gives a clue as to who is responsible for the massacre of your family.")
    print('')
    print("This game is unique in that the decisions you make throughout the course of it "
          "affect the events that occur within the game and the ending of its story. \n"
          "Choose wisely...")
    print('')
    while True:
        startOrHelp = input("Either type <help> for a tutorial (highly recommended if you have not played before), "
                            "or type <start> if you have played before and wish to begin immediately: ")
        if startOrHelp == "start":
            print('')
            break
        elif startOrHelp == "help":
            print('')
            print("Type <north>, <south>, <east>, and <west> to navigate. \n"
                  "Type <awaken> when in a dream state to wake up and move around in your home. \n"
                  "Type <sleep> when in the real world to return to your dream. \n"
                  "Type <score> to view your current score. \n"
                  "Type <moves> to see how many moves you have left. \n"
                  "Type <quit> to exit the game. \n"
                  "Type <look> to view information about your location. "
                  "If any special commands are possible at your location, (such as <speak>), "
                  "typing <look> will also inform you of this. \n"
                  "Type <search> to look for an item in your location. \n"
                  "Type <take [item name]> to take an item once you find it. \n"
                  "For example, once you find the map, type <take map> to pick it up (it is near the start). \n"
                  "Once the map is found typing <map> will view it. "
                  "Similarly to the map, every item serves a purpose, even if it cannot be used directly. \n"
                  "Some items can be used by typing <use [item name]>, but for others, you will be prompted to use it when the time is right. \n"
                  "Type <inv> to view your inventory. \n"
                  "Type <speak> to talk to any people present at your current location when prompted. \n"
                  "Type <help> at any point to view these commands again. \n"
                  "All commands should be typed in lower case and without the <>. \n")
            print("Simply interacting with the world adds to your score, regardless of whether your choice is good or evil.")
            input("Press Enter to Continue: ")
            print('')
            break
        else:
            print("You entered an invalid command.")
            
    
    
# store all 12 locations in a list to be used later
locDescrips = ["You find yourself in a vaguely familiar meadow filled with wilted daisies. "
               "Looking forward, you can see a village. In the center lies your home, which is engulfed in flames. ",
               "You arrive in a grey room with random burned objects scattered about."
               " As you walk into the room, the color fades from your skin and you notice everything you see is in black and white.",
               "In front of your home, a message, painted across the sidewalk in blood red reads: \n\"WHY?\"",
               "You arrive at a dinner table with a mirror image of yourself. He smiles at you provokingly. "
               "Perhaps you should try to <speak> to him.",
               "You arrive at the edge of a cliff, beyond which a dark abyss lies.",
               "Inside the house, you find that the walls are covered with black and white pictures of your family"
               " that were taken before they died mysteriously years ago."
               " Eerily enough, you are missing from all the pictures as if you were cropped out of them.",
               "You come across a wall with seemingly meaningless inscribings on them."
               " You cannot make out what the strange drawings say. You hear people shuffling around on the other side.",
               "Walking down the path, you witness many villagers screaming in agony and running down the street."
               " There appears to be an endless number of them",
               "At the end of the path of agony, a family of three sits around a small shrine. "
               "On the shrine lies a glowing dagger that seems to be the subject of their worship. It radiates with evil energy. "
               "The mother of the family sits alone in a corner looking very distraught. Perhaps you should try to <speak> to her?",
               "As you approach the wall, it crumbles, reavealing a balcony",
               "Using a ladder, you climb down from the balcony into the black water."
               " Proceeding without visiting every location and without the dream shard is ill-advised",
               "As you wade out of the water onto the land, you realize that the water surrounds you."
               " You must find a way out of this dream.",
               "You just woke up in your room. Testing.",
               "You are in the hallway. Testing.",
               "You are in the kitchen. Testing.",
               "You are in the living room. Testing."]

# all these lists of booleans are used in vital functions
hasBeenThere = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
hasBeenSearched = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
locationCheck = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
items = [None, "Ornament", "Map", "Exotic Garments", None, "Family Photo", None, "Strange Gem", "Shrine Key", "Dream Shard", None, None, "Blanket", None, "Food", "Expensive Necklace"]
inventory = []

# short name for each location, later displayed if player has already been to that location
locNames = ["The Meadow", "Grey Room", "Home Town",
           "Dinner Table", "Cliff", "House Interior", 
           "Guardian's Lair", "Path Of Agony", "Shrine" , "Balcony",
            "Water", "Land", "Your Room", "The Hallway", "Your Son's Room", "Your Daughter's Room"]

# matrix key
meadow = 0
greyRoom = 1
village = 2
dinnerTable = 3
cliff = 4
houseInterior = 5
strangeWall = 6
pathOfAgony = 7
shrine = 8
balcony = 9
water = 10
land = 11
room1 = 12
room2 = 13
room3 = 14
room4 = 15
# locInfo stores the number of the location you're in, making creating additional functions far easier.
# locInfo is repeatedly updated throughout the functions in this program
locInfo = 0
# matrix for the game world
         # N     S     E      W
world = [[2,  None,     1,  None] # meadow
        ,[3,  None,  None,     2] # grey room
        ,[5,     0,     3,  None] # home town
        ,[6,     1,     4,     2] # dinner table
        ,[7,  None,  None,     3] # cliff
        ,[None,  2,     6,  None] # house interior
        ,[9,     3,     7,     5] # guardian's lair
        ,[None,  4,     8,     6] # path of agony
        ,[None,  None,   None, 7] # shrine
        ,[None,  6,  10,  None] # balcony
        ,[11,  None,  None,  9] # water
        ,[None,10, None,  None] # land
        ,[13, None, None, None]
        ,[None,   12,   14, 15]
        ,[None, None, None, 13]
        ,[None, None, 13, None]
         ]
# main game loop
def gameLoop():
    global locInfo
    global hasBeenSearched
    global world
    global necklace
    global garments
    global coldManState
    global guardianState
    global shrineState
    global shrineOpen
    while True:
        showLocation(locInfo)
        userAction = input("Enter Command: ").lower()
        # only address the whereTo function if the user decides to move somewhere
        if userAction == "north" and locInfo == 6 and guardianState == 0:
            guardianEncounter()
        if userAction == "north" and shrineState == 3 and "Shrine Key" not in inventory:
            print("The shrine is locked and you cannot enter")
        elif userAction == "north" or userAction == "east" or userAction == "south" or userAction == "west":
            whereTo(locInfo, userAction)
        if userAction == "speak":
            if locInfo == 3:
                speechCheckOne()
            elif locInfo == 4:
                cliffEncounter()
            elif locInfo == 8 and shrineState != 1:
                shrineEncounter()
            elif locInfo == 8 and shrineState == 1:
                shrineQuestTwo()
            elif locInfo == 8 and shrineState == 9:
                shrineQuestTwo()
            elif locInfo == 8 and shrineState == 10:
                shrineQuestTwo()
        if userAction == "awaken":
            if locInfo <= 11:
                print('')
                print("You awaken from your slumber.")
                locInfo = 12
            elif locInfo >= 12:
                print("You are already awake.")
        if userAction == "sleep":
            if locInfo >= 12:
                print('')
                print("You go back to your bed and return to the dream world.")
                locInfo = 0
            elif locInfo <= 11:
                print("You are already dreaming.")
        if userAction == "score":
            print(score)
        if userAction == "moves":
            print("You have made", moves, "moves")
        if userAction == "look":
            print(locDescrips[locInfo])
        if userAction == "take":
            print("You must type take followed by the item name to take an item")
        if userAction == "help":
            print("Type <north>, <south>, <east>, and <west> to navigate. \n"
                  "Type <awaken> when in a dream state to wake up and move around in your home. \n"
                  "Type <sleep> when in the real world to return to your dream. \n"
                  "Type <score> to view your current score. \n"
                  "Type <moves> to see how many moves you have left. \n"
                  "Type <quit> to exit the game. \n"
                  "Type <look> to view information about your location. "
                  "If any special commands are possible at your location, (such as <speak>), "
                  "typing <look> will also inform you of this. \n"
                  "Type <search> to look for an item in your location. \n"
                  "Type <take [item name]> to take an item once you find it. \n"
                  "For example, once you find the map, type <take map> to pick it up (it is near the start). \n"
                  "Once the map is found typing <map> will view it. "
                  "Similarly to the map, every item serves a purpose, even if it cannot be used directly. \n"
                  "Some items can be used by typing <use [item name]>, but for others, you will be prompted to use it when the time is right. \n"
                  "Type <inv> to view your inventory. \n"
                  "Type <speak> to talk to any people present at your current location when prompted. \n"
                  "Type <help> at any point to view these commands again. \n"
                  "All commands should be typed in lower case and without the <>. \n")
        if userAction == "quit":
            quit()
        if userAction == "search":
            playerSearch(locInfo)
        if userAction == "take map":
            if locInfo == 2 and "Map" not in inventory:
                retrieve(locInfo)
                items[2] = None
            else:
                print("There is no map here")
        if userAction == "use necklace" or userAction == "use expensive necklace":
            if "Expensive Necklace" in inventory and necklace == 0:
                print("You have put on the expensive necklace")
                necklace = 1
            elif "Expensive Necklace" in inventory and necklace ==1:
                print("You are already wearing the expensive necklace")
            else:
                print("You do not have the expensive necklace")
        if userAction == "use exotic garments" or userAction == "use garments":
            if "Exotic Garments" in inventory and garments == 0:
                print("You have put on the exotic garments")
                garments = 1
            elif "Exotic Garments" in inventory and garments == 1:
                print("You are already wearing the exotic garments")
            else:
                print("You do not have the exotic garments")
        # the following set of if statements lets a user take an item, but they must state it by name.
        # once the item is taken, the element representing that item is set to None
        # this prevents the user from duplicating items by taking it multiple times
        if userAction[0:8] == "take exo" or userAction == "take garments":
            if locInfo == 3 and "Exotic Garments" not in inventory:
                retrieve(locInfo)
                items[3] = None
            else:
                print("There are no Exotic Garments here")
        if userAction == "take ornament":
            if locInfo == 1 and "Ornament" not in inventory:
                retrieve(locInfo)
                print("This item can be useful in convincing certain people. "
                      "Type <use garments> to put it on")
                items[4] = None
            else:
                print("There is no Ornament here")
        if userAction == "take family photo" or userAction == "take photo":
            if locInfo == 5 and "Family Photo" not in inventory:
                retrieve(locInfo)
                items[5] = None
            else:
                print("The Family Photo is not here")
        if userAction == "take strange gem":
            if locInfo == 7 and "Strange Gem" not in inventory:
                retrieve(locInfo)
                items[8] = None
            else:
                print("There is no Strange Gem here")
        if userAction == "take dream shard":
            if locInfo == 9 and "Dream Shard" not in inventory:
                retrieve(locInfo)
                items[9] = None
            else:
                print("There is no Dream Shard here")
        if userAction == "take shrine key" or userAction == "take key":
            if locInfo == 9 and "Shrine Key" not in inventory:
                retrieve(locInfo)
                print("Use this to get back into the shrine if you get locked out")
                items[8] = None
            else:
                print("There is no Shrine Key here")
        if userAction == "take blanket":
            if locInfo == 12 and "Blanket" not in inventory:
                retrieve(locInfo)
                items[12] = None
            else:
                print("There is no Blanket here")
        if userAction == "take necklace" or userAction == "take expensive necklace":
            if locInfo == 15 and "Expensive Necklace" not in inventory:
                retrieve(locInfo)
                items[15] = None
                print("This item can be useful in convincing certain people. "
                      "Type <use necklace> to put it on")
            else:
                print("The expensive Necklace is not here")
        if userAction == "use shrine key" or userAction == "use key":
            if shrineState == 4:
                print("There is nothing left in the shrine for you to destroy, you monster.")
            elif locInfo == 7 and "Shrine Key" in inventory and shrineOpen == False:
                print("You use the key to break back into the shrine")
                shrineBreakIn()
            elif shrineOpen == True:
                print("The shrine is not locked, you can enter any time you wish.")
            else:
                print("You are not in front of the shrine or you do not have the Shrine Key")  
        if userAction == "drop":
            dropItem(locInfo)
        if userAction[0:3] == "inv":
            print(inventory)
        if userAction == "stuck":
            print("There are 12 locations. Each one must be visited in order to win. \n"
                  "Type <search> at every location and then <take [item name]> if something is found. \n"
                  "You must find all items, except the Dream Shard, to pass the final stage of the game. \n"
                  "DO NOT try to visit the final location without finding the Dream Shard. You will die.")
        if userAction == "map" or userAction == "use map":
            # map only works if player has map in their inventory, otherwise it informs them that they cannot view map yet.
            if "Map" in inventory and locInfo <= 11:
                print(
                       "                                                 Fiery Throne        \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                             Balcony  ========== Blackened Water     \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       " House Interior ========= Guardian's Lair ========== Path of Agony ====== Shrine \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "  Home Town ============== Dinner Table ============= Cliff     \n"
                       "     ||                         ||                              \n"                  
                       "     ||                         ||                              \n"
                       "     ||                         ||                              \n"
                       "     ||                         ||                              \n"
                       "   Meadow ================== Grey Room                          \n"
                      )
            if "Map" in inventory and locInfo >= 12:
                print("  Living Room ============= The Hallway ============ Kitchen     \n"
                      "                                 ||                              \n"
                      "                                 ||                              \n"
                      "                                 ||                              \n"
                      "                                 ||                              \n"
                      "                         "+playerName+"'s Room \n"
                      )
            if "Map" not in inventory:
                print("You have not yet found the map")
        elif locInfo == 4 and coldManState == 0:
            print("A man lies near the edge of the cliff. "
                    "Perhaps you should try to <speak> to him?")
        elif locInfo == 4 and coldManState == 3:
            print("The man at the cliff's ashes lie where you killed him.")
        elif locInfo == 4 and coldManState == 1:
            print("The man at the cliff is content now that you have given him a blanket.")
        elif locInfo == 4 and coldManState == 2:
            print("The man at the cliff is angry with you for stealing his coin.")
                
            

def goTo(x):
    global score
    global hasBeenThere
    global locNames
    global moves
    global locInfo
    global locationCheck
    # goTo only occurs if the player actually moves somewhere, so 1 is added to the move number each time this executes.
    moves = moves + 1
    curLocation = locNames[x]
    if hasBeenThere[x] == False:
        score = score + 5
        hasBeenThere[x] = True
    # triggers the final encounter scene only if at "land"
    if curLocation == locNames[11]:
        finalEncounter(locInfo)
        
# special function for handling the final location of the game, where the player could potentially win or lose the game
def finalEncounter(location):
    global score
    global locNames
    global locInfo
    global locationCheck
    if locationCheck[location] == False:
        print(locDescrips[locInfo])
        print('')
        locationCheck[location] = True
    else:
        print(locNames[locInfo])
        print('')
    finalDecision = input()
    #win by using the dream shard. lose instantly if you have failed to collect it
    if finalDecision == "use dream shard":
         if "Dream Shard" in inventory and score >= 55:
             gameEnd()
         else:
             input("You failed to collect the dream shard and cannot leave the dream")
             quit()
    else:
         if "Dream Shard" in inventory and score >= 55:
             secondTry = input("Use the Dream Shard!")
             if secondTry == "use dream shard":
                 gameEnd()
             elif secondTry != "use dream shard":
                 input("You have failed to use the dream shard in time")
                 quit()
             else:
                 input("You have failed to use the dream shard in time")
                 quit()
         else:
             input("You have failed to collect the dream shard.")
             quit()
    
                    
def whereTo(location,userAction):
    global world
    global locInfo
    # decide what variables to use in the matrix based on user input
    if userAction == "north":
        direction = 0
    elif userAction == "south":
        direction = 1
    elif userAction  == "east":
        direction = 2
    elif userAction == "west":
        direction = 3
    # now we check matrix coordinates with these variables for our next location.
    # location was decided by locInfo variable and direction based on what direction was chosen
    nextLocation = world[location][direction]
    if nextLocation is None:
        print("There is nothing in that direction.")
    else:
        # update locInfo and pass what we got from the matrix coordinate through goTo
        locInfo = nextLocation
        goTo(nextLocation)

def showLocation(location):
    global locInfo
    global hasBeenThere
    global locationCheck
    global moves
    # display long location description if location has not been visited
    if locationCheck[location] == False:
        print(locDescrips[locInfo])
        locationCheck[location] = True
    else:
        # display short location name otherwise
        print(locNames[locInfo])

def playerSearch(s):
    global locInfo
    global hasBeenSearched
    global items
    global world
    # if they have not searched yet and there is an item present at current location, tell them what item is present
    if items[locInfo] == "Family Photo" and hasBeenThere[3] == True:
        print("The Family Photo you see on the stand can be taken. \n"
              "Perhaps you should bring it back to the mirror image of yourself at the table...")
        hasBeenSearched[s] = True
    elif items[locInfo] == "Family Photo":
        print("The Family Photo you see on the stand can be taken.")
        hasBeenSearched[s] = True
    elif items[locInfo] != None:
        print("While searching the area, you find a", items[locInfo], "for the taking.")
        # this allows them to take the item at the location with the <take> command
        hasBeenSearched[s] = True
    else:
        print("You find nothing worth taking in this area.")

def retrieve(locInfo):
    global score
    # only allow player to take an item if they have searched and there is an item in the location
    if hasBeenSearched[locInfo] is True:
        # add new item to inventory list and inform player of successful take
        inventory.append(items[locInfo])
        print("You have picked up a", items[locInfo]+".")
        score = score + 5
    else:
        print("You find nothing worth taking in this area. Try <search> if you have not already")

def dropItem(locInfo):
    # ask player what item they want to drop and put down the item they choose
    # the player can still choose to pick the item up again
    itemChoice = input("What item do you want to drop? ")
    if itemChoice == "map":
        if "Map" in inventory:
            inventory.remove("Map")
            items[2] = "Map"
            score = score - 5
        else:
            print("You do not have a map")
            print('')
    if itemChoice == "exotic garments":
        if "Exotic Garments" in inventory:
            inventory.remove("Exotic Garments")
            items[3] = "Exotic Garments"
            score = score - 5
        else:
            print("You do not have the Exotic Garments")
            print('')
    if itemChoice == "ornament":
        if "Ornament" in inventory:
            inventory.remove("Ornament")
            items[1] = "Ornament"
            score = score - 5
        else:
            print("You do not have the Ornament")
            print('')
    if itemChoice == "Family Photo":
        if "Family Photo" in inventory:
            inventory.remove("Family Photo")
            items[5] = "Family Photo"
            score = score - 5
        else:
            print("You do not have the Family Photo")
            print('')
    if itemChoice == "strange gem" or itemChoice == "gem":
        if "Strange Gem" in inventory:
            inventory.remove("Strange Gem")
            items[7] = "Strange Gem"
            score = score - 5
        else:
            print("You do not have the Strange Gem")
            print('')
    if itemChoice == "dream shard":
        if "Dream Shard" in inventory:
            print("You cannot drop essential items!")
            print('')
        else:
            print("You do not have the Dream Shard")
            print('')

def speechCheckOne():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global questionThreeAsked
    global morality
    if locInfo == 3 and "Family Photo" in inventory and morality > -3:
                if morality >= -2 and morality <= 2:
                    print("\"Well, hello there.\" He greets you.")
                if morality >= 3:
                    print("\"I haven't seen such a friendly face in a while! Greetings!\" He says to you, happily")
                consciousQuestion = input("What would you like to say (type the # of the response you want)?\n"
                                       "1 - Who are you? \n"
                                       "2 - How can I find out who burned my home and killed my family? \n"
                                       "3 - Why does this dream occur every time I sleep? \n"
                                       "4 - (show him the family photo) Why am I missing from this family portrait? \n "
                                          "I was certainly in the photo when it was taken \n"
                                       "5 - (End conversation)\n")      
                if consciousQuestion == "1":
                    print("\"I'm you, "+playerName+". Or, your subconscious, rather. "
                          "I can plainly say things that you subsciously know but are unable to recognize.\"")
                elif consciousQuestion == "2":
                    questionTwo = input("\"Now, that's a tough one. You had a lot of enemies in life, but you don't suspect any of them. "
                          "Why is that?\"\n"
                          "1 - Are you suggesting someone I know who isn't an enemy of mine did it? \n"
                          "2 - (End Conversation)\n")
                    if questionTwo == "1":
                        print("\"Have you not always suspected that to be possible?\"")
                elif consciousQuestion == "3":
                    print("\"Because you feel guilty for running away and it's been eating away at you for years. "
                          "My guess would be that you've had enough and want answers.\"")
                elif consciousQuestion == "4":
                    questionThree = input("\"Your subconscious has removed you from the picture out of guilt. \n "
                                          "Now, whether that is just guilt for running away, survivor guilt,"
                                          "or something much more serious, I do not wish to answer.\"\n"
                                          "1 - Why must everything be so cryptic? Why cant you just tell me, dammit! \n"
                                          "2 - (End Conversation)\n")
                    if questionThreeAsked == False:
                        score = score + 20
                        questionThreeAsked = True
                    if questionThree == "1":
                        print("\"That's your fault, you know. I'm only doing what you would do in the same situation. \n"
                              "Subconsciously, you love messing with people and playing games.\"")
    elif locInfo == 3 and "Family Photo" not in inventory and morality > -3:
                consciousQuestion = input("What would you like to say (type the # of the response you want)?\n"
                                       "1 - Who are you? \n"
                                       "2 - How can I find out who burned my home and killed my family? \n"
                                       "3 - Why does this dream occur every time I sleep? \n"
                                       "4 - (End conversation)\n")      
                if consciousQuestion == "1":
                    print("\"I'm you, "+playerName+". Or, your subconscious, rather. "
                          "I can plainly say things that you subsciously know but are unable to recognize.\"")
                elif consciousQuestion == "2":
                    questionTwo = input("\"Now, that's a tough one. You had a lot of enemies in life, but you don't suspect any of them. "
                          "Why is that?\"\n"
                          "1 - Are you suggesting someone I know who isn't an enemy of mine did it?\n"
                          "2 - (End Conversation) \n")
                    if questionTwo == "1":
                        print("\"Have you not always suspected that to be possible?\"")
                elif consciousQuestion == "3":
                    print("\"Because you feel guilty for running away and it's been eating away at you for years. "
                          "My guess would be that you've had enough and want answers.\"")
    else:
        print("Leave now. You should feel ashamed of how sadistic and evil you are")
        
def cliffEncounter():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global coldManState
    global morality
    global inventory
    if locInfo == 4 and "Cursed Dagger" not in inventory and coldManState == 2:
        print("\"Go away!!! You've already taken the one thing I had. What more do you want from me?\"\n")
    elif locInfo == 4 and "Cursed Dagger" in inventory and coldManState == 2:
        attackChoice = input("\"Go away!!! You've already taken the one thing I had. What more do you want from me?\"\n"
                             "1 - (Kill him using the cursed dagger)"
                             "2 - (Leave)")
        if attackChoice == "1":
            print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                  "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess. "
                  "You are certain that the man experienced some of the most pain possible while he slowly died.")
            coldManState = 3
    elif locInfo == 4 and coldManState == 1 and "Cursed Dagger" in inventory:
        print("\"Thank you again for the blanket!\"\n")
        attackChoiceTwo = input("1 - (Kill him using the cursed dagger)"
                                "2 - (Leave)")
    elif locInfo == 4 and coldManState == 1 and "Cursed Dagger" not in inventory:
        print("\"Thank you again for the blanket!\"\n")
    elif locInfo == 4 and coldManState == 0:
        print("As you approach the man, you can see that is barely clothed and is freezing from the cold. "
                        "However, you also notice that he is clutching a Rare Coin to his chest.")
        helpMan = input("What would you like to do (type the # of the action you want)?\n"
                        "1 - (Give him a blanket) \n"
                        "2 - (Steal his Rare Coin) \n"
                        "3 - (Stab him) \n"
                        "4 - (Leave him to freeze) \n")
        if helpMan == "1":
            if "Blanket" in inventory:
                print("\"Oh, thank you kind sir! I thought I might freeze to death!\"")
                inventory.remove("Blanket")
                coldManState = 1
                morality = morality + 1
            elif "Blanket" not in inventory:
                print("You do not have the item required to perform this action")
        if helpMan == "2":
            print("\"No! Don't take it from me!\" The man says. "
                  "He tries to stop you, but he is too weak to stop you from ripping it from his clutches")
            inventory.append("Rare Coin")
            coldManState = 2
            morality = morality - 2
        if helpMan == "3":
            if "Cursed Dagger" not in inventory:
                print("You lack the required item to perform this action")
            elif "Cursed Dagger" in inventory:
                print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                  "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess. "
                  "You are certain that the man experienced some of the most pain possible while he slowly died.")
                coldManState = 3
                morality = morality - 5
                
        
        
def guardianEncounter():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global necklace
    if "Ornament" in inventory and "Strange Gem" in inventory and "Rare Coin" in inventory:
        guardianRequest = 1
    input("As you try to continue, a guardian suddenly appears and blocks your way, preventing you from going forward. "
          "You must find some way to deal with him in order to continue. "
          "There are several hidden ways to do this, doing his bidding is not the only way. Press ENTER to hear his words... \n")
    if score < 50:
          print("\"Bah! You've hardly accomplished anything here. Come back when you've done more!\"")
    elif score >= 50:
        print("\"Seems like you've done quite a bit around here. So, here's the deal. "
              "I'll let you pass if you bring me my ornament and my gem. "
              "I also spotted a rare coin that I fancy and want you to bring that to me as well.\"")
        guardianChoice = input("What would you like to do (type the # of the action you want)?\n"
                                "1 - (Give him the items) \n"
                                "2 - (Kill the guardian) \n"
                                "3 - (Try to convince him to let you pass) \n"
                                "4 - I will come back later \n")
        if guardianChoice == "1":
            if guardianRequest == 1:
                print("\"Ah, thank you. You have done me a great service. You are free to pass.\"\n")
                print("The guardian disappears, allowing you to move forward freely")
                inventory.remove("Strange Gem")
                inventory.remove("Rare Coin")
                inventory.remove("Ornament")
                guardianState = 2
            else:
                print("\"Is this some kind of joke? You do not have all the items I requested.\"")
        if guardianChoice == "2":
            if "Cursed Dagger" not in inventory:
                print("The guardian is far stronger than you and would kill you instantly if you tried fighting him. "
                      "Perhaps if you had some sort of weapon you'd stand a chance...")
            if "Cursed Dagger" in inventory:
                print("You plunge the dagger into the guardian's heart. He screams in sheer pain as the dagger begins to disintegrates his life essense\n"
                      "Before dying, he bellows \"WHY HAVE YOU DONE THIS? YOU TRULY ARE EVIL SCUM AND DESERVE THE WORST OF FATES! YOU WILL RECEIVE WHAT YOU DESERVE\""
                      "The guardian fades into dust as he dies.\n"
                      "The path is now clear")
                morality = morality - 1
                guardianState = 3
        if guardianChoice == "3":
            if necklace == 1 and garments == 1:
                print("\"You know, you do seem like a citizen of high stature. I will let you pass.\"")
                print("The guardian disappears, allowing you to move forward freely")
                guardianState = 1
            else:
                print("The guardian laughs in your face and refuses to let you pass. "
                      "Perhaps if you could fool him somehow he would step aside...")

def shrineEncounter():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global necklace
    global shrineState
    global shrineOpen
    global morality
    global inventory
    if shrineState == 0:
        helpWoman = input("\"Please ser, you have to help me!\n"
                                "1 - What's wrong? \n"
                                "2 - (Refuse to help her) \n")
        if helpWoman == "1":
            print("\"My husband has become possessed! "
                  "He's obsessed with this dagger and worships it day and night! I think it is cursed! "
                  "He refuses to go find food and I don't want to leave our child here with him. \n"
                  "Can you please find us some food before we starve to death?")
            acceptQuest = input("1 - I will find him some food \n"
                                "2 - (Ignore her and take the dagger)\n"
                                "3 - You can all eat dirt, I don't care about you or your deadbeat husband \n"
                                "4 - (Give her food)\n"
                                "5 - (End Conversation)")
            if acceptQuest == "1":
                  print("\"Thank you! Come back as soon as you can!\"")
                  shrineState = 1
            if acceptQuest == "2":
                  print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path"
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
                  killOrSpare = input("What will you do? \n"
                        "1 - (Kill him using the dagger) \n"
                        "2 - (Put the dagger back)")
                  if killOrSpare == "1":
                        print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body until nothing remains. Soon, the man is nothing but ashes. "
                              "However, as you are killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        morality = morality - 10
                        inventory.append("Cursed Dagger")
                        shrineState = 5
                        shrineOpen = False
                        locInfo = 7
            if acceptQuest == "3":
                print("\"Leave us, then!\"")
                morality = morality - 1
                shrineState = 2
            if acceptQuest == "4":
                if "Food" in inventory:
                    print("\"Thank you kindly, ser! We certainly would have starved without your help! "
                          "If you wish to help further, <speak> to me again. I have another task for you\"")
                    inventory.remove("Food")
                    shrineState = 1
                else:
                    print("You do not have the item required to perform that action")
    if shrineState == 2:
        acceptQuest = input("1 - I have changed my mind, I will find him some food. \n"
                             "2 - (Give her food) \n"
                             "3 - (End Conversation)")
        if acceptQuest == "1":
            print("\"Thank you! Come back as soon as you can!\"")
        if acceptQuest == "2":
            if "Food" in inventory:
                print("\"Thank you kindly, ser! We certainly would have starved without your help! "
                      "If you wish to help further, <speak> to me again. I have another task for you\"")
                inventory.remove("Food")
                morality = morality + 2
                shrineState = 1
            else:
                print("You lack the required item to perform that action")

def shrineBreakIn():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global necklace
    global shrineState
    global shrineOpen
    global morality
    global inventory
    print("The woman screams as you break back into the shrine, cursed dagger in hand")
    evilChoice = input("What will you do?\n"
                       "1 - (Kill her and her son) \n"
                       "2 - (Leave)")
    if evilChoice == "1":
        print("You slaughter the mother and child mercilessly with the cursed dagger. "
              "Turning to leave the shrine, you hear their screams dissipate as the cursed energy from the dagger disintegrates their bodies. "
              "There is no going back from the evil path you have embarked on.")
        shrineState = 4
        morality = morality - 20

def shrineQuestTwo():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global necklace
    global shrineState
    global shrineOpen
    global morality
    global inventory
    if shrineState == 1:
        print("\"I have another job for you. You need to convince my husband that this dagger needs to be destroyed. "
              "It carries evil energy and I fear for our lives if it is allowed to remain. There is a body of black water "
              "past the Balcony that has the power to destroy evil artifacts. If you can convince my husband to let you take it, "
              "you must <drop> it when at the Blackened Water.\"")
        daggerQuestAccept = input("1 - Yes, I will talk to him \n"
                                  "2 - (End Conversation)")
        if daggerQuestAccept == "1":
            shrineState == 9
            daggerQuestBegin = input("\"Would you like to go speak with him now?\""
                                     "1 - Yes, bring me to him \n"
                                     "2 - No, I will do so later")
            if daggerQuestBegin == "1":
                print("The woman brings you to her husband")
                husbandSpeechCheck = input("He gets up from kneeling in front of the shrine."
                                           "\"What do you want?!?\" He yells, angrily. \n"
                                           "1 - That dagger is evil and must be destroyed. Give it to me so I can do so. \n"
                                           "2 - (End Conversation)")
                if husbandSpeechCheck == "1":
                    if garments == 1:
                        print("\"Really? Huh. Well, if you say so. You have been a great help so far anyway.\"\n"
                              "The man hands you the dagger.")
                        inventory.append("Cursed Dagger")
                        shrineState = 10
                    else:
                        print("\"You can have it over my dead body! Begone from my sight!\"")
                        shrineState = 9
        else:
            shrineState == 9
    if shrineState == 9:
        daggerQuestBegin = input("\"Would you like to go speak with my husband now?\""
                                     "1 - Yes, bring me to him \n"
                                     "2 - No, I will do so later")
        if daggerQuestBegin == "1":
            print("The woman brings you to her husband")
            husbandSpeechCheck = input("He gets up from kneeling in front of the shrine."
                                           "\"What do you want?!?\" He yells, angrily. \n"
                                           "1 - That dagger is evil and must be destroyed. Give it to me so I can do so. \n"
                                           "2 - (End Conversation)")
            if husbandSpeechCheck == "1":
                if garments == 1:
                    print("\"Really? Huh. Well, if you say so. You have been a great help so far anyway.\"\n"
                              "The man hands you the dagger.")
                    inventory.append("Cursed Dagger")
                    shrineState = 10
                else:
                    print("\"You can have it over my dead body! Begone from my sight!\"")
    if shrineState == 10:
        print("\"Thank you so much for taking the dagger. I hope that you will destroy it like I asked\"")
            
        
                                      
def gameEnd():
    print("Congratulations on completing the game! This game has 3 possible endings. "
          "If you want to know how to achieve the other two, just ask me!")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)
    
def main():
    showIntro()
    gameLoop()

main()
