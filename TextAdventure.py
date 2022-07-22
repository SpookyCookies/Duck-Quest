
import time,sys,os
import colorama
from colorama import Fore, Back, Style
colorama.init()
def FirstUserChoice():
        UserChoiceOne = input("What are you going to do now:  ")
        if UserChoiceOne == 'Describe':
            print('The room is dark, almost no light however, you are still able to see that there is a door')
            FirstUserChoice()
        if UserChoiceOne == 'Push':
            os.system('clear')
            print('What are you pushing on?')
            FirstUserChoice()
        if UserChoiceOne == 'Open':
            os.system('clear')
            print('What are you opening?')
            FirstUserChoice()
        if UserChoiceOne == 'Open Door':
            os.system('clear')
            typeanimation(FancyRoom)
            SecondUserChoice()
        if UserChoiceOne == 'Push Door':
            os.system('clear')
            print('How embarrasing!, this door is pull door')
            FirstUserChoice()
        if UserChoiceOne == 'Push Wall':
            os.system('clear')
            print('the fuck are you doing, stop that')
            FirstUserChoice()
        if UserChoiceOne == 'Push Candle':
            os.system('clear')
            typeanimation(CandelEnding)
            quit()
        if UserChoiceOne == 'Open Candle':
            os.system('clear')
            print('How would you open a candle...')
            time.sleep(5)
            print('Nevermind')
            FirstUserChoice()
        if UserChoiceOne == "Describe Room":
            os.system('clear')
            print('The room is dark, almost no light however, you are still able to see that there is a door')
            FirstUserChoice()
        if UserChoiceOne == "Describe Candle":
            os.system('clear')
            print('Old Fashioned Candle, not safe to eat but safe to look at')
            FirstUserChoice()
        if UserChoiceOne == "Describe Door":
            os.system('clear')
            print('Very beaten down wooden door looks looks like its been around for a while')
            FirstUserChoice()
        if UserChoiceOne == "Describe Me":
            os.system('clear')
            print('Beautiful')
            FirstUserChoice()
        else:
            os.system('clear')
            print("You canot",UserChoiceOne,"Remember to interact with the world you must use Describe/Push/Open/ and in some Special cases With")
            FirstUserChoice()
