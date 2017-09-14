score = 0
gamestart = ("You are a sleepwalker and an insomniac who is attempting to master lucid dreaming. You are currently stuck in a dream;"
" aware that you are in a dream state but unable to control your actions. You begin with a score of 0 and you will gain 5 points for every stage you progress through.")
meadow = ("In your dream, you are walking forward in a meadow littered with wilted, white dasies. Smoke fills the air and the sky is tinted an eerily familiar shade of red."
" You try to sieze control of your body and set your own course, but your efforts prove futile."
" Your body continues to run forward with purpose despite there being nothing in sight other than the dasies in this seemingly endless field.")
table = ("After what felt like hours of non-stop running, you come across a strange figure eating alone at a small table."
" Upon venturing closer, you realize that the person sitting there is a mirror image of yourself."
" You are terrified by this and wish to run away, but your body goes and sits down across from him against your will.")
greyroom = ("Suddenly, the entire meadow begins to fold in on itself as the color changes to a bleak grey."
" You watch as the color also drains from yourself and your surroundings until everything in your dream is black and white."
" \" You're certainly wondering where you are, aren't you?\" the mirror image asks of you, barely able to control his laughter."
" He lifts his fork from the plate and forcefully stabs it into the table."
" The letters he begins carving are rough and jagged, but when he finishes you can clearly make out the words \" D E A T H  R O W \".")
dreamend = ("Upon reading the words, you violently jolted up from your bed. You had experienced strange dreams before, but the meadow felt far too familiar for it to be pure coincidence...")
conclusion = ("You knew you had no choice but to lucid dream and re-enter that strange world so that you could figure out what happened and the reason for the carving on the table."
" To Be Continued In Future Game Versions...")

location = gamestart
print("GREYWALKER")
print('')
print(location)
print('')
input("Press ENTER to continue...")
print('')
score = score + 5
location = meadow
print(location)
print('')
print("Your score is ", score)
input("Press ENTER to continue...")
print('')
score = score + 5
location = table
print(location)
print('')
print("Your score is ", score)
input("Press ENTER to continue...")
print('')
score = score + 5
location = greyroom
print(location)
print('')
print("Your score is ", score)
input("Press ENTER to continue...")
print('')
score = score + 5
location = dreamend
print(location)
print('')
print("Your final score is ", score)
input("Press ENTER to continue...")
print('')
print(conclusion)
print('')
print("Copyright: Abel Simon, abel.simon1@marist.edu")
