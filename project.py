# FIVE YEARS AFLAME
# Author: [Temporarily Redacted]
# Date : November 28, 2017

score = 0
moves = 0
userAction = None
specialQuestionAsked = False
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
print("Public Test Version. Please tell me if you find any bugs or exploits.")
print('')
playerName = input("Your name is...you cannot seem to recall it. \nTry to remember your name: ").capitalize()
print(playerName + "...Yes, that was it.")
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
    Locale("shrine", "At the end of the path of agony, people gather around a small shrine", "Shrine", False, False, "Guardian Gem"),
    Locale("balcony", "As you approach the wall, it crumbles, reavealing a balcony", "Balcony", False, False, "Dream Shard"),
    Locale("water", "Using a ladder, you climb down from the balcony into the black water. Proceeding without visiting every location and without the dream shard is ill advised", "Water", False, False, None),
    Locale("land", "As you wade out of the water onto the land, you realize that the water surrounds you."
               " You must find a way out of this dream.", "Land", False, False, None)]
    

    
#after player gives their name, intro is the next thing to trigger
def showIntro():
    global playerName
    global score
    input("STORY:\n \n"
          "You are a sleepwalker with the power to bring items you find in your dreams into the real world. "
          "5 years ago, you woke up lying down on the front lawn of your home feeling almost paralyzed. "
          "Your entire house was engulfed in flames and your fiance, son, and daughter all perished in the fire. "
          "You immediately fled the country out of fear that you would be blamed. "
          "To this day, you still do not have a clue why it occurred or why whoever did it left you alive. "
          "You suspect that someone planned to ruin your life by killing everyone you loved and framing you. \n \n"
          "Recently, you have been having very detailed lucid dreams containing strange details about your past and the day of the fire. "
          "You travel this dream world in hopes that you will find something that shows you who is responsible for the massacre of your family...\n \n"
          "Press ENTER to continue...")
    print('')
    print("In this game, the decisions you make "
          "affect the events that occur within the game and the ending to your story. \n"
          "Choose wisely...")
    print('')
    while True:
        #loop until player asks for help or asks to start game
        startOrHelp = input("Type <help> for a tutorial. \n"
                            "Type <start> if you have played before and wish to begin immediately: ")
        if startOrHelp == "start":
            print("\n\n\n\n\n")
            break
        elif startOrHelp == "help":
            print('')
            print("Type <north>, <south>, <east>, and <west> to navigate. \n"
                  "Type <awaken> when in a dream state to wake up and move around in your home. \n"
                  "Type <sleep> when in the real world to return to your dream. \n"
                  "ALWAYS Type <search> to look for an item in your location. \n"
                  "Type <take item name> to take an item once you find it. \n"
                  "Example: type <take map> to pick up the map once found. \n"
                  "Type <score> to view your current score. \n"
                  "Type <moves> to see how many moves you have taken. \n"
                  "Type <look> to view the long description of your location (automatically displayed at first visit).\n"
                  "Type <map> once you find it to view it.\n"
                  "Type <inspect item name> to be told how to use an item.\n"
                  "Type <inv> to view your inventory. \n"
                  "Type <speak> to talk to any people present at your current location. \n"
                  "In sections that give you multiple numbered choices, type the # of the choice you want.\n"
                  "Type <help> at any point to view these commands again. \n"
                  "All commands should be typed without < or >. \n")
            print("Simply interacting with the world adds to your score, regardless of whether your choice is good or evil.")
            input("Press Enter to Continue: ")
            print("\n\n\n\n\n")
            break
        else:
            print("You entered an invalid command.")
            
    
    
# store all 16 locations in a list
locDescrips = ["You find yourself in a vaguely familiar meadow filled with wilted daisies. "
               "Looking forward, you can see a village. In the center lies your home, which is engulfed in flames. ",
               "You arrive in a grey room with random burned objects scattered about."
               " As you walk into the room, the color fades from your skin and you notice everything you see is in black and white.",
               "In front of your home, a message painted across the sidewalk in blood red reads:\"WHY?\"",
               "You arrive at a dinner table that you recognize from your old home.",
               "You arrive at the edge of a cliff, beyond which a dark abyss lies.",
               "Inside the house, you find that the walls are covered with black and white pictures of your family"
               " that were taken before they died mysteriously years ago."
               " Eerily enough, you are missing from all the pictures as if you were cropped out of them.",
               " You come across a large room that appears to be a lair for a creature of some sort."
               " A broken section of the wall reveals a balcony straight ahead. ",
               "Walking down the path, you witness many villagers screaming in agony and running down the street."
               " You are curious as to what could have possibly driven them insane.",
               "A small family sits around the shrine. "
               "On the shrine lies a glowing dagger that seems to be the subject of their worship. It radiates with evil energy. ",
               "With the guardian gone, you exit his lair through the broken section of the wall",
               "Using a ladder, you climb down from the balcony into the black water. "
               "The water seems to be filled with a destructive energy. "
               "In front of you lies a pair of opaque stairs leading to an empty throne.",
               "You climb up the stairs till you reach the platform containing the unoccupied throne.",
               "You wake up from your dream alone in your room. "
               "Try the <map> command if you found the map in your dream. "
               "Type <sleep> to return to your dream.",
               "You are in the hallway. From here, you can enter your kitchen or your living room.",
               "You left the stove in your kitchen on by accident earlier. The room reaks of carbon monoxide.",
               "The movie \"Inception\" plays on your living room television."]

# track whether locations have been visited, searched, and the place items at their corresponding locations
hasBeenThere = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
hasBeenSearched = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
locationCheck = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
items = [None, "Ornament", "Map", "Exotic Garments", None, "Family Photo", None, "Guardian Gem", "Shrine Key",
         "Dream Shard", None, None, "Blanket", None, "Food", "Expensive Necklace"]
inventory = []

# short name for each location, later displayed if player has already been to that location
locNames = ["The Meadow", "Grey Room", "Home Town",
           "Dinner Table", "Cliff", "House Interior", 
           "Guardian's Lair", "Path Of Agony", "Shrine" , "Balcony",
            "Black Water", "Throne of Dreams", "Your Room", "The Hallway",
            "The Living Room", "The Kitchen"]