def SecondUserChoice():
                UserChoiceTwo = input('What are you going to do now:  ')
                if UserChoiceTwo == 'Push':
                    os.system('clear')
                    print('What are you pushing on?')
                    SecondUserChoice()
                if UserChoiceTwo == 'Open':
                    os.system('clear')
                    print('What are you opening?')
                    SecondUserChoice()
                if UserChoiceTwo == 'Describe':
                    os.system('clear')
                    print('The room is fancy with many \u001b[33mexpensive light fixtures\u001b[0m a piano and a table with some hot coca on it and a lot of Cummus Lord FunkoPops however there seems to be a hatch on the floor, interesting')
                    SecondUserChoice()
                if UserChoiceTwo == 'Describe Room':
                    os.system('clear')
                    print('The room is fancy with many \u001b[33mexpensive light fixtures\u001b[0m a piano and a table with some hot coca on it  and a lot of Cummus Lord FunkoPops however there seems to be a hatch on the floor, interesting')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe FunkoPops":
                    os.system('clear')
                    print('White box with plastic lining the sides letting you see the LIMITED EDITION Cummus Lord FunkoPops')
                    time.sleep(3)
                    print('This ones been used...')
                    time.sleep(2)
                    print('ew')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Hatch":
                    os.system('clear')
                    print('Decently sized hatch,\u001b[31m perfect to fit you.\u001b[0m')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Expensive Light Fixtures":
                    os.system('clear')
                    print('Look expensive, how did they get here anyway?')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Table":
                    os.system('clear')
                    print('Its a nice table\u001b[31m would be a shame if something happened to it...\u001b[0m')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Piano":
                    os.system('clear')
                    print('Old fashion piano looks expensive like everything else does here')
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Hidden Door":
                    os.system('clear')
                    print('Its a hidden door, originally hidden by FunkoPops,\u001b[31mI wonder what would happen if you open it...\u001b[0m')    
                    SecondUserChoice()
                if UserChoiceTwo == "Describe Hot Coca":
                    os.system('clear')
                    print('\u001b[31mHot\u001b[0m to the touch \u001b[31mHot\u001b[0m to drink')
                    SecondUserChoice()
                if UserChoiceTwo == "Push Coca":
                    os.system('clear')
                    print('\u001b[31mWhy?\u001b[0m')
                    SecondUserChoice()
                if UserChoiceTwo == "Push Expensive Light Fixtures":
                    os.system('clear')
                    print('\u001b[31mYou broke them, you ungrateful fuck, STOP BREAKING SHIT\u001b[0m')
                    SecondUserChoice()
                if UserChoiceTwo == "Open Coca":
                     os.system('clear')
                     print('How would you open Coca?')
                     SecondUserChoice()
                if UserChoiceTwo == 'Open FunkoPops':
                    os.system('clear')
                    print('Better not they look expensive and in mint condition too...')
                    SecondUserChoice()
                if UserChoiceTwo == "Open Table":
                     os.system('clear')
                     print('Why would you think this would work?')
                     SecondUserChoice()
                if UserChoiceTwo == "Open Piano":
                     os.system('clear')
                     print('And how are you going to do that smart guy?')
                     SecondUserChoice()
                if UserChoiceTwo == "Push Piano":
                     os.system('clear')
                     print('No pushing the piano')
                     SecondUserChoice()
                if UserChoiceTwo == "Play Piano":
                    os.system('clear')
                    print('You start playing the most beautiful song known to man, its amazing')
                    SecondUserChoice()     
                if UserChoiceTwo == 'Open Hatch':
                    os.system('clear')
                    typeanimation(Outside)
                    LastUserChoice()
                if UserChoiceTwo == 'Push Hatch':
                    os.system('clear')
                    print('Open it, lol')
                    SecondUserChoice()
                if UserChoiceTwo == 'Push Table':
                    os.system('clear')
                    typeanimation2(BreakTable)
                    SecondUserChoice()
                if UserChoiceTwo == 'Open Hidden Door':
                    os.system('clear')
                    typeanimation(SpaceEnding)
                    quit()
                if UserChoiceTwo == 'Push FunkoPops':
                    os.system('clear')
                    print('You pushed over the funkopops and now they are all over the floor, good going asshole, however you notice that there is a door')
                    SecondUserChoice()
                else:
                    os.system('clear')
                    print("Again, You canot",UserChoiceTwo," please only use Describe/Push/Open/ and in some Special cases With")
                    SecondUserChoice()
def LastUserChoice():
                UserChoiceLast = input('What are you going to do now:  ')
                if UserChoiceLast == 'Push':
                    os.system('clear')
                    print('I told you again and again and again\u001b[31m WHAT ARE YOU PUSHING????\u001b[0m')
                    LastUserChoice()
                if UserChoiceLast == 'Open':
                    os.system('clear')
                    print('ughhh... what are you opening?')
                    LastUserChoice()
                if UserChoiceLast == "Describe":
                    os.system('clear')
                    print('You seem to be on the side of a road with a car standing in front of you, its freezing cold out and snow is everywhere')
                    LastUserChoice()
                    LastUserChoice()
                if UserChoiceLast == "Describe Outside":
                    os.system('clear')
                    print('You seem to be on the side of a road with a car standing in front of you, its freezing cold out and snow is everywhere')
                    LastUserChoice()
                if UserChoiceLast == "Describe Trunk":
                     os.system('clear')
                     print('A trunk \u001b[31m perfect for storing dead bodies...\u001b[0m just messing around, I wonder whats inside of it')
                     LastUserChoice()
                if UserChoiceLast == "Describe Road":
                    os.system('clear')
                    print('Covered with snow and ice')
                    LastUserChoice()
                if UserChoiceLast == "Describe Car Door":
                    os.system('clear')
                    print('Just a car door')
                    LastUserChoice()
                if UserChoiceLast == "Describe Snow":
                    os.system('clear')
                    print('White stuff that falls from the sky,  \u001b[31m almost seems to be fake\u001b[0m')
                    LastUserChoice()
                if UserChoiceLast == "Describe Key":
                    os.system('clear')
                    print('Looks like the key to a car')
                    LastUserChoice()
                if UserChoiceLast == "Open Snow":
                    os.system('clear')
                    print('How would you possibly think to open snow?')
                    LastUserChoice()
                if UserChoiceLast == "Open Road":
                    os.system('clear')
                    print('Some call it the open road for a reason I guess...')
                    LastUserChoice()
                if UserChoiceLast == "Open Key":
                     os.system('clear')
                     print('Why in your right mind would you think to open a key?')
                     time.sleep(3)
                     print('I swear you got a few nuts & bolts loose upstairs dont you?')
                     LastUserChoice()
                if UserChoiceLast == "Push Car Door":
                    os.system('clear')
                    print('Dont push it you might break it')
                    LastUserChoice()
                if UserChoiceLast == "Push Key":
                    os.system('clear')
                    print('Might want to try Open Car Door With Key')
                    LastUserChoice()
                if UserChoiceLast == "Push Road":
                    os.system('clear')
                    print('Its as strudy as it will ever be')
                    LastUserChoice()
                if UserChoiceLast == "Push Me":
                     os.system('clear')
                     print('You are actually really pushing my buttons')
                     LastUserChoice()

                if UserChoiceLast == "Open Trunk":
                    os.system('clear')
                    print('You open the trunk with ease and you see a key, you pick it up')
                    LastUserChoice()
                if UserChoiceLast == 'Open Door':
                    os.system('clear')
                    print('You may want to try Open Car Door')
                    LastUserChoice()
                if UserChoiceLast == "Open Car Door":
                    os.system('clear')
                    print('\u001b[31mIts locked\u001b[0m you may want to try the trunk of the car' )
                    LastUserChoice()
                if UserChoiceLast == 'Open Car Door With Key':
                    os.system('clear')
                    typeanimation(CarEnding)
                    quit()
                if UserChoiceLast == "Push Snow":
                    os.system('clear')
                    typeanimation(RealEnding)
                    quit()
                else:
                    os.system('clear')
                    print('You Canot',UserChoiceLast,'Please Remember To only use Describe/Push/Open/ and in some Special cases With')
                    LastUserChoice()
