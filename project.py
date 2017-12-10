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
familyHonored = 0
daggerState = 0
shrineOpen = True
familyPhoto = False

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
          "Recently, you have been having very detailed lucid dreams containing strange details about your past and the day of the fire. "
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
               "You arrive at a dinner table that you recognize from your old home.",
               "You arrive at the edge of a cliff, beyond which a dark abyss lies.",
               "Inside the house, you find that the walls are covered with black and white pictures of your family"
               " that were taken before they died mysteriously years ago."
               " Eerily enough, you are missing from all the pictures as if you were cropped out of them.",
               " You come across a large room that appears to be a lair for a creature of some sort."
               " A broken section of the wall reveals a balcony straight ahead. ",
               "Walking down the path, you witness many villagers screaming in agony and running down the street."
               " You are curious as to what could have possibly driven them insane.",
               "At the end of the path of agony, a small family sits around a small shrine. "
               "On the shrine lies a glowing dagger that seems to be the subject of their worship. It radiates with evil energy. "
               "The mother of the family sits alone in a corner looking very distraught. Perhaps you should try to <speak> to her?",
               "With the guardian gone, you exit his lair through the broken section of the wall",
               "Using a ladder, you climb down from the balcony into the black water. "
               "The water seems to be filled with a destructive energy. "
               "In front of you lies a pair of opaque stairs leading to an empty throne.",
               "You climb up the stairs till you reach the platform containing the unoccupied throne.",
               "You wake up from your dream alone in your room. "
               "The items you collected in your dream transfer over, so the <map> command will still work if you found the map. "
               "Type <sleep> to return to your dream.",
               "You are in the hallway. From here, you can enter your kitchen or your living room.",
               "Looks like you left the stove in your kitchen on by accident earlier. The room reaks of carbon monoxide.",
               "The movie \"Inception\" plays on your living room television."]

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
            "Black Water", "Throne of Dreams", "Your Room", "The Hallway", "The Living Room", "The Kitchen"]

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
blackWater = 10
throneOfDreams = 11
yourRoom = 12
hallway = 13
livingRoom = 14
kitchen = 15
# locInfo stores the number of the location you're in, making creating additional functions far easier.
# locInfo is repeatedly updated throughout the functions in this program
locInfo = 0
# matrix for the game world
         # N     S     E      W