# matrix key
meadow = 0
greyRoom = 1
homeTown = 2
dinnerTable = 3
cliff = 4
houseInterior = 5
guardianLair = 6
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
        ,[3,  None,  None,     0] # greyRoom
        ,[5,     0,     3,  None] # homeTown
        ,[6,     1,     4,     2] # dinnerTable
        ,[7,  None,  None,     3] # cliff
        ,[None,  2,     6,  None] # houseInterior
        ,[9,     3,     7,     5] # guardianLair
        ,[None,  4,     8,     6] # pathOfAgony
        ,[None,  None,   None, 7] # shrine
        ,[None,   6,   10,  None] # balcony
        ,[11,  None,   None,   9] # blackWater
        ,[None,  10, None,  None] # throneOfDreams
        ,[13,  None, None,  None] # yourRoom
        ,[None,   12,   14,   15] # hallway
        ,[None, None, None,   13] # livingRoom
        ,[None, None,   13, None] # kitchen
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
        #display location info every time loop begins
        showLocation(locInfo)
        userAction = input("Enter Command: ").lower()
        #if guardian has not been dealt with, prevent them from moving past the guardian lair
        if userAction == "north" and locInfo == 6 and guardianState == 0:
            guardianEncounter()
        #if player gets locked out of shrine, do not allow them to re-enter without the key
        elif userAction == "east" and shrineState == 3 and locInfo == 7 and "Shrine Key" not in inventory:
            print("The shrine is locked and you cannot enter")
        elif userAction == "east" and shrineState == 3 and locInfo == 7 and "Shrine Key" in inventory:
            print("The shrine is locked. Maybe if you <use shrine key> you will be able to enter.")
        elif userAction == "north" or userAction == "east" or userAction == "south" or userAction == "west":
            whereTo(locInfo, userAction)
        #if user chooses to speak, a different function is addressed depending on what NPCs are present for them to speak to
        #this also depends on the state of the NPC they are trying to speak to (alive, dead, mad, etc)
        if userAction[0:5] == "speak":
            if locInfo == 3:
                speechCheckOne()
            elif locInfo == 7:
                print("You try speaking to the encrazed people, but they flail their arms and are completely incoherent.")
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
        #allow player to transfer to the real world if they are sleeping
        elif userAction == "awaken":
            if locInfo <= 11:
                print("You awaken from your slumber.")
                print('')
                locInfo = 12
            elif locInfo >= 12:
                print("You are already awake.")
        #allow player to return to the dream world if they are awake
        elif userAction == "sleep":
            if locInfo >= 12:
                print("You go back to your bed and return to the dream world.")
                print('')
                locInfo = 0
            elif locInfo <= 11:
                print("You are already dreaming.")
        elif userAction == "score":
            print(score)
        #in this version of the game, you cannot run out of moves
        #i want players to have freedom to explore for as long as they want
        #(however, score is subtracted from your # of moves at end)
        elif userAction == "moves":
            print("You have made", moves, "moves")
        #new description for if player destroys the shrine and looks around in it
        if userAction == "look" and locInfo == 8 and shrineState == 4:
            print("You have destroyed everything in the shrine and slaughtered the helpless family.")
        if userAction == "look" and locInfo == 8 and shrineState == 12:
            print("You have destroyed everything in the shrine and slaughtered the helpless family.")
        #give long location description on request
        elif userAction == "look":
            print(locDescrips[locInfo])
        #player cannot take without listing item name
        elif userAction == "take":
            print("You must type take followed by the item name to take an item")
        #give commands on request
        elif userAction == "help":
            print("Type <north>, <south>, <east>, and <west> to navigate. \n"
                  "Type <awaken> when in a dream state to wake up and move around in your home. \n"
                  "Type <sleep> when in the real world to return to your dream. \n"
                  "ALWAYS Type <search> to look for an item in your location. \n"
                  "Type <take item name> to take an item once you find it. \n"
                  "Example: type <take map> to pick up the map once found. \n"
                  "Type <score> to view your current score. \n"
                  "Type <moves> to see how many moves you have taken. \n"
                  "Type <look> to view the long description of your location (automatically displayed at first visit).\n"
                  "Type <map> once you find it to view it.\n"
                  "Type <inspect item name> to be told how to use an item.\n"
                  "Type <inv> to view your inventory. \n"
                  "Type <speak> to talk to any people present at your current location. \n"
                  "In sections that give you multiple numbered choices, type the # of the choice you want.\n"
                  "Type <help> at any point to view these commands again. \n"
                  "All commands should be typed without < or >. \n")
        #begin set of inspect commands
        #typing inspect followed by item name gives information about an items purpose
        if userAction == "inspect food":
            if "Food" in inventory:
                print("Eating this item will provide a slight score boost. However, it is also needed for a hidden quest...")
            else:
                print("You do not have Food")
        elif userAction == "inspect ornament":
            if "Ornament" in inventory:
                print("This item is part of the guardian quest.")
            else:
                print("You do not have the Ornament.")
        elif userAction == "inspect map":
            if "Map" in inventory:
                print("Type <map> to view the map.")
            else:
                print("You do not have the map.")
        elif userAction == "inspect garments" or userAction == "inspect exotic garments":
            if "Exotic Garments" in inventory:
                print("These are useful in convincing certain people to do your bidding.\n"
                      "Type <use garments> to equip them.")
            else:
                print("You do not have Exotic Garments")
        elif userAction == "inspect photo" or userAction == "inspect family photo":
            if "Family Photo" in inventory:
                print("This item unlocks special dialogue when it is in your inventory.")
            else:
                print("You do not have the Family Photo")
        elif userAction == "inspect guardian gem" or userAction == "inspect gem":
            if "Guardian Gem" in inventory:
                print("This item is part of the guardian quest.")
            else:
                print("You do not have the Guardian Gem in your inventory")
        elif userAction == "inspect shrine key" or userAction == "inspect key":
            if "Shrine Key" in inventory:
                print("If you get locked out of the shrine, <use key> when standing outside it.")
            else:
                print("You do not have the Shrine Key.")
        elif userAction == "inspect dagger" or userAction == "inspect cursed dagger":
            if "Cursed Dagger" in inventory:
                print("This dagger radiates with an evil energy. "
                      "There are several chances where you will be given the choice to use it, "
                      "but there is no going back once you do.")
            else:
                print("You do not have the Cursed Dagger")
        elif userAction == "inspect rare coin" or userAction == "inspect coin":
            if "Rare Coin" in inventory:
                print("This item is part of the guardian quest.")
            else:
                print("You do not have the Rare Coin.")
        elif userAction == "inspect dream shard" or userAction == "inspect shard":
            if "Dream Shard" in inventory:
                print("This item will <summon> the owner of the Throne of Dreams if you are standing in front of it.")
            else:
                print("You do not have the Dream Shard")
        elif userAction == "inspect blanket":
            if "Blanket" in inventory:
                print("This is a quest item.")
            else:
                print("You do not have the blanket.")
        elif userAction == "inspect necklace" or userAction == "inspect expensive necklace":
            if "Expensive Necklace" in inventory:
                print("This is useful in convincing certain people to do your bidding.\n"
                      "Type <use necklace> to equip it.")
            else:
                print("You do not have the Expensive Necklace")
        elif userAction == "inspect ring" or userAction == "inspect wedding ring":
            if "Wedding Ring" in inventory:
                print("The ring you used to propose to your fiance.\n"
                      "<use ring> at the meadow.")
            else:
                print("You do not have the Wedding Ring")
        #end set of inspect commands
        elif userAction == "quit":
            quit()
        #refer to playerSearch function if player searches an area
        elif userAction == "search":
            playerSearch(locInfo)
        elif userAction == "use ring":
            if "Wedding Ring" in inventory and locInfo == 0 and familyHonored == 1:
                ringSequence()
            elif "Wedding Ring" in inventory and locInfo != 1:
                print("You cannot use the ring here")
            elif "Wedding Ring" not in inventory and familyHonored != 1:
                print("You have already used your ring")
            elif "Wedding Ring" not in inventory:
                print("You do not have the ring")
        elif userAction == "use necklace" or userAction == "use expensive necklace":
            if "Expensive Necklace" in inventory and necklace == 0:
                print("You have put on the expensive necklace")
                score = score + 5
                necklace = 1
            elif "Expensive Necklace" in inventory and necklace ==1:
                print("You are already wearing the expensive necklace")
            else:
                print("You do not have the expensive necklace")
        elif userAction == "use exotic garments" or userAction == "use garments":
            if "Exotic Garments" in inventory and garments == 0:
                print("You have put on the exotic garments")
                garments = 1
                score = score + 5
                print("This item can be useful in convincing certain people. "
                      "Type <use garments> to put it on")
            elif "Exotic Garments" in inventory and garments == 1:
                print("You are already wearing the exotic garments")
            else:
                print("You do not have the exotic garments")
        #begin set of take commands
        #player must type take followed by item name to take an item
        #item is removed from location when taken to prevent duplicating items
        elif userAction == "take map":
            if locInfo == 2 and "Map" not in inventory:
                retrieve(locInfo)
                items[2] = None
            else:
                print("There is no map here")
        elif userAction[0:8] == "take exo" or userAction == "take garments":
            if locInfo == 3 and "Exotic Garments" not in inventory:
                retrieve(locInfo)
                items[3] = None
            else:
                print("There are no Exotic Garments here")
        elif userAction == "take ornament":
            if locInfo == 1 and "Ornament" not in inventory:
                retrieve(locInfo)
                items[1] = None
            else:
                print("There is no Ornament here")
        elif userAction == "take family photo" or userAction == "take photo":
            if locInfo == 5 and "Family Photo" not in inventory:
                score = score + 5
                retrieve(locInfo)
                familyPhoto = True
                items[5] = None
            else:
                print("The Family Photo is not here")
        elif userAction == "take guardian gem" or userAction == "take gem":
            if locInfo == 7 and "Guardian Gem" not in inventory:
                retrieve(locInfo)
                items[7] = None
            else:
                print("There is no Guardian Gem here")
        elif userAction == "take dream shard" or userAction == "take shard":
            if locInfo == 9 and "Dream Shard" not in inventory:
                retrieve(locInfo)
                items[9] = None
            else:
                print("There is no Dream Shard here")
        elif userAction == "take shrine key" or userAction == "take key" or userAction == "steal key" or userAction == "steal shrine key":
            if locInfo == 8 and "Shrine Key" not in inventory:
                score = score + 5
                morality = morality - 1
                retrieve(locInfo)
                print("Use this to get back into the shrine if you get locked out")
                items[8] = None
            else:
                print("There is no Shrine Key here")
        elif userAction == "take blanket":
            if locInfo == 12 and "Blanket" not in inventory:
                retrieve(locInfo)
                items[12] = None
            else:
                print("There is no Blanket here")
        elif userAction == "take necklace" or userAction == "take expensive necklace":
            if locInfo == 15 and "Expensive Necklace" not in inventory:
                retrieve(locInfo)
                items[15] = None
                print("This item can be useful in convincing certain people. "
                      "Type <use necklace> to put it on")
            else:
                print("The expensive Necklace is not here")
        elif userAction == "take food":
            if locInfo == 14 and "Food" not in inventory:
                retrieve(locInfo)
                items[14] = None
                print("This item can be used for a quick score boost, but it has another hidden purpose...")
            else:
                print("There is no food here")
        elif userAction == "take dagger" or userAction == "take cursed dagger":
            if locInfo == 8 and "Cursed Dagger" not in inventory:
                print("You must <speak> to the woman to be given this option")  
        elif userAction == "use shrine key" or userAction == "use key":
            if locInfo == 7 and "Shrine Key" in inventory and shrineOpen == False:
                print("You use the key to break back into the shrine")
                score = score + 10
                shrineBreakIn()
            elif shrineOpen == True:
                print("The shrine is not locked, you can enter any time you wish.")
            else:
                print("You are not in front of the shrine or you do not have the Shrine Key")
        elif userAction == "use food" or userAction == "eat food":
            if "Food" in inventory and locInfo == 8:
                print("\"How could you eat that in front of us, you monster?!\"")
                morality = morality - 2
                score = score + 10
                shrineState = 11
                inventory.remove("Food")
            elif "Food" in inventory:
                print("You eat the food, increasing your score")
                score = score + 5
                inventory.remove("Food")
            else:
                print("You do not have food in your inventory")
        elif userAction == "drop":
            dropItem(locInfo)
        elif userAction[0:3] == "inv":
            print(inventory)
        elif userAction == "summon":
            if locInfo == 11 and "Dream Shard" in inventory:
                finalChoice = input("Are you sure you wish to summon? "
                                    "Once you do this, the final sequence of the game begins. There will be no turning back. "
                                    "Remember, there is a second world accessible with <awaken> and exitable with <sleep>\n"
                                    "Summon?(yes/no): ")
                if finalChoice[0:1] == "y":
                    finalEncounter()
            elif "Dream Shard" not in inventory:
                print("You lack the item required to summon. Judging by the aesthetic of the throne, "
                      "whatever item you need to <summon> has something to do with dreams.")
            elif "Dream Shard" in inventory:
                print("You cannot summon from here. Try going toward the throne in the distance")
        elif userAction == "stuck":
            print("in progress")
        elif userAction == "map" or userAction == "use map":
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
                      "                      "+playerName+"'s Room \n"
                      )
            if "Map" not in inventory:
                print("You have not yet found the map")
        if locInfo == 4 and coldManState == 0:
            print("A man lies near the edge of the cliff. "
                  "Perhaps you should try to <speak> to him?")
        elif locInfo == 4 and coldManState == 3:
            print("The air is filled with a burning scent from the man's death.")
        elif locInfo == 4 and coldManState == 1:
            print("The man at this location is content now that you have given him a blanket.")
        elif locInfo == 4 and coldManState == 2:
            print("The man at this location is angry with you for stealing his coin.")
        elif locInfo == 3:
            print("A mirror image of yourself sits at table in this location. "
                  "Perhaps you should try to <speak> to him?")
        elif locInfo == 8 and shrineState == 0:
            print("The mother of the family  at this location looks very distraught.\nPerhaps you should try to <speak> to her?")
        elif locInfo == 8 and shrineState == 1:
            print("The mother of the family at this location pleased with you.\n<speak> to her for another quest.")
        elif locInfo == 8 and shrineState == 2:
            print("The mother of the family at this location is angry with you.\nPerhaps you can <speak> to her if you want to fix things?")
        elif locInfo == 8 and shrineState == 11:
            print("The mother of the family at this location is angry with you for eating food in front of her instead of helping.")
        elif locInfo == 11:
            print("The throne at this location is unoccupied.\n"
                  "Perhaps you should try to <summon> the owner.")
        
                              
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
    global shrineState
    # if they have not searched yet and there is an item present at current location, tell them what item is present
    if items[locInfo] == "Family Photo" and hasBeenThere[3] == True:
        print("The Family Photo you see on the stand can be taken. \n"
              "Perhaps you should bring it back to the mirror image of yourself at the table...")
        hasBeenSearched[s] = True
    elif items[locInfo] == "Family Photo":
        print("The <Family Photo> you see on the stand can be taken.")
        hasBeenSearched[s] = True
    elif items[locInfo] == "Food" and hasBeenThere[8] == True and shrineState == 0:
        print("Opening your fridge, you find <food>. The family at the shrine could really use this.")
    elif items[locInfo] == "Food":
        print("Opening your fridge, you find <food>.")
    elif items[locInfo] == "Exotic Garments":
        print("A pair of <Exotic Garments> are laid out on the dinner table for the taking.")
    elif items[locInfo] == "Expensive Necklace":
        print("You spot a <necklace> that you left here by accident")
    elif items[locInfo] == "Ornament":
        print("An <ornament> lies on the table in front of you.")
    elif items[locInfo] == "Map":
        print("A <map> of your dream world is pinned to your mailbox")
    elif items[locInfo] == "Shrine Key":
        print("You notice a shrine key hanging from the man's pocket. "
              "You could steal it without him noticing...")
    elif items[locInfo] != None:
        print("While searching the area, you find", items[locInfo], "for the taking.")
        # this allows them to take the item at the location with the <take> command
        hasBeenSearched[s] = True
    else:
        print("You find nothing worth taking in this area.")