IntroText = "\u001b[32mWelcome to: A Ducks Quest Of Time!\n\
By: Greg Soft aka Gang Weed Studios\n\
This game is very uppercase Sensitive so please use Uppercase at the start of each word\n\
Would you like to start the game? Y/N\u001b[0m\n\
"
WakingUp = "\u001b[32mGame Now Starting...\u001b[0m\n\
You wake up in a room, its\u001b[30;1m dark\u001b[0m there is only a\u001b[33m candle\u001b[0m, what are you going to do?\n\
You can interact with the\u001b[32m world\u001b[0m by using the words\u001b[33;1m Describe/Push/Open\u001b[0m and in some special cases\u001b[33;1m With\u001b[0m (Examples: Push Button, Open Button, Open Button With Key)\n\
"
RealEnding = "\u001b[1mYou pushed the snow and the whole world falls from beneath you, you are now falling and you wake up in your room playing Hentai Craft V2 thank god it was a dream\n\
You got the REAL ENDING?\n\
THE END."
CandelEnding = "\u001b[1mYou pushed the candle and the flame has gone out now you have been swallowed by darkness\n\
You try to run to the door you thought was there however by feeling the wall its not there anymore\n\
You slowly go insane and starve to death\n\
You got the WHY DID YOU PUT OUT THE CANDLE ENDING.\n\
THE END."
SpaceEnding = "\u001b[1mYou open the door and go into it falling into space, you cannot do anything else, you are stuck in space not being able to hear your own voice or move\n\
You have achieved THE SPACE ENDING\n\
THE END."
CarEnding = "\u001b[1mYou Escaped!\n\
You have achieved the CAR ENDING\n\
(perhaps there are secrets to be found?)\n\
THE END."
BreakTable = "\u001b[31mGreat you broke the table dipshit, apparently no one can have nice things in life\u001b[0m \n\
"
FancyRoom = "\u001b[1m\u001b[33mYou open the door and now you are met with a bright vibrant room\u001b[0m \n\
"
Outside = "\u001b[1mYou open the hatch and are now outside\u001b[0m \n\
"
def typeanimation(IntroText):
    for char in IntroText:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
os.system('clear')

typeanimation(IntroText)
def typeanimation2(IntroText):
    for char in IntroText:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)
os.system('clear')
def StartOfGame():
    UserInputOne = input()
    if UserInputOne == "Y":
        typeanimation(WakingUp)
        FirstUserChoice()
    if UserInputOne == "N":
        print('Ok Guess not then')
    
    else:
        print('Its Y or N')
        StartOfGame()
StartOfGame()