world = [[2,  None,     1,  None] # meadow
        ,[3,  None,  None,     0] # grey room
        ,[5,     0,     3,  None] # home town
        ,[6,     1,     4,     2] # dinner table
        ,[7,  None,  None,     3] # cliff
        ,[None,  2,     6,  None] # house interior
        ,[9,     3,     7,     5] # guardian's lair
        ,[None,  4,     8,     6] # path of agony
        ,[None,  None,   None, 7] # shrine
        ,[None,  6,  10,  None] # balcony
        ,[11,  None,  None,  9] # blackened water
        ,[None,10, None,  None] # fiery throne
        ,[13, None, None, None] # your room
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
    global morality
    global score
    global familyHonored
    global familyPhoto
    while True:
        showLocation(locInfo)
        userAction = input("Enter Command: ").lower()
        # only address the whereTo function if the user decides to move somewhere
        if userAction == "north" and locInfo == 6 and guardianState == 0:
            guardianEncounter()
        elif userAction == "east" and shrineState == 3 and locInfo == 7 and "Shrine Key" not in inventory:
            print("The shrine is locked and you cannot enter")
        elif userAction == "east" and shrineState == 3 and locInfo == 7 and "Shrine Key" in inventory:
            print("The shrine is locked. Maybe if you <use shrine key> you will be able to enter.")
        elif userAction =="east" and shrineState == 4 and locInfo == 7:
            print("There is nothing left in the shrine for you to destroy, you monster")
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
                print("You awaken from your slumber.")
                print('')
                locInfo = 12
            elif locInfo >= 12:
                print("You are already awake.")
        if userAction == "sleep":
            if locInfo >= 12:
                print("You go back to your bed and return to the dream world.")
                print('')
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
        if userAction == "use ring":
            if "Wedding Ring" in inventory and locInfo == 0 and familyHonored == 1:
                ringSequence()
            elif "Wedding Ring" in inventory and locInfo != 1:
                print("You cannot use the ring here")
            elif "Wedding Ring" not in inventory and familyHonored != 1:
                print("You have already used your ring")
            elif "Wedding Ring" not in inventory:
                print("You do not have the ring")
        if userAction == "use necklace" or userAction == "use expensive necklace":
            if "Expensive Necklace" in inventory and necklace == 0:
                print("You have put on the expensive necklace")
                score = score + 5
                necklace = 1
            elif "Expensive Necklace" in inventory and necklace ==1:
                print("You are already wearing the expensive necklace")
            else:
                print("You do not have the expensive necklace")
        if userAction == "use exotic garments" or userAction == "use garments":
            if "Exotic Garments" in inventory and garments == 0:
                print("You have put on the exotic garments")
                garments = 1
                score = score + 5
            elif "Exotic Garments" in inventory and garments == 1:
                print("You are already wearing the exotic garments")
            else:
                print("You do not have the exotic garments")
        # the following set of if statements lets a user take an item, but they must state it by name.
        # once the item is taken, the element representing that item is set to None
        # this prevents the user from duplicating items by taking it multiple times
        if userAction[0:8] == "take exo" or userAction == "take garments":
            if locInfo == 3 and "Exotic Garments" not in inventory:
                score = score + 5
                retrieve(locInfo)
                items[3] = None
            else:
                print("There are no Exotic Garments here")
        if userAction == "take ornament":
            if locInfo == 1 and "Ornament" not in inventory:
                score = score + 5
                retrieve(locInfo)
                print("This item can be useful in convincing certain people. "
                      "Type <use garments> to put it on")
                items[4] = None
            else:
                print("There is no Ornament here")
        if userAction == "take family photo" or userAction == "take photo":
            if locInfo == 5 and "Family Photo" not in inventory:
                score = score + 5
                retrieve(locInfo)
                familyPhoto = True
                items[5] = None
            else:
                print("The Family Photo is not here")
        if userAction == "take strange gem" or userAction == "take gem":
            if locInfo == 7 and "Strange Gem" not in inventory:
                score = score + 5
                retrieve(locInfo)
                items[7] = None
            else:
                print("There is no Strange Gem here")
        if userAction == "take dream shard" or userAction == "take shard":
            if locInfo == 9 and "Dream Shard" not in inventory:
                retrieve(locInfo)
                items[9] = None
            else:
                print("There is no Dream Shard here")
        if userAction == "take shrine key" or userAction == "take key":
            if locInfo == 8 and "Shrine Key" not in inventory:
                score = score + 5
                retrieve(locInfo)
                print("Use this to get back into the shrine if you get locked out")
                items[8] = None
            else:
                print("There is no Shrine Key here")
        if userAction == "take blanket":
            if locInfo == 12 and "Blanket" not in inventory:
                score = score + 5
                retrieve(locInfo)
                items[12] = None
            else:
                print("There is no Blanket here")
        if userAction == "take necklace" or userAction == "take expensive necklace":
            if locInfo == 15 and "Expensive Necklace" not in inventory:
                score = score + 5
                retrieve(locInfo)
                items[15] = None
                print("This item can be useful in convincing certain people. "
                      "Type <use necklace> to put it on")
            else:
                print("The expensive Necklace is not here")
        if userAction == "take food":
            if locInfo == 14 and "Food" not in inventory:
                score = score + 5
                retrieve(locInfo)
                items[14] = None
                print("This item can be used for a quick score boost, but it has another hidden purpose...")
            else:
                print("There is no food here")
        if userAction == "use shrine key" or userAction == "use key":
            if locInfo == 7 and "Shrine Key" in inventory and shrineOpen == False:
                print("You use the key to break back into the shrine")
                score = score + 10
                shrineBreakIn()
            elif shrineOpen == True:
                print("The shrine is not locked, you can enter any time you wish.")
            else:
                print("You are not in front of the shrine or you do not have the Shrine Key")
        if userAction == "use food" or userAction == "eat food":
            if "Food" in inventory and locInfo == 8:
                print("\"How could you eat that in front of us, you monster?!\"")
                morality = morality - 1
                score = score + 5
                shrineState = 11
                inventory.remove("Food")
            elif "Food" in inventory:
                score = score + 5
                inventory.remove("Food")
            else:
                print("You do not have food in your inventory")
        if userAction == "drop":
            dropItem(locInfo)
        if userAction[0:3] == "inv":
            print(inventory)
        if userAction == "summon":
            if locInfo == 11 and "Dream Shard" in inventory:
                finalChoice = input("Are you sure you wish to summon? "
                                    "Once you do this, the final sequence of the game begins.There will be no turning back. "
                                    "Remember, there is a second world accessible with <awaken> and exitable with <sleep>\n"
                                    "Summon?(yes/no): ")
                if finalChoice[0:1] == "y":
                    finalEncounter()
            elif "Dream Shard" not in inventory:
                print("You lack the item required to summon. Judging by the aesthetic of the throne, "
                      "whatever item you need to <summon> has something to do with dreams.")
            elif "Dream Shard" in inventory:
                print("You cannot summon from here. Try going toward the throne in the distance")
        if userAction == "stuck":
            print("in progress")
        if userAction == "map" or userAction == "use map":
            # map only works if player has map in their inventory, otherwise it informs them that they cannot view map yet.
            if "Map" in inventory and locInfo <= 11:
                print(
                       "                                                 Throne of Dreams        \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                                                       ||            \n"
                       "                             Balcony  ========== Blackened Water     \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       " House Interior ========= Guardian's Lair ======= Path of Agony ====== Shrine \n"
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
        elif locInfo == 3:
            print("A mirror image of yourself sits at the dinner table. "
                  "Perhaps you should try to <speak> to him?")
        elif locInfo == 11:
            print("The throne is unoccupied. Perhaps you should try to <summon> the owner.")
                
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
    if items[locInfo] != None:
        # add new item to inventory list and inform player of successful take
        inventory.append(items[locInfo])
        print("You have picked up a", items[locInfo]+".")
        score = score + 5
    else:
        print("You find nothing worth taking in this area. Try <search> if you have not already")

def dropItem(locInfo):
    global daggerState
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
    if itemChoice == "cursed dagger" or itemChoice == "dagger":
        if "Cursed Dagger" in inventory and locInfo == 10:
            print("The dagger shakes violently and then explodes the moment it makes contact with the water")
            inventory.remove("Cursed Dagger")
            morality = morality + 2
            score = score + 15
            daggerState = 1
        elif "Cursed Dagger" in inventory:
            print("You cannot drop the Cursed Dagger at this location")
            print('')
        else:
            print("You do not have the Cursed Dagger")

def speechCheckOne():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global questionThreeAsked
    global morality
    global familyHonored
    if locInfo == 3 and "Family Photo" in inventory:
                if morality >= -4 and morality <= 4:
                    print("\"Well, hello there.\" He greets you.")
                elif morality >= 5:
                    print("\"I haven't seen such a friendly face in a while! Greetings!\" He says to you, happily")
                elif morality <= -5 and morality >= -9:
                    print("\"You're scum. But, I'm sure you know that, right?\"")
                elif morality <= -10:
                    print("\"I greatly disprove of your evil actions. I beg of you, change your ways!\"")    
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
                        print("\"That's your fault, you know. I'm only doing what you would do in the same situation. "
                              "Subconsciously, you love messing with people and playing games.\"")
                        if familyHonored == 0:
                            print("In any case, I'm glad you're demonstrating curiosity.\n"
                                  "Here, take the ring you gave your wife. Go to the Meadow and <use ring>. I'm sure you'll see why.\n")
                            inventory.append("Wedding Ring")
                            familyHonored = 1
    elif locInfo == 3 and "Family Photo" not in inventory:
                if morality >= -4 and morality <= 2:
                    print("\"Well, hello there.\" He greets you.")
                elif morality >= 3:
                    print("\"I haven't seen such a friendly face in a while! Greetings!\" He says to you, happily")
                elif morality <= -5 and morality >= -9:
                    print("\"You're scum. But, I'm sure you know that, right?\"")
                elif morality <= -10:
                    print("\"I greatly disprove of your evil actions. I beg of you, change your ways!\"")  
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

def ringSequence():
    global familyHonored
    global morality
    global score
    if familyHonored == 1:
        print("You remember why this ring and the meadow are special.\n"
              "Not only was it your marriage ring, but this is where you proposed to her as well. "
              "She was so happy that years later during a cancer scare, "
              "she told you that if she didn't make it, she wanted to be buried in this same meadow where you proposed.")
        ringChoice = input("1 - (Bury the ring)\n"
                           "2 - (Destroy the ring)\n"
                           "3 - (Do nothing)\n")
        if ringChoice == "1":
            print("You honor your wife's legacy by burying the ring in the meadow")
            morality = morality + 2
            inventory.remove("Wedding Ring")
            score = score + 10
            familyHonored = 2
        if ringChoice == "2":
            print("You spite your wife and her death by destroying the ring")
            inventory. remove("Wedding Ring")
            morality = morality - 2
            score = score + 10
            familyHonored = 3
        
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
                             "1 - (Kill him with the cursed dagger) \n"
                             "2 - (Leave)")
        if attackChoice == "1":
            print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                  "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess. "
                  "You are certain that the man experienced some of the most pain possible while he slowly died.")
            coldManState = 3
    elif locInfo == 4 and coldManState == 1 and "Cursed Dagger" in inventory:
        print("\"Thank you again for the blanket!\"\n")
        attackChoiceTwo = input("1 - (Kill him with the cursed dagger)"
                                "2 - (Leave)")
    elif locInfo == 4 and coldManState == 1 and "Cursed Dagger" not in inventory:
        print("\"Thank you again for the blanket!\"\n")
    elif locInfo == 4 and coldManState == 0:
        print("As you approach the man, you can see that he is barely clothed and is freezing from the cold. "
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
            morality = morality - 3
        if helpMan == "3":
            if "Cursed Dagger" not in inventory:
                print("You lack the required item to perform this action")
            elif "Cursed Dagger" in inventory:
                print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                  "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess. "
                  "You are certain that the man experienced some of the most pain possible while he slowly died.")
                coldManState = 3
                morality = morality - 10
                
        
        
