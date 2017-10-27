# GREYWALKER
# Author: Abel Simon
# Date : October 23, 2017

score = 0

moves = 0

def showIntro():
    print("GREYWALKER")
    print('')
    playerName = input("Your name is...you cannot seem to recall it. Try to remember your name: ")
    print("Ah, yes, " + playerName + ", that was it. You are a sleepwalker"
          "and an insomniac who is attempting to master lucid dreaming."
    "You have successfully assumed control of yourself within your dream and intend to explore the strange realm you have dreamed of.")
    print('')
    input(" You begin with a score of 0 and you will gain 5 points for every stage you progress through."
          "You will win the game when all locations have been visited."
          " Type North, South, East, or West to navigate, type Quit to end the game, or type Help to view this message again."
          " For now, press ENTER to continue. ")
    

location = ["You find yourself in a vaguely familiar meadow filled with wilted daisies."
          " Looking forward, you can see a village engulfed in flames."
          " There appears to be areas of interest to the east, west, and south as well.",
            "The village is completely vacant as the buildings crumble and burn around you."
            "However, in front of you lies one house that is completely unaffected by the fire,"
            "and a sign in front of it that reads: WHY HAVE YOU CAUSED US SUCH AGONY?",
            "You arrive in a grey room with random burned objects scattered about."
            "As you walk into the room, the color fades from your skin and you notice everything you see is in black and white." ,
             "You arrive at a dinner table with a mirror image of yourself. No matter what you do, he does not speak to you.",
             "You arrive at the edge of a cliff with a dark abyss below it. There is nothing of interest here.",
             "Inside the house, you find that the walls are covered with black and white pictures of your family"
                "that were taken before they died mysteriously years ago."
                "Eerily enough, you are missing from all the pictures as if you were cropped out of them.",
             "You come across a wall with seemingly meaningless inscribings on them. You cannot make out what the strange drawings say.",
             "Walking down the path, you witness many villagers screaming in agony and running down the street."
             "There appears to be an endless number of them"]

hasBeenThere = [False, False, False, False, False, False, False, False]

curLocation = location[0]
 
def gameEnd():
    print("Suddenly, before you could discover all you needed to, you awaken from the dream."
          "You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the cryptic message on the sign"
" To Be Continued In Future Game Versions...")
    input("Copyright: Abel Simon, abel.simon1@marist.edu")
    quit(1)



def gameLoop():
        global curLocation
        global location
        global score
        global stage
        while True:
           if moves == 15:
               input("You have taken too long to explore your dream and so it has ended")
               quit()
           print(curLocation)
           if score == 35:
               gameEnd()
           userChoice = input()
           userChoice = userChoice.lower()
           if userChoice == ("north"):
               if curLocation == location[0]:
                   goTo(2)
               elif curLocation == location[1]:
                   goTo(3)
               elif curLocation == location[2]:
                   goTo(5)
               elif curLocation == location[3]:
                   goTo(6)
               elif curLocation == location[4]:
                   goTo(7)
               elif curLocation == location[5]:
                   print("That is not a valid direction from your currrent location")
               elif curLocation == location[6]:
                   print("That is not a valid direction from your currrent location")
               else:
                   print("That is not a valid direction from your currrent location")
           if userChoice == ("south"):
                if curLocation == location[0]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[1]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[2]:
                    goTo(0)
                elif curLocation == location[3]:
                    goTo(1)
                elif curLocation == location[4]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[5]:
                    goTo(2)
                elif curLocation == location[6]:
                    goTo(3)
                elif curLocation == location[7]:
                    goTo(4)
                else:
                    print("That is not a valid direction from your currrent location")
           if userChoice == ("west"):
                if curLocation == location[0]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[1]:
                    goTo(0)
                elif curLocation == location[2]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[3]:
                    goTo(2)
                elif curLocation == location[4]:
                    goTo(3)
                elif curLocation == location[5]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[6]:
                    goTo(5)
                elif curLocation == location[7]:
                    goTo(6)
                else:
                    print("That is not a valid direction from your currrent location")
           if userChoice == ("east"):
                if curLocation == location[0]:
                    goTo(1)
                elif curLocation == location[1]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[2]:
                    goTo(3)
                elif curLocation == location[3]:
                    goTo(4)
                elif curLocation == location[4]:
                    print("That is not a valid direction from your currrent location")
                elif curLocation == location[5]:
                    goTo(6)
                elif curLocation == location[6]:
                    goTo(7)
                elif curLocation == location[7]:
                    print("That is not a valid direction from your currrent location")
           if userChoice == ("score"):
                print(score)
           if userChoice == ("help"):
                print("Type North, South, East, or West to navigate, type Map to view the map, type Points to view your score,"
                      " or type Quit to end the game."
                      " You may also type Help at any point to view this message again.")
           if userChoice == ("quit"):
               quit()
           if userChoice == ("map"):
                print(
                       "House Interior ============= Strange Wall ============== Path of Agony \n"
                       "     ||                           ||                          ||       \n"
                       "     ||                           ||                          ||       \n"
                       "     ||                           ||                          ||       \n"
                       "     ||                           ||                          ||       \n"
                       " Grey Room ================ Dinner Table =================== Cliff     \n"
                       "     ||                           ||                                   \n"                  
                       "     ||                           ||                                   \n"
                       "     ||                           ||                                   \n"
                       "     ||                           ||                                   \n"
                       "   Meadow ==================== Village                                 \n"
                      )

def goTo(x):
    global curLocation
    global stage
    global score
    global moves
    curLocation = location[x]
    moves = moves + 1
    if hasBeenThere[x] is False:
        score = score + 5
        hasBeenThere[x] = True    

def main():
    showIntro()
    gameLoop()

main()
