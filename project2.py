score = 0
meadow = ("In your dream, you are walking forward in a meadow littered with wilted, white dasies. Smoke fills the air and the sky is tinted an eerily familiar shade of red."
" You try to sieze control of your body and set your own course, but your efforts prove futile."
" Your body continues to run forward with purpose despite there being nothing in sight other than the dasies in this seemingly endless field.")
burningVillage = ("this shit burned")
greyRoom = ("this shit grey")
dinnerTable = ("eat shit here")
cliff = ("dont jump off this shit")
houseInterior = ("strange shit going on in here")

def gameIntro():
    print("GREYWALKER")
    print('')
    playerName = input("Your name is...you struggle to recall your name. Try to remember your name.")
    print("Ah, yes, "+playerName+", that was it. You are a sleepwalker and an insomniac who is attempting to master lucid dreaming."
    " You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input(" You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          " Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again. For now, press ENTER to continue.")

def gameEnd():
    print("You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the carving on the table."
" To Be Continued In Future Game Versions...")
    print("Copyright: Abel Simon, abel.simon1@marist.edu")
    

def gameLoop():
    location = meadow
    score = 5
    print("MEADOW")
    print("Score:",score)
    print(location)
    meadow == True
    while True:
        userChoice = input()
        if userChoice == ("North"):
            location = burningVillage
            score = score + 5
            print("BURNING VILLAGE")
            print("Score:",score)
            print(location)
            userChoice = input()
            if userChoice == ("North"):
                location = houseInterior
                score = score + 5
                print("BURNING HOUSE")
                print("Score:",score)
                print(location)
            if userChoice == ("South"):
                print("MEADOW")
                print("Score:",score)
                print(location)
        if userChoice == ("Help"):
            print("Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again.")
        if userChoice == ("Quit"):
            quit(1)
        else:
            print("Please enter a valid command")
            
gameIntro() 
gameLoop()