def guardianEncounter():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global necklace
    global morality
    if "Ornament" in inventory and "Strange Gem" in inventory and "Rare Coin" in inventory:
        guardianRequest = 1
    input("As you try to continue, a guardian suddenly appears and blocks your way, preventing you from going forward. "
          "You must find some way to deal with him in order to continue. "
          "There are several hidden ways to do this, doing his bidding is not the only way. Press ENTER to hear his words... \n")
    if score < 5 and guardianState == 0:
          print("\"Bah! You've hardly accomplished anything here. Come back when you've done more!\"")
          locInfo = 6
    elif guardianState == 0:
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
                locInfo = 6
            else:
                print("\"Is this some kind of joke? You do not have all the items I requested.\"")
                locInfo = 6
        if guardianChoice == "2":
            if "Cursed Dagger" not in inventory:
                print("The guardian is far stronger than you and would kill you instantly if you tried fighting him. "
                      "Perhaps if you had some sort of weapon you'd stand a chance...")
            if "Cursed Dagger" in inventory:
                print("You plunge the dagger into the guardian's heart. He screams in sheer pain as the dagger begins to disintegrates his life essense.\n"
                      "Before dying, he bellows \"WHY HAVE YOU DONE THIS? YOU TRULY ARE EVIL SCUM AND DESERVE THE WORST OF FATES!\" "
                      "The guardian fades into dust as he dies.\n"
                      "The path is now clear")
                morality = morality - 10
                guardianState = 3
                locInfo = 6
        if guardianChoice == "3":
            if necklace == 1 and garments == 1:
                print("\"You know, you do seem like a citizen of high stature. I will let you pass.\"")
                print("The guardian disappears, allowing you to move forward freely")
                guardianState = 1
                locInfo = 6
            else:
                print("The guardian laughs in your face and refuses to let you pass. "
                      "Perhaps if you could fool him somehow he would step aside...")
                locInfo = 6
        else:
            locInfo = 6

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
                  "He's obsessed with this dagger and worships it day and night! I think it is cursed; it has driven everyone mad! "
                  "He refuses to go find food and I don't want to leave our child here with him. \n"
                  "Can you please find us some food before we starve to death?\n")
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
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        morality = morality - 10
                        inventory.append("Cursed Dagger")
                        shrineState = 3
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
        print("What would you like to say?")
        acceptQuest = input("1 - I have changed my mind, I will find him some food. \n"
                             "2 - (Give her food)\n"
                             "3 - (Ignore her and take the dagger)\n"
                             "4 - (End Conversation)\n")
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
        if acceptQuest == "3":
            print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path"
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
            killOrSpareTwo = input("What will you do? \n"
                                   "1 - (Kill him using the dagger) \n"
                                   "2 - (Put the dagger back)")
            if killOrSpareTwo == "1":
                print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                      "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                      "a person's body until nothing remains. Soon, the man is nothing but ashes. "
                      "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                      "and lock the door.")
                morality = morality - 10
                inventory.append("Cursed Dagger")
                shrineState = 3
                shrineOpen = False
                locInfo = 7
    if shrineState == 11:
        evilChoiceTwo = input("\"What do you want? You're clearly not here to help us\"\n"
                              "1 - (Ignore her and take the dagger) \n"
                              "2 - (End conversation)\n")
        if evilChoiceTwo == "1":
                  print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path"
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
                  killOrSpareTwo = input("What will you do? \n"
                        "1 - (Kill him using the dagger) \n"
                        "2 - (Put the dagger back)")
                  if killOrSpareTwo == "1":
                        print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body until nothing remains. Soon, the man is nothing but ashes. "
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        morality = morality - 10
                        inventory.append("Cursed Dagger")
                        shrineState = 3
                        shrineOpen = False
                        locInfo = 7
                              
        

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
        shrineOpen = True
        shrineState = 4
        morality = morality - 20
        locInfo = 7
    else:
        print("You leave the shrine and they lock the door behind you again")

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
        print("\"You need to convince my husband that this dagger needs to be destroyed. "
              "It carries evil energy and I fear for our lives if it is allowed to remain. There is a body of black water "
              "past the Balcony that has the power to destroy evil artifacts. If you can convince my husband to let you take it, "
              "you must <drop> it when at the Blackened Water.\"")
        daggerQuestAccept = input("1 - Yes, I will talk to him \n"
                                  "2 - (End Conversation)")
        if daggerQuestAccept == "1":
            shrineState == 9
            daggerQuestBegin = input("\"Would you like to go speak with him now?\"\n"
                                     "1 - Yes, bring me to him \n"
                                     "2 - No, I will do so later\n")
            if daggerQuestBegin == "1":
                print("The woman brings you to her husband")
                husbandSpeechCheck = input("He gets up from kneeling in front of the shrine.\n"
                                           "\"What do you want?!?\" He yells, angrily. \n"
                                           "1 - That dagger is evil and must be destroyed. Give it to me so I can do so. \n"
                                           "2 - (End Conversation)\n")
                if husbandSpeechCheck == "1":
                    if garments == 1 or necklace == 1:
                        print("\"Really? Huh. Well, if you say so. You have been a great help so far anyway.\"\n"
                              "The man hands you the dagger.")
                        inventory.append("Cursed Dagger")
                        shrineState = 10
                    else:
                        print("\"You can have it over my dead body! Begone from my sight!\"")
        else:
            shrineState == 9
    if shrineState == 10:
        print("\"Thank you so much for taking the dagger. Please do not use it for anything, just destroy it!\"")