def retrieve(locInfo):
    global score
    # only allow player to take an item if they have searched and there is an item in the location
    if items[locInfo] == "Shrine Key":
        print("You successfully steal the Shrine Key from the man")
        inventory.append(items[locInfo])
        score = score + 5
    elif items[locInfo] != None:
        # add new item to inventory list and inform player of successful take
        inventory.append(items[locInfo])
        print("You have picked up", items[locInfo]+".")
        score = score + 5
    else:
        print("You find nothing worth taking in this area. Try <search> if you have not already")

def dropItem(locInfo):
    global daggerState
    # ask player what item they want to drop and put down the item they choose
    # the player can still choose to pick the item up again
    itemChoice = input("What item do you want to drop? ")
    if itemChoice == "map":
        print("You cannot drop essential items!")
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
        print("You cannot drop essential quest items!")
    if itemChoice == "guardian gem" or itemChoice == "gem":
        if "Guardian Gem" in inventory:
            inventory.remove("Guardian Gem")
            items[7] = "Guardian Gem"
            score = score - 5
        else:
            print("You do not have the Guardian Gem")
            print('')
    if itemChoice == "dream shard":
        print("You cannot drop essential items!")
    if itemChoice == "cursed dagger" or itemChoice == "dagger":
        if "Cursed Dagger" in inventory and locInfo == 10:
            print("The dagger shakes violently and then explodes the moment it makes contact with the water")
            inventory.remove("Cursed Dagger")
            morality = morality + 3
            score = score + 15
            daggerState = 1
        elif "Cursed Dagger" in inventory:
            print("You cannot drop the Cursed Dagger at this location")
            print('')
        else:
            print("You do not have the Cursed Dagger")
    if itemChoice == "food":
        if "Food" in inventory:
            inventory.remove("Food")
            items[15] = "Food"
            score = score - 5
        else:
            print("You do not have Food")
            print('')

