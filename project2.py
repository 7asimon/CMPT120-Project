meadow = ("this shit flowery")
burningVillage = ("this shit burned")
greyRoom = ("this shit grey")
dinnerTable = ("eat shit here")
cliff = ("dont jump off this shit")
houseInterior = ("strange shit going on in here")

score = 0

def gameIntro():
    print("GREYWALKER")
    print('')
    playerName = input("Your name is...you struggle to recall your name. Try to remember your name...")
    print("Ah, yes, "+playerName+", that was it. You are a sleepwalker and an insomniac who is attempting to master lucid dreaming."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input(" You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          " Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again. For now, press ENTER to continue.")
    stage1 = False
    if stage1 == False:
        scoreLocation()

def gameEnd():
    print("Suddenly, before you could discover all you needed to, you awaken from the dream. You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the cryptic message on the sign"
" To Be Continued In Future Game Versions...")
    print("Copyright: Abel Simon, abel.simon1@marist.edu")
    

def gameLoop():
    stage1 = True
    stage2 = False
    stage3 = False
    stage4 = False
    stage6 = False
    loop = 1
    while True:
        while loop == 1:
            location = meadow
            print("MEADOW")
            print("Score:",score)
            print(location)
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
            stage2 == True
            print("BURNING VILLAGE")
            print("Score:",score)
            print(location)
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
            stage3 == True
            print("CLIFF")
            print("Score:",score)
            print(location)
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
            stage4 == True
            print("GREY ROOM")
            print("Score:",score)
            print(location)
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
            stage5 == True
            print("DINNER TABLE")
            print("Score:",score)
            print(location)
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
            stage6 == True
            print("HOUSE INTERIOR")
            print("Score:",score)
            print(location)
            if score == 50:
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
