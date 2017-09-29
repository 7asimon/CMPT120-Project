# GREYWALKER
# Author: Abel Simon
# Date : September 29, 2017

score = 0

def gameIntro():
    print("GREYWALKER")
    print('')
    playerName = input("Your name is...you cannot seem to recall it. Try to remember your name: ")
    print("Ah, yes, " + playerName + ", that was it. You are a sleepwalker and an insomniac who is attempting to master lucid dreaming."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input(" You begin with a score of 0 and you will gain 5 points for every stage you progress through. You will win the game when all locations have been visited."
          " Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again. For now, press ENTER to continue. ")

meadow = ("As the dream begins, you find yourself in a vaguely familiar meadow filled with wilted daisies. Looking forward, you can see a village engulfed in flames. There appears to be areas of interest to the east, west, and south as well.")
burningVillage = ("The village is completely vacant as the buildings crumble and burn around you. However, in front of you lies one house that is completely unaffected by the fire, and a sign in front of it that reads: WHY HAVE YOU CAUSED US SUCH AGONY?")
greyRoom = ("You arrive in a grey room with random burned objects scattered about. As you walk into the room, the color fades from your skin and you notice everything you see is in black and white.")
dinnerTable = ("You arrive at a dinner table with a mirror image of yourself. No matter what you do, he does not speak to you.")
cliff = ("You arrive at the edge of a cliff with a dark abyss below it. There is nothing of interest here.")
houseInterior = ("Inside the house, you find that the walls are covered with black and white pictures of your family that were taken before they died mysteriously years ago. Eerily enough, you are missing from all the pictures as if you were cropped out of them.")
 
def gameEnd():
    print("Suddenly, before you could discover all you needed to, you awaken from the dream. You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the cryptic message on the sign"
" To Be Continued In Future Game Versions...")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)

def gameLoop():
    stage1 = False
    stage2 = False
    stage3 = False
    stage4 = False
    stage5 = False
    stage6 = False
    loop = 1
    while True:
        while loop == 1:
            location = meadow
            if stage1 == False:
                scoreLocation()
            stage1 = True
            print("MEADOW")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("North"):
                loop = 2
                break
            if userChoice == ("South"):
                loop = 3
                break
            if userChoice == ("East"):
                loop = 4
                break
            if userChoice == ("West"):
                loop = 5
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                loop = 1
                break
                
        while loop == 2:
            location = burningVillage
            if stage2 == False:
                scoreLocation()
            stage2 = True
            print("BURNING VILLAGE")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("South"):
                loop = 1
                break
            if userChoice == ("North"):
                loop = 6
                break
            if userChoice == ("East"):
                print("There is no desirable path to the east.")
                print('')
                break
            if userChoice == ("West"):
                print("There is no desirable path to the west.")
                print('')
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                break

        while loop == 3:
            location = cliff
            if stage3 == False:
                scoreLocation()
            stage3 = True
            print("CLIFF")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("North"):
                loop = 1
                break
            if userChoice == ("South"):
                  suicide = input("Continuing to go South will send you off the cliff and kill you. Are you sure you wish to die? (Y/N)")
                  if suicide == ("Y") or suicide == ("y"):
                      print("You have died within the dream and it has ended.")
                      quit(1)
                  else:
                      loop = 3
                      break
            if userChoice == ("East"):
                print("There is no desirable path to the east.")
                print('')
                break
            if userChoice == ("West"):
                print("There is no desirable path to the west.")
                print('')
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                break
        while loop == 4:
            location = greyRoom
            if stage4 == False:
                scoreLocation()
            stage4 = True
            print("GREY ROOM")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("North"):
                print("There is no desirable path to the north.")
                print('')
                break
            if userChoice == ("South"):
                print("There is no desirable path to the south.")
                print('')
                break
            if userChoice == ("East"):
                print("There is no desirable path to the east.")
                print('')
                break
            if userChoice == ("West"):
                loop = 1
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                break
        while loop == 5:
            location = dinnerTable
            if stage5 == False:
                scoreLocation()
            stage5 = True
            print("DINNER TABLE")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("North"):
                print("There is no desirable path to the north.")
                print('')
                break
            if userChoice == ("South"):
                print("There is no desirable path to the south.")
                print('')
                break
            if userChoice == ("East"):
                loop = 1
                break
            if userChoice == ("West"):
                print("There is no desirable path to the west.")
                print('')
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                break
        while loop == 6:
            location = houseInterior
            if stage6 == False:
                scoreLocation()
            stage6 = True
            print("HOUSE INTERIOR")
            print("Score:",score)
            print(location)
            if score == 30:
                gameEnd()
            userChoice = input()
            if userChoice == ("North"):
                print("There is no desirable path to the north.")
                print('')
                break
            if userChoice == ("South"):
                loop = 2
                break
            if userChoice == ("East"):
                print("There is no desirable path to the east.")
                print('')
                break
            if userChoice == ("West"):
                print("There is no desirable path to the west.")
                print('')
                break
            if userChoice == ("Help"):
                print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
                print('')
                break
            if userChoice == ("Quit"):
                quit(1)
            else:
                print("Please enter a valid command")
                print('')
                break
            

def scoreLocation():
        global score
        score = score + 5
        
    
            
gameIntro()
gameLoop()