def speechCheckOne():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global specialQuestionAsked
    global morality
    global familyHonored
    if locInfo == 3 and morality <= -70:
        print("Stay away from me, you vile man! I refuse to speak to you!")
    elif locInfo == 3 and "Family Photo" in inventory:
                if morality >= -4 and morality <= 4:
                    print("\"Well, hello there.\" He greets you.")
                elif morality >= 5:
                    print("\"I haven't seen such a friendly face in a while! Greetings!\" He says to you, happily")
                elif morality <= -5 and morality >= -9:
                    print("\"You're scum. But, I'm sure you know that, right?\"")
                elif morality <= -10:
                    print("\"I greatly disprove of your evil actions. I beg of you, change your ways!\"")    
                consciousQuestion = input("What would you like to say (type the # of the response you want)?\n"
                                       "1 - Who are you?\n"
                                       "2 - How can I find out who burned my home and killed my family?\n"
                                       "3 - Why does this dream occur every time I sleep?\n"
                                       "4 - How am I doing?\n"
                                       "5 - (show him the family photo) Why am I missing from this family portrait?\n "
                                          "I was certainly in the photo when it was taken\n"
                                       "6 - (End Conversation)\n")
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
                elif consciousQuestion == "5":
                    questionThree = input("\"Your subconscious has removed you from the picture out of guilt. \n "
                                          "Now, whether that is just guilt for running away, survivor guilt, "
                                          "or something much more serious, I do not wish to answer.\"\n"
                                          "1 - Why must everything be so cryptic? Why cant you just tell me, dammit! \n"
                                          "2 - (End Conversation)\n")
                    if specialQuestionAsked == False:
                        score = score + 15
                        specialQuestionAsked = True
                    if questionThree == "1":
                        print("\"That's your fault, you know. I'm only doing what you would do in the same situation.\n"
                              "Subconsciously, you love messing with people and playing games.\"\n")
                        if familyHonored == 0:
                            print("In any case, I'm glad you're demonstrating curiosity.\n"
                                  "Here, take the ring you gave your fiance. Go to the Meadow and <use ring>. I'm sure you'll see why.\"\n(He gives you a Wedding Ring)\n")
                            inventory.append("Wedding Ring")
                            familyHonored = 1
                elif consciousQuestion == "4":
                    if morality >= -4 and morality <= 2 and score >= 60:
                        print("\"It is hard for me to pass judgement on you...\n"
                              "You are either staying out of things or are avoiding doing anything significantly good or evil.\"")
                    elif morality >= -4 and morality <= 2:
                        print("\"You haven't done anything notable yet. You've yet to create your legacy here.\"")
                    elif morality >= 3:
                        print("\"The world needs more people like you. You deserve to have a lot of respect for yourself.\"")
                    elif morality <= -5 and morality >= -4:
                        print("\"You are evil and should be condemned endlessly for your actions.\"")
                    elif morality <= -15:
                        print("\"You are irredeemably evil and your sadism knows no bounds. I hesitate to even call you human at this point.\"") 
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
                                       "4 - How am I doing?\n"
                                       "5 - (End Conversation)\n")      
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
                elif consciousQuestion == "4":
                    if morality >= -4 and morality <= 2 and score >= 60:
                        print("\"It is hard for me to pass judgement on you...\n"
                              "You are either staying out of things or are avoiding being significantly good or evil.\"")
                    elif morality >= -4 and morality <= 2:
                        print("\"You haven't done anything notable yet. You've yet to create your legacy here.\"")
                    elif morality >= 3:
                        print("\"The world needs more people like you. You deserve to have a lot of respect for yourself.\"")
                    elif morality <= -5 and morality >= -14:
                        print("\"You are evil and should be condemned endlessly for your actions.\"")
                    elif morality <= -15:
                        print("\"You are irredeemably evil and your sadism knows no bounds. I hesitate to even call you human at this point.\"")  
                