# special function for handling the final location of the game, where the player could potentially win or lose the game
def finalEncounter():
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
    global coldManState
    global familyHonored
    global daggerState
    global familyPhoto
    input("During this section, press ENTER when ... appears at the end to continue...\n")
    print("The shard glows vibrantly as you use it and a memory of your wife comes out from behind the throne to sit on it.\n"
          "\"It looks like you have finally reached the end, my love.\"")
    input("ENTER - What end? This cannot end until I know who took you from me!\n")
    input("\"You're still asking this? I cannot believe how blind you are to what is right in front of you. "
          "I'll save the answers for when we're done here. "
          "First, let's talk about what you've been doing in this dream world you've created for yourself...")
    if guardianState == 1:
        input("You passed the guardian with a non-violent approach, to your credit.\n"
              "...")
    if guardianState == 2:
        input("You did the guardian's bidding and stole from the man by the cliff.\n"
              "...")
    if guardianState == 3:
        input("You murdered the guardian with a cursed dagger when there were non-violent options available.\n"
              "...")
    if coldManState == 0:
        input("You did not help the freezing man by the cliff.\n"
              "...")
    if coldManState == 1:
        input("You were kind enough to give a blanket to the freezing man by the cliff.\n"
              "...")
    if "Rare Coin" in inventory:
        if coldManState != 3:
            input("You stole the Rare Coin from the old man, the only thing he had, and did not help him.\n"
                  "...")
        if coldManState == 3:
            input("You stole the Rare Coin from the old man and then proceeded to murder him needlessly.")
    elif coldManState == 3:
        input("You killed the old man with the cursed dagger for no reason other than bloodlust.\n"
              "...")
    if shrineState == 0:
        input("You did not feed the family at the shrine.\n"
              "...")
    if shrineState == 1 or shrineState == 9:
        input("You were kind enough to feed the family at the shrine, but you did not help save the father and destroy the cursed dagger.\n"
              "...")
    if shrineState == 2:
        input("You insulted the woman at the shrine and did not help her family.\n"
              "...")
    if shrineState == 3:
        input("You slaughtered the man at the shrine while his family watched just because you wanted the cursed dagger.\n"
              "...")
    if shrineState == 4:
        input("Not only did you murder the man at the shrine, but you also broke back into the shrine and slaughtered the rest of his family too. "
              "Was killing the man in front of his family and stealing the dagger really not enough for you?\n"
              "...")
    if shrineState == 10:
        input("You were kind enough to both feed the family at the shrine and save the father.\n"
              "...")
    if shrineState == 10:
        if coldManState == 3 and guardianState != 3:
            input("You fed the family and saved the husband, but you used the dagger to kill the helpless man at the cliff after the family gave it up. "
                  "Why do so much good only to erase it with pure evil?\n"
                  "...")
        if coldManState != 3 and guardianState == 3:
            input("You fed the family and saved the husband, but you used the dagger to kill the guardian after the family gave it up. "
                  "Why do so much good only to erase it with pure evil?\n"
                  "...")
        if coldManState == 3 and guardianState == 3:
            input("You fed the family and saved the husband, but you used the dagger to kill both the guardian and the helpless man at the cliff after the family gave it up. "
                  "Why do so much good only to erase it with pure, unadulterated evil?\n"
                  "...")
        if coldManState != 3 and guardianState != 3:
            input("You fed the family and saved the husband. For this, I applaud you.\n"
                  "...")
    if "Cursed Dagger" in inventory:
        input("You did not destroy the cursed dagger like you should have.\n"
              "...")
    if familyPhoto == False and hasBeenThere[5] == True:
        input("You neglected to collect your family photo.\n"
              "...")
    if "Family Photo" in inventory:
        input("You collected the family photo.\n"
              "...")
    if daggerState == 1:
        input("You destroyed the cursed dagger like you should have.\n"
              "...")
    if familyHonored == 0:
        input("And finally, you did not find my ring and honor my memory\n"
              "...")
    if familyHonored == 1:
        input("And finally, you found my ring, but neglected to honor my memory like your subconscious advised you.\n"
              "...")
    if familyHonored == 2:
        input("And finally, you honored my memory by burying my ring where I wanted to be buried.\n"
              "...")
    if familyHonored == 3:
        input("And finally, you disgraced my memory by destroying my ring.\n"
              "...")
    input("If I had to score your morality somehow, I'd give you a "+str(morality)+"...")
    if morality <= -10:
        input("Now that you understand how horrible of a person you are. I'll tell you exactly who murdered your family...")
        input("You did. You killed me. You killed our daughter. You killed our son...")
        input("In the middle of the night, while sleepwalking, you lit a match on the stove and torched the whole house. "
              "Conveniently, you then stumbled out of the house and collapsed, leaving us to burn to death while you fled the country...")
        endChoice = input("This dream world you've created and the atrocious acts you've committed in it only prove how terrible of a person you are, subconsciously. "
              "What happened that night was a demonstration of your true desires: destruction, death, and chaos. Do you see it now?\"\n"
              "1 - I don't believe you\n"
              "2 - I don't care, I had fun\n"
              "3 - I'm sorry\n"
              "4 - (Say Nothing)\n")
        if endChoice == "1":
            input("\"But you do. You know it's true and that's the real reason why you ran...\"")
        if endChoice == "2":
            input("\"You're evil and deserve to suffer...\"")
        if endChoice == "3":
            input("\"It's far too late for apologies...\"")
        print("Ultimately, it was your choice, " +playerName+ ". You chose to be evil. There's only one option left. "
              "You've always had this strange ability to bring things from your dreams into the real world, "
              "though it comes at a great cost and you nearly died last time you brought anything of significant back to the world. "
              "That's a risk you need to take this time. Transfer the Dream Shard out of here and use it; it will automatically reset the timeline to before you killed us.\"")
        while True:
            resetChoice = input("1 - Fine, I'll do it\n"
                                "2 - No, I refuse to do it\n")
            if resetChoice == "1":
                input("\"Good. I will wake you up now, and everything will be back the way it was before...\"")
                input("You wake up and use the Dream Shard. A cloud covers you as you begin to see a vision of the timeline you're being transfered to...")
                input("The memory of your wife that you conjured up tricked you.\n"
                      "The Dream Shard transfers you to the morning you woke up to find your family dead in the burning house...")
                input("You scream in agony as you feel the transfer process slowly removing your memories of the dreams "
                      "and everything that occurred during the past five years ago being removed.\n"
                      "You are doomed to repeat the process of running away and experiencing these dreams again every five years...\n")
                input("Unless you change your ways the next time the dreams start occurring again...Will you?")
                gameEndEvil()  
            else:
                print("I'm not letting you wake up from this dream until you agree to it.\n")
                continue
    
    
def gameEndEvil():
    globalScore
    print("Congratulations on completing the game. You have achieved the evil ending of the game with a final score of "+score+"."
          "This game has 3 endings, all of which are drastically different and reveal different information about the story."
          "If you want to know how to achieve the other two, just ask me!")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)
    
def gameEnd():
    print("Congratulations on completing the game! This game has 4 possible endings, all of which are drastically different. "
          "If you want to know how to achieve the other two, just ask me!")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)
    
def main():
    showIntro()
    gameLoop()

main()
