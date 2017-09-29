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
    playerName = input("Your name is...you struggle to recall your name. Try to remember your name.")
    print("Ah, yes, "+playerName+", that was it. You are a sleepwalker and an insomniac who is attempting to master lucid dreaming."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input(" You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          " Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again. For now, press ENTER to continue.")
    stage1 = False
    if stage1 == False:
        scoreLocation()
        stage1 == True

def gameEnd():
    print("You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the carving on the table."
" To Be Continued In Future Game Versions...")
    print("Copyright: Abel Simon, abel.simon1@marist.edu")
    

def gameLoop():
    stage1 = False
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
                loop = 1
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
                loop = 4

        while loop == 3:
            location = cliff
            if stage3 == False:
                storeLocation()
            stage3 == True
            print("CLIFF"
            print("Score:",score)
            print(location)
            userChoice = input()
            if userChoice = 
            

def scoreLocation():
        global score
        score = score + 5
        
    
            
gameIntro() 
gameLoop()