def ringSequence():
    global familyHonored
    global morality
    global score
    if familyHonored == 1:
        print("You remember why this ring and the meadow are special.\n"
              "Not only was it your marriage ring, but this is where you proposed to them as well. "
              "They were so happy that years later during a cancer scare, "
              "they told you that if they didn't make it, they wanted to be buried in this same meadow where you proposed.")
        ringChoice = input("1 - (Bury the ring)\n"
                           "2 - (Destroy the ring)\n"
                           "3 - (Do nothing)\n")
        if ringChoice == "1":
            print("You honor your fiance's legacy by burying the ring in the meadow")
            morality = morality + 2
            inventory.remove("Wedding Ring")
            score = score + 10
            familyHonored = 2
        if ringChoice == "2":
            print("You spite your fiance and their death by destroying the ring")
            inventory.remove("Wedding Ring")
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
    if locInfo == 4 and coldManState == 2:
        attackChoice = input("\"I don't want your help, go away!!! You've already taken the one thing I had. What more do you want from me?\"\n"
                             "1 - (Kill him with the cursed dagger) \n"
                             "2 - (Leave)\n")
        if attackChoice == "1":
            if "Cursed Dagger" in inventory:
                print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                      "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess.")
                coldManState = 3
                morality = morality - 15
                score = score + 15
            else:
                print("You do not have the item required to perform that action")
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
                morality = morality + 3
                score = score + 15
            elif "Blanket" not in inventory:
                print("You do not have the item required to perform this action")
        if helpMan == "2":
            print("\"No! Don't take it from me!\" The man says. "
                  "He tries to stop you, but he is too weak to stop you from ripping it from his clutches")
            inventory.append("Rare Coin")
            coldManState = 2
            score = score + 10
            morality = morality - 3
        if helpMan == "3":
            if "Cursed Dagger" not in inventory:
                print("You lack the required item to perform this action")
            elif "Cursed Dagger" in inventory:
                print("The man screams and writhes in extreme pain the moment the dagger makes contact with his heart. "
                  "A blue energy courses throughout the man as he begins to disintegrate from the cursed energy the dagger possess.")
                coldManState = 3
                morality = morality - 15
                score = score + 15
                
        
        
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
    if "Ornament" in inventory and "Guardian Gem" in inventory and "Rare Coin" in inventory:
        guardianRequest = 1
    input("As you try to continue, a guardian suddenly appears and blocks your way, preventing you from going forward. "
          "You must find some way to deal with him in order to continue. "
          "There are several hidden ways to do this, doing his bidding is not the only way. Press ENTER to hear his words... \n")
    if score < 60 and guardianState == 0:
          print("\"Bah! You've hardly accomplished anything yet. Come back when you've done more!\"")
          locInfo = 6
    elif guardianState == 0:
        print("\"Seems like you've done quite a bit around here. So, here's the deal. "
              "I'll let you pass if you bring me my ornament and my gem. "
              "I also spotted a rare coin that I want you to steal for me.\"")
        guardianChoice = input("What would you like to do (type the # of the action you want)?\n"
                                "1 - (Give him the items)\n"
                                "2 - (Kill the guardian)\n"
                                "3 - (Try to convince him to let you pass)\n"
                                "4 - What will you do with these items?\n"
                                "5 - I will come back later\n")
        if guardianChoice == "1":
            if guardianRequest == 1:
                print("\"Ah, thank you. You have done me a great service. You are free to pass.\"\n")
                print("The guardian disappears, allowing you to move forward freely")
                inventory.remove("Guardian Gem")
                inventory.remove("Rare Coin")
                inventory.remove("Ornament")
                guardianState = 2
                morality = morality - 5
                locInfo = 6
                score = score + 10
            else:
                print("\"Is this some kind of joke? You do not have all the items I requested.\"")
                locInfo = 6
        if guardianChoice == "2":
            if "Cursed Dagger" not in inventory:
                print("The guardian is far stronger than you and would kill you instantly if you tried fighting him. "
                      "Perhaps if you had some sort of weapon you'd stand a chance...")
            if "Cursed Dagger" in inventory:
                print("You plunge the dagger into the guardian's heart. He screams in sheer pain as the dagger begins to disintegrates his life essense.\n"
                      "Before dying, he bellows: \"WHY HAVE YOU DONE THIS? YOU TRULY ARE EVIL SCUM AND DESERVE THE WORST OF FATES!\" "
                      "The guardian fades into dust as he dies.\n"
                      "The path is now clear")
                morality = morality - 10
                guardianState = 3
                locInfo = 6
                score = score + 15
        if guardianChoice == "3":
            if necklace == 1 and garments == 1:
                print("\"You know, you do seem like a citizen of high stature. I will let you pass.\"")
                print("The guardian disappears, allowing you to move forward freely")
                guardianState = 1
                morality = morality + 2
                locInfo = 6
                score = score + 15
            else:
                print("The guardian laughs in your face and refuses to let you pass. "
                      "Perhaps if you could fool him somehow he would step aside...")
                locInfo = 6
        if guardianChoice == "4":
            print("\"I plan to use them to restore my power and rule this land as sovereign. "
                  "Please understand that I am not evil, I just see that this land is in chaos and needs order.\"")
            print("You see that the guardian is power-hungry, but killing him would still be wrong.\n")
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
                  "Can you please find us some food before we starve to death?\"\n")
            acceptQuest = input("1 - I will find him some food \n"
                                "2 - (Ignore her and take the dagger)\n"
                                "3 - You can all eat dirt, I don't care about you or your deadbeat husband \n"
                                "4 - (Give her food)\n"
                                "5 - (End Conversation)\n")
            if acceptQuest == "1":
                  print("\"Thank you! Come back as soon as you can!\"")
            if acceptQuest == "2":
                  print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path. "
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
                  killOrSpare = input("What will you do? \n"
                        "1 - (Kill him using the dagger) \n"
                        "2 - (Put the dagger back)\n")
                  if killOrSpare == "1":
                        print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body. Soon, the man is wiped from existence.\n"
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        print("There is no going back from the evil path you have embarked on.")
                        morality = morality - 15
                        inventory.append("Cursed Dagger")
                        shrineState = 3
                        shrineOpen = False
                        locInfo = 7
                        score = score + 15
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
                    morality = morality + 5
                    score = score + 10
                else:
                    print("You do not have the item required to perform that action")
    if shrineState == 2:
        print("What would you like to say?")
        acceptQuest = input("1 - I have changed my mind, I will find him some food. \n"
                             "2 - (Give her food)\n"
                             "3 - (Ignore her and take the dagger)\n"
                             "4 - (End Conversation)\n")
        if acceptQuest == "1":
            print("\"Fine then. Come back as soon as you can.\"")
        if acceptQuest == "2":
            if "Food" in inventory:
                print("\"Thank you kindly, ser! We certainly would have starved without your help! "
                      "If you wish to help further, <speak> to me again. I have another task for you\"")
                inventory.remove("Food")
                morality = morality + 5
                shrineState = 1
                score = score + 10
            else:
                print("You lack the required item to perform that action")
        if acceptQuest == "3":
            print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path. "
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
            killOrSpareTwo = input("What will you do? \n"
                                   "1 - (Kill him using the dagger) \n"
                                   "2 - (Put the dagger back)\n")
            if killOrSpareTwo == "1":
                print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body. Soon, the man is wiped from existence.\n"
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                print("There is no going back from the evil path you have embarked on.")
                morality = morality - 15
                inventory.append("Cursed Dagger")
                shrineState = 3
                shrineOpen = False
                locInfo = 7
                score = score + 15
    if shrineState == 11:
        evilChoiceTwo = input("\"What do you want? You're clearly not here to help us\"\n"
                              "1 - (Ignore her and take the dagger) \n"
                              "2 - (End conversation)\n")
        if evilChoiceTwo == "1":
                  print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path. "
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
                  killOrSpareTwo = input("What will you do? \n"
                        "1 - (Kill him using the dagger) \n"
                        "2 - (Put the dagger back)\n")
                  if killOrSpareTwo == "1":
                        print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body. Soon, the man is wiped from existence.\n"
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        print("There is no going back from the evil path you have embarked on.")
                        morality = morality - 15
                        inventory.append("Cursed Dagger")
                        shrineState = 3
                        shrineOpen = False
                        locInfo = 7
                        score = score + 15
                              
        

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
                       "1 - (Slaughter the rest of the family) \n"
                       "2 - (Leave)\n")
    if evilChoice == "1":
        print("You slaughter the mother and child mercilessly with the cursed dagger. "
              "Turning to leave the shrine, you hear their screams dissipate as the cursed energy from the dagger disintegrates their bodies.")
        shrineOpen = True
        shrineState = 4
        morality = morality - 30
        locInfo = 7
        score = score + 25
    else:
        print("You leave the shrine and they lock the door behind you again")

