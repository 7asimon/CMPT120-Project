# GREYWALKER
# Author: Abel Simon
# Date : November 28, 2017

score = 0
moves = 0
userAction = None

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
           "Dinner Table", False, False, "Ripped Garments"),
    Locale("cliff", "You arrive at the edge of a cliff with a dark abyss below it. There is nothing of interest here.", "Cliff",
           False, False, "Ornament"),
    Locale("house interior", "Inside the house, you find that the walls are covered with black and white pictures of your family"
               " that were taken before they died mysteriously years ago."
               " Eerily enough, you are missing from all the pictures as if you were cropped out of them.", "House Interior",
           False, False, "Necklace"),
    Locale("strange wall", "You come across a wall with seemingly meaningless inscribings on them."
               " You cannot make out what the strange drawings say. You hear people shuffling around on the other side.", "Strange Wall",
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
    print("GREYWALKER")
    print('')
    # store input name in a variable and return it to them
    playerName = input("Your name is...you cannot seem to recall it. Try to remember your name: ")
    print("Ah, yes, " + playerName + ", that was it. You are a sleepwalker"
          " and an insomniac who is attempting to master lucid dreaming in order to discover forgotten secrets about your past."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input("You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          " You must collect all important artifacts and visit every location before the final encounter of the game."
          " Once the game begins, type help to view the list of usable commands.")
    print('')
    
# store all 12 locations in a list to be used later
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
               " You cannot make out what the strange drawings say. You hear people shuffling around on the other side.",
               "Walking down the path, you witness many villagers screaming in agony and running down the street."
               " There appears to be an endless number of them",
               "At the end of the path of agony, people gather around a small shrine",
               "As you approach the wall, it crumbles, reavealing a balcony",
               "Using a ladder, you climb down from the balcony into the black water."
               " Proceeding without visiting every location and without the dream shard is ill-advised",
               "As you wade out of the water onto the land, you realize that the water surrounds you."
               " You must find a way out of this dream."]

# all these lists of booleans are used in vital functions
hasBeenThere = [False, False, False, False, False, False, False, False, False, False, False, False]
hasBeenSearched = [False, False, False, False, False, False, False, False, False, False, False, False]
locationCheck = [False, False, False, False, False, False, False, False, False, False, False, False]
items = [None, None, "Map", "Ripped Garments", "Ornament", "Necklace", None, None, "Strange Gem", "Dream Shard", None, None]
inventory = []

# short name for each location, later displayed if player has already been to that location
locNames = ["The Meadow", "Burning Village", "Grey Room",
           "Dinner Table", "Cliff", "House Interior", 
           "Strange Wall", "Path Of Agony", "Shrine" , "Balcony",
            "Water", "Land"]

# matrix key
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
water = 10
land = 11
# locInfo stores the number of the location you're in, making creating additional functions far easier.
# locInfo is repeatedly updated throughout the functions in this program
locInfo = 0
# matrix for the game world
         # N     S     E      W
world = [[2,  None,     1,  None] # meadow
        ,[3,  None,     4,     2] # village
        ,[5,     0,     3,  None] # grey room
        ,[6,     1,     4,     2] # dinner table
        ,[7,  None,  None,     3] # cliff
        ,[None,  2,     6,  None] # house interior
        ,[9,     3,     7,     5] # strange wall
        ,[None,  4,     8,     6] # path of agony
        ,[None,  None,   None, 7] # shrine
        ,[10,  6,  None,  None] # balcony
        ,[11,  9,  None,  None] # water
        ,[None,10, None,  None] # land
        ]
# main game loop
def gameLoop():
    global locInfo
    global hasBeenSearched
    global world
    while True:
        showLocation(locInfo)
        userAction = input("Enter Command: ").lower()
        # only address the whereTo function if the user decides to move somewhere 
        if userAction == "north" or userAction == "east" or userAction == "south" or userAction == "west":
            whereTo(locInfo, userAction)
        if userAction == "score":
            print(score)
        if userAction == "moves":
            print("You have", 16 - moves ,"moves left")
        if userAction == "look":
            print(Locales[locInfo].locDescrip)
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
        if userAction == "take map":
            if locInfo == 2 and "Map" not in inventory:
                retrieve(locInfo)
                items[2] = None
            else:
                print("There is no map here")
        # the following set of if statements lets a user take an item, but they must state it by name.
        # once the item is taken, the element representing that item is set to None
        # this prevents the user from duplicating items by taking it multiple times
        if userAction[0:8] == "take rip":
            if locInfo == 3 and "Ripped Garments" not in inventory:
                retrieve(locInfo)
                items[3] = None
            else:
                print("There are no Ripped Garments here")
        if userAction == "take ornament":
            if locInfo == 4 and "Ornament" not in inventory:
                retrieve(locInfo)
                items[4] = None
            else:
                print("There is no Ornament here")
        if userAction == "take necklace":
            if locInfo == 5 and "Necklace" not in inventory:
                retrieve(locInfo)
                items[5] = None
            else:
                print("There is no Necklace here")
        if userAction == "take strange gem":
            if locInfo == 8 and "Strange Gem" not in inventory:
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
            if "Map" in inventory:
                print(
                       "                               Land                                  \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       "                               Water                                 \n"
                       "                                ||                                   \n"
                       "                              Balcony                                \n"
                       "                                ||                                   \n"
                       "                                ||                                   \n"
                       " House Interior ========= Strange Wall ========== Path of Agony ===== Shrine \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       "     ||                         ||                     ||       \n"
                       " Grey Room ============== Dinner Table ============= Cliff      \n"
                       "     ||                         ||                              \n"                  
                       "     ||                         ||                              \n"
                       "     ||                         ||                              \n"
                       "     ||                         ||                              \n"
                       "   Meadow =================== Village                           \n"
                      )
            else:
                print("You have not yet found the map")
                
            

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
    # defeat if you fail to win within the 20 given moves
    if moves == 20:
        print("You run out of time and the dream has ended")
        input()
        quit()
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
    if items[locInfo] != None:
        print("While searching the area, you find a", items[locInfo], "for the taking.")
        # this allows them to take the item at the location with the <take> command
        hasBeenSearched[s] = True
    else:
        print("You find nothing worth taking in this area.")

def retrieve(locInfo):
    # only allow player to take an item if they have searched and there is an item in the location
    if hasBeenSearched[locInfo] is True:
        # add new item to inventory list and inform player of successful take
        inventory.append(items[locInfo])
        print("You have picked up a", items[locInfo]+".")
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
        else:
            print("You do not have a map")
            print('')
    if itemChoice == "ripped garments":
        if "Ripped Garments" in inventory:
            inventory.remove("Ripped Garments")
            items[3] = "Ripped Garments"
        else:
            print("You do not have Ripped Garments")
            print('')
    if itemChoice == "ornament":
        if "Ornament" in inventory:
            inventory.remove("Ornament")
            items[4] = "Ornament"
        else:
            print("You do not have the Ornament")
            print('')
    if itemChoice == "necklace":
        if "Necklace" in inventory:
            inventory.remove("Necklace")
            items[5] = "Necklace"
        else:
            print("You do not have the Necklace")
            print('')
    if itemChoice == "strange gem" or itemChoice == "gem":
        if "Strange Gem" in inventory:
            inventory.remove("Strange Gem")
            items[8] = "Strange Gem"
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

def gameEnd():
    print("You use the Dream Shard and escape the dream." 
" All will be solved in the final game version...")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)
    
def main():
    showIntro()
    gameLoop()

main()