# special quest that triggers if you feed the family and speak to the woman again
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
                                  "2 - (End Conversation)\n")
        if daggerQuestAccept == "1":
            daggerQuestBegin = input("\"Would you like to go speak with him now?\"\n"
                                     "1 - Yes, bring me to him \n"
                                     "2 - No, I will do so later\n")
            if daggerQuestBegin == "1":
                print("The woman brings you to her husband")
                husbandSpeechCheck = input("He gets up from kneeling in front of the shrine.\n"
                                           "\"What do you want?!?\" He yells, angrily. \n"
                                           "1 - That dagger is evil and must be destroyed. Give it to me so I can do so. \n"
                                           "2 - (Try to take the dagger)\n"
                                           "3 - (End Conversation)\n")
                if husbandSpeechCheck == "1":
                    if garments == 1 or necklace == 1:
                        print("\"Really? Huh. Well, if you say so. You have been a great help so far anyway.\"\n"
                              "The man hands you the dagger.")
                        inventory.append("Cursed Dagger")
                        morality = morality + 5
                        shrineState = 10
                        score = score + 25
                    else:
                        print("\"You can have it over my dead body! Begone from my sight!\"")
                if husbandSpeechCheck == "2":
                    print("You run up and take the dagger. As you attempt to leave, the woman's husband blocks your path. "
                        "\"You're gonna have to kill me first if you want to leave with that dagger! I won't allow it!\" He yells.")
                    killOrSpareThree = input("What will you do? \n"
                        "1 - (Kill him using the dagger) \n"
                        "2 - (Put the dagger back)\n")
                    if killOrSpareThree == "1":
                        print("The man's wife and child watch in horror as you slaughter him using the dagger. "
                              "As he dies, you realize that the dagger causes an immensely painful death by slowly disintegrating "
                              "a person's body. Soon, the man is wiped from existence.\n"
                              "However, as you finish killing her husband, the woman manages to push you out of the shrine room "
                              "and lock the door.")
                        print("There is no going back from the evil path you have embarked on.")
                        morality = morality - 25
                        inventory.append("Cursed Dagger")
                        shrineState = 3
                        shrineOpen = False
                        locInfo = 7
                        score = score + 20
                        
    if shrineState == 10:
        sadisticChoice = input("\"Thank you so much for taking the dagger. Please do not use it for anything, just destroy it!\"\n"
                               "1 - {Kill them using the dagger)\n"
                               "2 - (End Conversation)\n")
        if sadisticChoice == "1":
            print("You slaughter the entire family mercileslly without any remorse.\n"
                  "Turning to leave the shrine, you hear their screams dissipate as the cursed energy from the dagger disintegrates their bodies.")
            shrineOpen = True
            shrineState = 12
            morality = morality - 50
            locInfo = 7
            score = score + 40
            
        

# special function for handling the end of the game
# here, the players actions throughout the game affect the ending they get
def finalEncounter():
    global locInfo
    global hasBeenSearched
    global world
    global score
    global guardianRequest
    global guardianState
    global garments
    global moves
    global necklace
    global shrineState
    global shrineOpen
    global morality
    global inventory
    global coldManState
    global familyHonored
    global daggerState
    global familyPhoto
    global moves
    score = score + 100
    score = score - moves
    input("During this section, press ENTER when ... appears at the end to continue...\n")
    print("The shard glows vibrantly as you use it and your fiance, in perfect detail, comes out from behind the throne to sit on it.\n"
          "\"I was waiting for you to come to this end, my love.\"\n")
    input("ENTER - How have you appeared here in such clear detail? You don't seem like a mere memory\n")
    print("\"You're not the only one in the world with strange abilities.\n"
          "I found out that in death, I can visit the dreams of the one I loved most if they still live. "
          "I can also control their dreams, but I only figured out how to do it recently. I made this world as a test for you.\"\n")
    input("ENTER - So, what happened to you? Tell me who took you from me!\n")
    input("\"You're still asking this? I cannot believe how blind you are to what is right in front of you. "
          "I'll save the answers for when we're done here. "
          "First, let's talk about what you've been doing in this dream world you've created for yourself.\n"
          "...")
    if guardianState == 1:
        input("You passed the guardian with a non-violent approach and without allowing him to become the ruler of this land.\n"
              "...")
    if guardianState == 2:
        input("You did the guardian's bidding and this land now has a power hungry dictator as a result.\n"
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
            input("You stole the Rare Coin from the old man and then proceeded to murder him needlessly.\n"
                  "...")
    elif coldManState == 3:
        input("You killed the old man with the cursed dagger for no reason other than bloodlust.\n"
              "...")
    if shrineState == 0:
        input("You did not help the family at the shrine.\n"
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
        input("Not only did you murder the man at the shrine, but you also broke back into the shrine and slaughtered the rest of his family too.\n"
              "Was killing the man in front of his family and stealing the dagger really not enough for you?\n"
              "...")
    if shrineState == 12:
        input("You tricked the family at the shrine into beliving that you wanted to help, but then you took the dagger and slaughtered all of them.\n"
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
        input("And finally, you found my ring, but neglected to honor my memory.\n"
              "...")
    if familyHonored == 2:
        input("And finally, you honored my memory by burying my ring where I wanted to be buried.\n"
              "...")
    if familyHonored == 3:
        input("And finally, you disgraced my memory by destroying my ring.\n"
              "...")
    input("If I had to score your morality somehow, I'd give you a "+str(morality)+"...")
    if morality <= -70:
        input("Now that you understand how horrible of a person you are. I'll tell you exactly who murdered your family...")
        input("You did. You killed me. You killed our daughter. You killed our son...")
        input("In the middle of the night, while sleepwalking, you lit a match on the stove and torched the whole house. "
              "Conveniently, you then stumbled out of the house and collapsed, leaving us to burn to death while you fled the country...")
        endChoice = input("This dream world you've created and the atrocious acts you've committed in it only prove how terrible of a person you are, subconsciously. "
              "What happened that night was a demonstration of your true desires: destruction, death, and chaos. Do you see it now?\"\n"
              "1 - I don't believe you\n"
              "2 - I don't care, I had fun\n"
              "3 - I'm sorry\n"
              "4 - (Continue)\n")
        if endChoice == "1":
            input("\"After all the atrocities you've committed, you don't believe yourself to be capable of this? Don't lie to yourself.\"")
        if endChoice == "2":
            input("\"You're evil and deserve to suffer...\"")
        if endChoice == "3":
            input("\"No, you are not. Nobody as evil as you are is ever sorry.\"")
        print("\"I actually cannot believe how staggeringly evil you are. "
              "It's almost like somebody is controlling your actions. No human this evil should even be allowed to live.")
        reasoning = input("Tell me, why did you do it? Why must you be so vile and destructive?\"\n"
                          "1 - Because I'm bored\n"
                          "2 - Because I can\n"
                          "3 - Because I don't care about anyone\n"
                          "4 - (Continue)\n")
        if reasoning == "1":
            print("\"Surely there must be a better solution for boredom other than mass killings and chaos!\"")
        if reasoning == "2":
            print("\"You are the worst kind of evil; the kind that exists just because the world cannot stop them "
                  "and lack any real reason for their actions. Your type cannot even be understood.\"")
        if reasoning == "3":
            print("\"Clearly! Nobody those capable of caring about others could do what you just did.\"")
        input("You must not be allowed to live, no matter the cost. I'm shutting down your brain so that you will never wake up from this dream. "
              "Doing so will destroy the only place I can reside in, but I don't care. I'm doing the world a massive service.\"")
        while True:
            resetChoice = input("\"Are you ready to die?\"\n"
                                "1 - Yes\n"
                                "2 - You cannot kill me\n"
                                "3 - (Kill Her)\n")
            if resetChoice == "1":
                input("\"Good. I am sorry, but this is the way it must be. I am ashamed to say that I ever loved you.\"")
                input("You feel yourself shutting down as your consciousness leaves you...")
                input("...")
                input("You finally breathe your last breath. Both you and the etheral version of your fiance die permanently in your dream.")
                print("\n\n\n\n\n")
                gameEndTrueEvil()
            if resetChoice == "2":
                print("Yes, I can. You are in a dream world that I created and I have control of your consciousness. "
                      "I can kill you and plan to do so when you are ready.")
            if resetChoice == "3":
                if "Cursed Dagger" not in inventory:
                    print("You lack the required item to attempt that action")
                elif "Cursed Dagger" in inventory:
                    input("You attempt to stab her with the dagger, but it disintegrates from your hand as you try.\n"
                          "\"Did you not think I would anticipate that? I created this world, you fool.\" She says...")
                    inventory.remove("Cursed Dagger")
                
            else:
                print("\"I have locked your body in this dream. "
                      "Your body can either starve to death or you can accept your fate now.\"\n")
                continue
    elif morality <= -10:
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
            input("\"After all the atrocities you've committed, you don't believe yourself to be capable of this? Don't lie to yourself.\"")
        if endChoice == "2":
            input("\"Really? You truly do deserve to suffer.\"")
        if endChoice == "3":
            input("\"It's far too late for apologies...\"")
        print("Ultimately, it was your choice, " +playerName+ ". You chose to be evil. There's only one option left. "
              "You've always had this strange ability to bring things from your dreams into the real world, "
              "though it comes at a great cost and you nearly died last time you brought anything of significance back to the world. "
              "That's a risk you need to take this time. Transfer the Dream Shard out of here and use it; it will automatically reset the timeline to before you killed us.\"")
        while True:
            resetChoice = input("1 - Fine, I'll do it\n"
                                "2 - If I'm as evil as you say, why would you do that for me?\n"
                                "3 - No, I refuse to do it\n")
            if resetChoice == "1":
                input("\"Good. I will wake you up now, and everything will be back the way it was before...\"")
                input("You wake up and use the Dream Shard. A cloud covers you as you begin to see a vision of the timeline you're being transfered to...")
                input("Your fiance tricked you.\n"
                      "The Dream Shard transfers you to the morning you woke up to find your family dead in the burning house...")
                input("You scream in agony as you feel the transfer process slowly removing your memories.\n "
                      "You are brought back to the beginning of your agony...\n")
                input("...")
                playerNameTwo = input("Your name is...you cannot seem to recall it. \nTry to remember your name: ").capitalize()
                print(playerNameTwo + "...Yes, that was it...")
                input("and so the cycle begins again...")
                print("\n\n\n\n\n")
                gameEndEvil()
            if resetChoice == "2":
                print("Because I love you and still believe that there is hope for us.")
            else:
                print("I'm not letting you wake up from this dream until you agree to it.\n")
                continue
    elif morality >= -9 and morality <= 9:
        input("Now that you understand what you've done. I'll tell you exactly who murdered your family...")
        input("You did. You killed me. You killed our daughter. You killed our son...")
        input("In the middle of the night, while sleepwalking, you lit a match on the stove and torched the whole house. "
              "Conveniently, you then stumbled out of the house and collapsed, leaving us to burn to death while you fled the country...")
        endChoice = input("This dream world you've created and the acts you've committed have not convinced me that you're evil, "
                          "but they have not convinced me that your act of arson was a lapse in judgement either.\"\n"
                          "1 - I don't believe you\n"
                          "2 - I don't care, I had fun\n"
                          "3 - I'm sorry\n"
                          "4 - (Say Nothing)\n")
        if endChoice == "1":
            input("\"But you do. You know it's true and that's the real reason why you ran...\"")
        if endChoice == "2":
            input("\"I see...\"")
        if endChoice == "3":
            input("\"It's far too late for apologies...\"")
        print("I still think you've suffered enough over the past few years" +playerName+ ". I leave you with one choice."
              "You've always had this strange ability to bring things from your dreams into the real world, "
              "though it comes at a great cost and you nearly died last time you brought anything of significance back to the world. "
              "That's a risk you need to take this time. Transfer the Dream Shard out of here; it will automatically wipe your memories."
              "It's the only way you will find peace.\"")
        while True:
            resetChoice = input("1 - Fine, I'll do it\n"
                                "2 - No, I refuse to do it\n")
            if resetChoice == "1":
                input("\"Good. I will wake you up now, and you will be able to live a normal life.\"")
                input("You wake up and use the Dream Shard. It seeps into your brain, "
                      "erasing all memories you have related to your family...")
                input("...")
                input("Your family was so interwoven into your life that the erasure process causes you to forget more than you anticipated...\n")
                input("You wake up with no recollection of who you are...")
                print("\n\n\n\n\n")
                gameEndNeutral()  
            else:
                print("I'm not letting you wake up from this dream until you agree to it.\n")
                continue
    elif morality >= 10:
        input("You...I can't do this, " +playerName+". you're a good person. You have always been...")
        input("I planned to try and convince you that you burned the house down and killed us but...I did it...\n")
        input("I don't know why I did it. Because I wanted to? Because I COULD do it? "
              "Sometimes there really is no reason for evil...\n")
        input("After I did it I immediately regretted it and tried to save everyone, "
              "but I had sedated you all before, so I couldn't wake anyone up. "
              "I carried you outside and tried to go get the kids, but the fire had already spread everywhere. "
              "They died and I died trying to save them.\"...\n")
        while True:
            endChoice = input("1 - I don't know what to say\n"
                              "2 - (Kill Her)\n"
                              "3 - I don't believe you\n"
                              "4 - What happens now, then?\n")
            if endChoice == "1":
                print("Please, you don't have to say anything, You married the wrong woman. That's all there is to know.")
                continue
            if endChoice == "2":
                if "Cursed Dagger" in inventory:
                    print("You rush her with the cursed dagger and plunge it into her heart.\n")
                    input("\"I...I understand...I deserve this.\" She stammers as she disintegrates...")
                    input("...")
                    print("\n\n\n\n\n")
                    gameEndRevenge()
                if "Cursed Dagger" not in inventory:
                    print("You do not have the item required to perform that action")
                    continue
            if endChoice == "3":
                print("I wish it were not true, my love. I'm sorry.")
            if endChoice == "4":
                print("As hard as it is for me to say...move on. If either of us try and use our powers to fix this, "
                      "the results will prove disastrous for you. I will leave and I will never disrupt your sleep again.")
                input("I'm sorry, "+playerName+". Try to forget about me...")
                input("...")
                print("\n\n\n\n\n")
                gameEndGood()
        
                          
def gameEndGood():
    global Score
    print("Congratulations on completing the game! \nYou have achieved the GOOD ending of the game with a final score of: "+str(score)+". \n"
          "This game has 5 endings, one of which is hidden in the GOOD ending. "
          "All of the endings are drastically different and reveal different information about the story. "
          "If you want to know how to achieve the other 4, just ask me!")
    input()
    quit(1)
    
def gameEndEvil():
    global Score
    print("Congratulations on completing the game! \nYou have achieved the EVIL ending of the game with a final score of: "+str(score)+". \n"
          "This game has 5 endings, one of which is hidden in the GOOD ending. "
          "All of the endings are drastically different and reveal different information about the story. "
          "If you want to know how to achieve the other 4, just ask me!")
    input()
    quit(1)

def gameEndNeutral():
    global Score
    print("Congratulations on completing the game! \nYou have achieved the NEUTRAL ending of the game with a final score of: "+str(score)+". \n"
          "This game has 5 endings, one of which is hidden in the GOOD ending. "
          "All of the endings are drastically different and reveal different information about the story. "
          "If you want to know how to achieve the other 4, just ask me!")
    input()
    quit(1)

def gameEndRevenge():
    global Score
    print("Congratulations on completing the game! \nYou have achieved the REVENGE ending of the game with a final score of: "+str(score)+". \n"
          "This game has 5 endings, one of which is hidden in the GOOD ending (you just achieved it). "
          "All of the endings are drastically different and reveal different information about the story. "
          "If you want to know how to achieve the other 4, just ask me!")
    input()
    quit(1)

def gameEndTrueEvil():
    global Score
    print("Congratulations on completing the game! \nYou have achieved the TRUE EVIL ending of the game with a final score of: "+str(score)+". \n"
          "This game has 5 endings, one of which is hidden in the GOOD ending (you just achieved it). "
          "All of the endings are drastically different and reveal different information about the story. "
          "If you want to know how to achieve the other 4, just ask me!")
    input()
    quit(1)

# note: max morality is 18 i think
# note: min morality is close to -100. I'm not sure.

def main():
    showIntro()
    gameLoop()

main()
