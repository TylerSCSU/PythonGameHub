import random
import time
import pickle

def menu():
    print('Game Menu')
    print('----------------------')
    print('1. Guessing Games')
    print('2. Competition Games')
    print('----------------------')
    print('3. Exit')

    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Please choose a category: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')
    
        if int(choice) == 1:
            guessing()
        elif int(choice) == 2:
            competetive()
        elif int(choice) == 3:
            exit()
        else:
            print('Please choose a valid option. (1-3)')
            print('')

def guessing():
    print('')
    print('Guessing Games')
    print('----------------------')
    print('1. Guess the Number')
    print('2. Code Breaker')
    print('3. Hang-Man')
    print('4. Back')

    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')

        if int(choice) == 1:
            GTN_menu(GTN_high_scores)
        elif int(choice) == 2:
            CB_menu(CB_high_scores)
        elif int(choice) == 3:
            HM_menu()
        elif int(choice) == 4:
            menu()
        else: 
            print('Please enter a valid option. (1-4)')

def competetive():
    print('')
    print('Competetive Games')
    print('----------------------')
    print('1. Rock, Paper, or Scissors')
    print('2. Impossible-Game')
    print('3. Highest-Roll')
    print('4. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')

        if int(choice) == 1:
            RPS_menu(RPS_high_scores)
        elif int(choice) == 2:
            IG_menu()
        elif int(choice) == 3:
            HR_menu()
        elif int(choice) == 4:
            menu()
        else:
            print('Please enter a valid option. (1-4) ')
    
#Rock Paper Scissors
def RPS_menu(RPS_high_scores):

    print('Rock, Paper, or Scissors')
    print('The classic childrens game where you try to out smart your opponent, or at least try to make the right symbol using your hands.')
    print('----------------------')
    print('1. Single Player')
    print('2. Multiplayer')
    print('3. How-to-Play')
    print('4. High Scores')
    print('5. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')

        if int(choice) == 1:
            RPS(RPS_high_scores)
        elif int(choice) == 2:
            RPS_TWO()
        elif int(choice) == 3:
            RPS_HTP()
        elif int(choice) == 4:
            RPS_high(RPS_high_scores)
        elif int(choice) == 5:
            RPS_pickle_out(RPS_high_scores)
            competetive()
        else:
            print('Please enter a valid option: ')
            print('')

def RPS(RPS_high_scores):
    testing = 'n'
    #cont = 'y'
    userwins = 0
    compwins = 0

    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')

    testing = input('Are you testing? (Do you want to see the computer\'s choice?) Enter "y" or "n": ')
    while str(testing) != 'y' and str(testing) != 'Y' and str(testing) != 'n' and str(testing) != 'N' and str(testing).upper() != 'QUIT':
        testing = input('Please enter "y" or "n": ')
    
    if str(testing).upper() == 'QUIT':
        print('')
        RPS_menu(RPS_high_scores)
    
    while int(compwins) == 0:
        number = 0
        shoot = 0
        while number == shoot:

            for x in range(1):
                number = random.randint(1,3)
            
            if str(testing) == 'y' or str(testing) == "Y":
                if number == 1:
                    Comp = 'Rock'
                elif number == 2:
                    Comp = 'Paper'
                elif number == 3:
                    Comp = 'Scissors'
                print('')
                print('Testing ---- Computers Choice: ' + str(Comp))
                print('')

            choice = input('Choose Rock, Paper, or Scissors: ')
            while str(choice).upper() != 'ROCK' and  str(choice).upper() != 'PAPER' and str(choice).upper() != 'SCISSORS' and str(choice).upper() != 'QUIT':
                choice = input('Please choose one of the following; Rock, Paper, or Scissors: ')

            def Chosen(choice, shoot):
                if choice.upper() == 'QUIT':
                    RPS_menu(RPS_high_scores)
                elif choice.upper() == 'ROCK':
                    shoot = 1
                elif choice.upper() == 'PAPER':
                    shoot = 2
                elif choice.upper() == 'SCISSORS':
                    shoot = 3
                return shoot
            
            shoot = Chosen(choice, shoot)
            Comp = 'None'
            
            if number == 1:
                Comp = 'Rock'
            elif number == 2:
                Comp = 'Paper'
            elif number == 3:
                Comp = 'Scissors'

            print('Computer has chosen: ' + str(Comp))

            def Winner(number, shoot, userwins, compwins):
                if number == 1 and shoot == 2:
                    print('User Wins!')
                    userwins += 1
                elif number == 1 and shoot == 3:
                    print('Computer Wins!')
                    compwins += 1
                elif number == 2 and shoot == 1:
                    print('Computer Wins!')
                    compwins += 1
                elif number == 2 and shoot == 3:
                    print('User Wins!')
                    userwins += 1
                elif number == 3 and shoot == 1:
                    print('User Wins!')
                    userwins += 1
                elif number == 3 and shoot == 2:
                    print('Computer Wins!')
                    compwins += 1
                else :
                    print('It\'s a tie! Let\'s try again!')
                
                return userwins, compwins
            
            userwins, compwins = Winner(number, shoot, userwins, compwins)

        if int(compwins) == 1:
            print('Final Score: ' + str(userwins))
            # Check to see if they made a high score here by loading the list of high scores
            name = input('Please enter your name: ')
            RPS_high_scores.append((userwins, name))
            print('')
            RPS_menu(RPS_high_scores)

        else :
            print('Score: ' + str(userwins))
        
        # cont = input('Play again? ("y" or "n")')
        # while str(cont) != 'y' or str(cont) != 'Y' or str(cont) != 'n' or str(cont) != 'N':
        #     cont = input('Please enter "y" or "n" to continue: ')

def RPS_TWO():
    userwins = 0
    compwins = 0

    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    player1 = input('Enter Player 1\'s name: ')
    while len(player1) == 0:
        player1 = input('Enter Player 1\'s name: ')
    if str(player1).upper() == 'QUIT':
        print('')
        RPS_menu(RPS_high_scores)
    player2 = input('Enter Player 2\'s name: ')
    while len(player2) == 0:
        player2 = input('Enter Player 2\'s name: ')
    if str(player2).upper() == 'QUIT':
        print('')
        RPS_menu(RPS_high_scores)
    cont = 'y'
    while cont.upper() == 'Y' or cont.upper() == 'YES':
        compwins = 0
        while int(compwins) == 0:
            number = 0
            shoot = 0
            while number == shoot:
                choice = input(str(player1) + ', Choose Rock, Paper, or Scissors: ')
                while str(choice).upper() != 'ROCK' and  str(choice).upper() != 'PAPER' and str(choice).upper() != 'SCISSORS' and str(choice).upper() != 'QUIT' :
                    choice = input(str(player1) + ', please choose one of the following; Rock, Paper, or Scissors: ')
                time.sleep(.5)
                if str(choice).upper() == 'QUIT':
                    print('')
                    RPS_menu(RPS_high_scores)
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print(str(player1) + '\'s choice has been hidden.')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')

                choose = input(str(player2) + ', Choose Rock, Paper, or Scissors: ')
                while str(choose).upper() != 'ROCK' and  str(choose).upper() != 'PAPER' and str(choose).upper() != 'SCISSORS' and str(choose).upper() != 'QUIT':
                    choose = input(str(player2) + ', please choose one of the following; Rock, Paper, or Scissors: ')

                if str(choose).upper() == 'QUIT':
                    print('')
                    RPS_menu(RPS_high_scores)

                def Chosen1(choice, shoot):
                    if choice.upper() == 'ROCK':
                        shoot = 1
                    elif choice.upper() == 'PAPER':
                        shoot = 2
                    elif choice.upper() == 'SCISSORS':
                        shoot = 3
                    return shoot

                def Chosen2(choose, shoot1):
                    if choose.upper() == 'ROCK':
                        shoot1 = 1
                    elif choose.upper() == 'PAPER':
                        shoot1 = 2
                    elif choose.upper() == 'SCISSORS':
                        shoot1 = 3
                    return shoot1
                
                shoot = Chosen1(choice, shoot)
                number = Chosen2(choose, number)        

                print(str(player1) + ' has chosen: ' + str(choice))

                def Winner(number, shoot, userwins, compwins):
                    if number == 1 and shoot == 2:
                        print(str(player1 + ' Wins!'))
                        userwins += 1
                    elif number == 1 and shoot == 3:
                        print(str(player2 + ' Wins!'))
                        compwins += 1
                    elif number == 2 and shoot == 1:
                        print(str(player2 + ' Wins!'))
                        compwins += 1
                    elif number == 2 and shoot == 3:
                        print(str(player1 + ' Wins!'))
                        userwins += 1
                    elif number == 3 and shoot == 1:
                        print(str(player1 + ' Wins!'))
                        userwins += 1
                    elif number == 3 and shoot == 2:
                        print(str(player2 + ' Wins!'))
                        compwins += 1
                    else :
                        print('It\'s a tie! Let\'s try again!')
                        print('')
                        time.sleep(1.5)
                    
                    return userwins, compwins
                
                userwins, compwins = Winner(number, shoot, userwins, compwins)

            if int(compwins) == 1:
                print('Congratulations ' + str(player2) + '!')
                print('')
                
            else :
                print('Congratulations ' + str(player1) + '!')
                print('')
            compwins = 1
        cont = input('Play again? Enter a "y" to continue, else enter any other key to quit): ')
        print('')

    time.sleep(1)
    RPS_menu(RPS_high_scores)

def RPS_HTP():
    print('Rock, Paper, or Scissors')
    print('The classic childrens game where you try to out smart your opponent, or at least try to make the right symbol using your hands.')
    print('----------------------')
    print('Choose one of the three options when asked too.')
    print('There are many different scenarios the options can have, based on what your opponent chooses.')
    print('Rock beats Scissors, Scissors beats Paper, and Paper beats Rock')
    print('1. You win! (How: You choose an option that beats your opponents. Simple, right?)')
    print('2. You lose! (How: You choose an option that loses to your opponents choice. Again, pretty simple.)')
    print('3. You tie! (How: You and your opponent chose the same option! Wow! What are the odds! (1/3 apparently... I looked it up...')
    print('You play until you lose! The longer you win, the better your score! If the computer wins, you lose!')
    print('')
    back = input('Enter "1" to go back to the menu... When you are ready, of course... : ')
    while back != '1':
        back = input('I said enter "1"!!!!! Try again: ')
    
    if int(back) == 1:
        print('')
        RPS_menu(RPS_high_scores)

def RPS_high(RPS_high_scores):
    print('')
    print('HIGH SCORES')
    print('------------------------')
    RPS_high_scores.sort(reverse = True)
    for score, name in RPS_high_scores:
        print("{{name:>{col_width}}} | {{score:<{col_width}}}".format(col_width=(5-3)//2).format(name=name, score=score))
    print('')
    pause = input('Enter any key to return to the menu: ')
    print('')
    RPS_menu(RPS_high_scores)

def RPS_pickle_in():
    try:
        in_file = open('RPS_high_scores.txt', 'rb')
        RPS_high_scores = pickle.load(in_file)
    except IOError:
        in_file = open('RPS_high_scores.txt', 'w')
        RPS_high_scores = []

    return RPS_high_scores

def RPS_pickle_out(RPS_high_scores):
    save_file = open('RPS_high_scores.txt','wb')
    pickle.dump(RPS_high_scores, save_file)
    save_file.close()

#Guess the number
def GTN_menu(GTN_high_scores):
    print('')
    print('Guess the Number')
    print('Just a guessing game! Try to guess the number in the least amount of guesses!')
    print('----------------------')
    print('1. Single Player')
    print('2. Multiplayer')
    print('3. How-to-Play')
    print('4. High Scores')
    print('5. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')        

        if int(choice) == 1:
            GTN(GTN_high_scores)
        elif int(choice) == 2:
            GTN_TWO()
        elif int(choice) == 3:
            GTN_HTP()
        elif int(choice) == 4:
            GTN_high(GTN_high_scores)
        elif int(choice) == 5:
            GTN_pickle_out(GTN_high_scores)
            guessing()
        else:
            print('Please enter a valid option: ')
            print('')
    
def GTN(GTN_high_scores):
    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    print('Choose the range you\'d like to use!')
    print('(Just a reminder, only option "3" can get you on the leaderboards!)')
    print('--------------------------------------')
    print('1. 1 - 10 (Easy)')
    print('2. 1 - 100 (Medium)')
    print('3. 1 - 1000 (Hard)')
    print('--------------------------------------')
    option = input('Enter option (1-3): ')
    while option != '1' and option != '2' and option != '3' and option.upper() != 'QUIT':
        option = input('Please input a valid option (1-3): ')
    print('')

    if str(option).upper() == 'QUIT':
        print('')
        GTN_menu(GTN_high_scores)

    testing = input('Are you testing? (Do you want to see the computer\'s choice?) Enter "y" or "n": ')
    while str(testing).upper() != 'Y' and str(testing).upper() != 'N' and str(testing).upper() != 'quit':
        testing = input('Please enter "y" or "n": ')

    if str(testing).upper() == 'QUIT':
        print('')
        GTN_menu(GTN_high_scores)
    elif int(option) == 1:
        for x in range(1):
            number = random.randint(1,10)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        while True:
            try:
                pick = input('It\'s a number 1 - 10: ')
                pick = int(pick)
                print('')
                break
            except:
                if pick.upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your guess can only be a number.')
                    print('')

    elif int(option) == 2:
        for x in range(1):
            number = random.randint(1,100)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        while True:
            try:
                pick = input('It\'s a number 1 - 100: ')
                pick = int(pick)
                print('')
                break
            except:
                if pick.upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your guess can only be a number.')
                    print('')

    elif int(option) == 3:
        for x in range(1):
            number = random.randint(1,1000)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        while True:
            try:
                pick = input('It\'s a number 1 - 1000: ')
                pick = int(pick)
                print('')
                break
            except:
                if pick.upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your guess can only be a number.')
                    print('')

    times = 0

    while True:
        if int(pick) > int(number):
            times += 1
            print('Too high, try again.')
            while True:
                try:
                    pick = input()
                    pick = int(pick)
                    print('')
                    break
                except:
                    if str(pick).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your guess can only be a number.')
                        print('')
        elif int(pick) < int(number):
            times += 1
            print('Too low, try again.')
            while True:
                try:
                    pick = input()
                    pick = int(pick)
                    print('')
                    break
                except:
                    if str(pick).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your guess can only be a number.')
                        print('')
        else :
            times += 1
            print('Congratulations! You guessed the right number! --- ' + str(number) + ' --- In this many tries: ' + str(times))
            if int(option) == 3:
                name = input('Please enter your name: ')
                if name.upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                GTN_high_scores.append((times, name))
            time.sleep(1.5)
            GTN_menu(GTN_high_scores)

def GTN_TWO():
    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    print('Player 1 will choose the range, and then the number.')
    print('Player 2 will be guessing the number.')
    print('Choose the range you\'d like to use!')
    print('--------------------------------------')
    print('1. 1 - 10 (Easy)')
    print('2. 1 - 100 (Medium)')
    print('3. 1 - 1000 (Hard)')
    print('--------------------------------------')
    option = input('Enter option (1-3): ')
    while option != '1' and option != '2' and option != '3' and option.upper() != 'QUIT':
        option = input('Please input a valid option (1-3): ')
    print('')
    if option.upper() == 'QUIT':
        GTN_menu(GTN_high_scores)
    pick = 0
    number = 0

    
    if int(option) == 1:
            while int(number) < 1 or int(number) > 10:
                try:
                    number = input('Player 1, pick a number 1 - 10: ')
                    number = int(number)
                    print('')
                    break
                except:
                    if str(number).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your choice can only be a number 1 - 10.')
                        print('')
            time.sleep(1.5)
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('The number has been hidden.')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')   

            
            print('1 - 10')
            while True:
                try:
                    pick = input('Player 2, guess a number: ')
                    pick = int(pick)
                    print('')
                    break
                except:
                    if str(pick).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your guess can only be a number.')
                        print('')


    elif int(option) == 2:
        while int(number) < 1 or int(number) > 100:
            try:
                number = input('Player 1, pick a number 1 - 100: ')
                number = int(number)
                print('')
                break
            except:
                if str(number).upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your choice can only be a number 1 - 100.')
                    print('')
        time.sleep(1.5)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('The number has been hidden.')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')    

        print('1 - 100')
        while True:
            try:
                pick = input('Player 2, guess a number: ')
                pick = int(pick)
                print('')
                break
            except:
                if str(pick).upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your guess can only be a number.')
                    print('')

    elif int(option) == 3:
        while int(number) < 1 or int(number) > 1000:
            try:
                number = input('Player 1, pick a number 1 - 1000: ')
                number = int(number)
                print('')
                break
            except:
                if str(number).upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your choice can only be a number 1 - 1000.')
                    print('')
        time.sleep(1.5)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('The number has been hidden.')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')    

        print('1 - 1000')
        while True:
            try:
                pick = input('Player 2, guess a number: ')
                pick = int(pick)
                print('')
                break
            except:
                if str(pick).upper() == 'QUIT':
                    print('')
                    GTN_menu(GTN_high_scores)
                else :
                    print('Your guess can only be a number.')
                    print('')

    times = 0
    while True:
        if str(pick).upper() == 'QUIT':
                print('')
                GTN_menu(GTN_high_scores)
        elif int(pick) > int(number):
            times += 1
            print('Too high, try again.')
            while True:
                try:
                    pick = input()
                    pick = int(pick)
                    print('')
                    break
                except:
                    if str(pick).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your guess can only be a number.')
                        print('')
        elif int(pick) < int(number):
            times += 1
            print('Too low, try again.')
            while True:
                try:
                    pick = input()
                    pick = int(pick)
                    print('')
                    break
                except:
                    if str(pick).upper() == 'QUIT':
                        print('')
                        GTN_menu(GTN_high_scores)
                    else :
                        print('Your guess can only be a number.')
                        print('')
        else:
            times += 1
            print('Congratulations! You guessed the right number! --- ' + str(number) + ' --- In this many tries: ' + str(times))
            time.sleep(1.5)
            GTN_menu(GTN_high_scores)
            
def GTN_HTP():
    print('')
    print('Guess the Number')
    print('Just a guessing game! Try to guess the number in the least amount of guesses!')
    print('----------------------')
    print('I\'m sure I don\'t need to explain how you guess. Didn\'t you do that throughout highschool and college?')
    print('You guess the number!')
    print('Choose between three options to create the difficulty of your choosing.')
    print('1. 1 - 10. (Honestly if you take more then ten guesses to get this one correct, there isn\'t anything I can do to help you... ')
    print('2. 1 - 100 (A bit more difficult. You\'ll find this to be the most fun experience you\'ve had in the past... how long have you been playing? ')
    print('3. 1 - 1000 (Now this is what separates the strong from the weak. And by strong, I mean insane... It\'s 1000 numbers... ')
    print('Just so you know, only the third option gets a spot on the high scores list. You have to earn that!')
    print('')
    back = input('Enter "1" to go back to the menu... Or should I make you guess the number to go back... : ')
    if back != '1':
        back = input('Well well well, you typed something other than 1... Did you think I would be that cruel? (Go ahead and try again! I\'ll wait!): ')
    
    while back != '1':
        back = input('I was only kidding about making you guess... Just type "1" when you are ready to return. (Sorry!): ')
    
    if back == '1':
        GTN_menu(GTN_high_scores)

def GTN_high(GTN_high_scores):
    print('')
    print('HIGH SCORES')
    print('------------------------')
    GTN_high_scores.sort(reverse = False)
    for score, name in GTN_high_scores:
        print("{{name:>{col_width}}} | {{score:<{col_width}}}".format(col_width=(5-3)//2).format(name=name, score=score))
    print('')
    pause = input('Enter any key to return to the menu: ')
    print('')
    GTN_menu(GTN_high_scores)

def GTN_pickle_in():
    try:
        in_file = open('GTN_high_scores.txt', 'rb')
        GTN_high_scores = pickle.load(in_file)
    except IOError:
        in_file = open('GTN_high_scores.txt', 'w')
        GTN_high_scores = []

    return GTN_high_scores

def GTN_pickle_out(GTN_high_scores):
    save_file = open('GTN_high_scores.txt','wb')
    pickle.dump(GTN_high_scores, save_file)
    save_file.close()

#Code Breaker
def CB_menu(CB_high_scores):
    print('')
    print('Code Breaker')
    print('Break the code! Guess the correct digets and you win!')
    print('----------------------')
    print('1. Single Player')
    print('2. Multiplayer')
    print('3. How-to-Play')
    print('4. High Scores')
    print('5. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')  

        if int(choice) == 1:
            CB(CB_high_scores)
        elif int(choice) == 2:
            CB_TWO()
        elif int(choice) == 3:
            CB_HTP()
        elif int(choice) == 4:
            CB_high(CB_high_scores)
        elif int(choice) == 5:
            CB_pickle_out(CB_high_scores)
            guessing()
        else:
            print('Please enter a valid option: ')

def CB(CB_high_scores):

    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    print('Choose the difficulty you want!')
    print('(Just a reminder, only option "3" can get you on the leaderboards!)')
    print('--------------------------------------')
    print('1. 3 Digit (Easy)')
    print('2. 4 Digit (Medium)')
    print('3. 5 Digit (Hard)')
    print('--------------------------------------')
    option = input('Enter option (1-3): ')
    while option != '1' and option != '2' and option != '3' and option.upper() != 'QUIT':
        option = input('Please input a valid option (1-3): ')
    print('')

    if str(option).upper() == 'QUIT':
        print('')
        CB_menu(CB_high_scores)

    testing = input('Are you testing? (Do you want to see the computer\'s choice?) Enter "y" or "n": ')
    while str(testing).upper() != 'Y' and str(testing).upper() != 'N' and str(testing).upper() == 'QUIT':
        testing = input('Please enter "y" or "n": ')
    print('')
    if str(testing).upper() == 'QUIT':
        print('')
        CB_menu(CB_high_scores)
    elif int(option) == 1:
        for x in range(1):
            number = random.randint(100,999)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        print('Break the 3 digit code: ')
        print('----------------------')
    elif int(option) == 2:
        for x in range(1):
            number = random.randint(1000,9999)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        print('Break the 4 digit code: ')
        print('----------------------')
    elif int(option) == 3:
        for x in range(1):
            number = random.randint(10000, 99999)
        if str(testing).upper() == 'Y':
            print('The number is: ' + str(number))
        print('Break the 5 digit code')
        print('----------------------')

    go = 'y'
    while (go != 'n'):
        count = 0
        correct = 0
        
        while correct == 0:
            if int(option) == 1:
                while True:
                    try:
                        guess = input('Enter a 3 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            elif int(option) == 2:
                while True:
                    try:
                        guess = input('Enter a 4 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            elif int(option) == 3:
                while True:
                    try:
                        guess = input('Enter a 5 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            
            list2 = []
            x = 0
            y = 0
            z = 0
            tree = 0
            stump = 0

            if str(option) == '1':
                if str(guess).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                elif len(str(guess2)) < 3 or len(str(guess2)) > 3:
                    print('3 digits only! Try again.')
                else :
                    while int(x) < 3:
                        list1 = [int(d) for d in str(number)]
                        x += 1
                    while int(y) < 3:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 3:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 3:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')
                
            elif str(option) == '2':
                if str(guess).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                elif len(str(guess2)) < 4 or len(str(guess2)) > 4:
                    print('4 digits only! Try again.')
                else :
                    while int(x) < 4:
                        list1 = [int(d) for d in str(number)]
                        x += 1
                    while int(y) < 4:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 4:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 4:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')
            
            elif str(option) == '3':
                if str(guess).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                elif len(str(guess2)) < 5 or len(str(guess2)) > 5:
                    print('5 digits only! Try again.')
                else :
                    while int(x) < 5:
                        list1 = [int(d) for d in str(number)]
                        x += 1
                    while int(y) < 5:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 5:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 5:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')
            
                
        count += 1
        print('')
        print('You win! You guess the numbers ' + str(number) + ' in ' + str(count) + str(endmessage))
        if int(option) == 3:
            name = input('Please enter your name: ')
            CB_high_scores.append((count, name))
        print('')
        pause = input('Enter any key to return to the menu... when you are ready!: ')
        time.sleep(1)
        CB_menu(CB_high_scores)

def CB_TWO():
    
    print('')
    print('Player 1 will pick the difficulty and the number.')
    print('Player 2 will be guessing.')
    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    print('Player 1, Choose the difficulty you want!')
    print('--------------------------------------')
    print('1. 3 Digit (Easy)')
    print('2. 4 Digit (Medium)')
    print('3. 5 Digit (Hard)')
    print('--------------------------------------')
    option = input('Enter option (1-3): ')
    while option != '1' and option != '2' and option != '3' and option.upper() != 'QUIT':
        option = input('Please input a valid option (1-3): ')
    print('')
    
    number = 0
    if str(option).upper() == 'QUIT':
        print('')
        CB_menu(CB_high_scores)
    elif int(option) == 1:
        while True:
            try:
                while len(str(number)) != 3 and str(number).upper() != 'QUIT':
                    number = input('Please enter a 3 digit code: ')
                number2 = str(number)
                number = int(number)
                break
            except:
                if str(number).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                else:
                    print('The code has to be a number.')
                    number = ''
            print('')

    elif int(option) == 2:
        while True:
            try:
                while len(str(number)) != 4 and str(number).upper() != 'QUIT':
                    number = input('Please enter a 4 digit code: ')
                    number2 = str(number)
                number = int(number)
                break
            except:
                if str(number).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                else:
                    print('The code has to be a number.')
                    number = ''
            print('')
    elif int(option) == 3:
        while True:
            try:
                while len(str(number)) != 5 and str(number).upper() != 'QUIT':
                    number = input('Please enter a 5 digit code: ')
                    number2 = str(number)
                number = int(number)
                break
            except:
                if str(number).upper() == 'QUIT':
                    print('')
                    CB_menu(CB_high_scores)
                else:
                    print('The code has to be a number.')
                    number = ''
            print('')
    
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('The code has been hidden.')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    if int(option) == 1:
        print('Break the 3 digit code: ')
        print('----------------------')
    elif int(option) == 2:
        print('Break the 4 digit code: ')
        print('----------------------')
    elif int(option) == 3:
        print('Break the 5 digit code')
        print('----------------------')

    go = 'y'
    while (go != 'n'):
        count = 0
        correct = 0
        
        while correct == 0:
            if int(option) == 1:
                while True:
                    try:
                        guess = input('Enter a 3 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            elif int(option) == 2:
                while True:
                    try:
                        guess = input('Enter a 4 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            elif int(option) == 3:
                while True:
                    try:
                        guess = input('Enter a 5 digit code: ')
                        guess2 = str(guess)
                        guess = int(guess)
                        break
                    except:
                        if str(guess).upper() == 'QUIT':
                            print('')
                            CB_menu(CB_high_scores)
                        else:
                            print('The code has to only include numbers.')
            list2 = []
            x = 0
            y = 0
            z = 0
            tree = 0
            stump = 0

            if str(guess).upper() == 'QUIT':
                print('')
                CB_menu(CB_high_scores)
            elif int(option) == 1:
                if len(str(guess2)) < 3 or len(str(guess2)) > 3:
                    print('3 digits only! Try again.')
                else :
                    while int(x) < 3:
                        list1 = [int(d) for d in str(number2)]
                        x += 1
                    while int(y) < 3:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 3:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 3:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')  
            elif int(option) == 2:
                if len(str(guess2)) < 4 or len(str(guess2)) > 4:
                    print('4 digits only! Try again.')
                else :
                    while int(x) < 4:
                        list1 = [int(d) for d in str(number2)]
                        x += 1
                    while int(y) < 4:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 4:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 4:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')
            elif int(option) == 3:
                if len(str(guess2)) < 5 or len(str(guess2)) > 5:
                    print('5 digits only! Try again.')
                else :
                    while int(x) < 5:
                        list1 = [int(d) for d in str(number2)]
                        x += 1
                    while int(y) < 5:
                        list2 = [int(d) for d in str(guess2)]
                        y += 1
                    
                    while int(z) < 5:
                        if list1[z] == list2[z]:
                            tree += 1
                        else :
                            stump += 1
                        z += 1
                    if tree == 5:
                        correct = 1
                    else :
                        print('')
                        print('Correct = ' + str(tree) + '  Wrong = ' + str(stump))
                        count += 1
                        if count < 2:
                            countmessage = ' guess.'
                            endmessage = ' try.'
                        else :
                            countmessage = ' guesses.'
                            endmessage = ' tries.'
                        print('You have made ' + str(count) + str(countmessage))
                        print('')
            
                
        count += 1
        print('')
        print('You win! You guess the numbers ' + str(number2) + ' in ' + str(count) + str(endmessage))
        print('')
        time.sleep(2)
        CB_menu(CB_high_scores)

def CB_HTP():
    print('')
    print('Code Breaker')
    print('Break the code! Guess the correct digits and you win!')
    print('----------------------')
    print('This is a simple game, yet can be frustrating indeed.')
    print('Your mission, if you choose to accept it, will be to decode the set of numbers.')
    print('You will need to type the code exactly how it is, number for number.')
    print('If you get a digit correct, you will be told so... You just won\'t know which digit it is... Good luck!')
    print('There are three levels. Only the hardest one will allow you to get on the high score list.')
    print('1. 3 Digit code. (Super simple... I hope...)')
    print('2. 4 Digit code. (A bit more challenging.')
    print('3. 5 Digit code. (This is frustrating.')
    print('This message will self-distruct in 5 seconds.')
    print('')
    back = input('Enter "1" to go back to the menu... There is no code to break... yet... : ')
    if back != '1':
        back = input('Okay, it seems you didn\'t believe me. Here is the code. One digit, in a range of... 1. Do your best...: ')
    
    while back != '1':
        back = input('Okay, this shouldn\'t even be challenging. You aren\'t even playing the game yet... Just type "1" to go back!: ')
    
    if back == '1':
        CB_menu(CB_high_scores)

def CB_high(CB_high_scores):
    print('')
    print('HIGH SCORES')
    print('------------------------')
    CB_high_scores.sort(reverse = False)
    for score, name in CB_high_scores:
        print("{{name:>{col_width}}} | {{score:<{col_width}}}".format(col_width=(5-3)//2).format(name=name, score=score))
    print('')
    pause = input('Enter any key to return to the menu: ')
    print('')
    CB_menu(CB_high_scores)

def CB_pickle_in():
    try:
        in_file = open('CB_high_scores.txt', 'rb')
        CB_high_scores = pickle.load(in_file)
    except IOError:
        in_file = open('CB_high_scores.txt', 'w')
        CB_high_scores = []

    return CB_high_scores

def CB_pickle_out(CB_high_scores):
    save_file = open('CB_high_scores.txt','wb')
    pickle.dump(CB_high_scores, save_file)
    save_file.close()

#Hang-man
def HM_menu():
    print('')
    print('Hang-man')
    print('Guess the word that fills in the blanks! ')
    print('----------------------')
    print('1. Single Player')
    print('2. How-to-Play')
    print('3. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')  

        if int(choice) == 1:
            HM()
        elif int(choice) == 2:
            HM_HTP()
        elif int(choice) == 3:
            guessing()
        else:
            print('Please enter a valid option: ')

def HM():
    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    print('Choose the difficulty you want!')
    print('--------------------------------------')
    print('1. 10 Mistakes (Easy)')
    print('2. 8 Mistakes (Medium)')
    print('3. 6 Mistakes (Hard)')
    print('--------------------------------------')
    option = input('Enter option (1-3): ')
    while option != '1' and option != '2' and option != '3' and option.upper() != 'QUIT':
        option = input('Please input a valid option (1-3): ')
    print('')
    if option.upper() == 'QUIT':
        HM_menu()

    testing = input('Are you testing? (Do you want to see the computer\'s choice?) Enter "y" or "n": ')
    while str(testing).upper() != 'Y' and str(testing).upper() != 'N' and str(testing).upper() != 'QUIT':
        testing = input('Please enter "y" or "n": ')
    print('')
    if testing.upper() == 'QUIT':
        HM_menu()

    wordlist = ['secret', 'football', 'baseball', 'soccer', 'through', 'whisper', 'garentee', 'fighter', 'driver', 'wrestler']
    guesses = ''
    for x in range(1):
        number = random.randint(1,10)
    number -= 1
    word = wordlist[number]
    
    if int(option) == 1:
        turns = 10
    elif int(option) == 2:
        turns = 8
    elif int(option) == 3:
        turns = 6

    while turns > 0:  
        print('Letters guessed: ')
        print(guesses)
        print('----------------------')
        failed = 0              
        for char in word:      
            if char in guesses:    
                print(char)  
            else:
                print("_")     
                failed += 1    

        if failed == 0:        
            print("You won")
            break     

        print('Your word has ' + str(len(word)) + ' many letters in it!') 
        print("Remaining guesses: " + str(turns)) 
        if str(testing).upper() == 'Y':
            print('Testing: ' + word)        
        print('')
        
        
        guess = input("Guess a character: ")
        if guess.upper() == 'QUIT':
            HM_menu()
        while len(guess) != 1:
            guess = input('Please guess no more than one character: ')
            if guess.upper() == 'QUIT':
                HM_menu()
        
        if guess.upper() == 'QUIT':
            HM_menu()
            
        guesses += guess
        if guess not in word:  
            turns -= 1        
            print("Wrong")    
            print('')
            if turns == 0:           
                print("You Loose! Better luck next time!")
                print('Your word was: ' + str(word))
    time.sleep(1)
    HM_menu()

def HM_HTP():
    print('')
    print('Hang-man')
    print('Guess the word that fills in the blanks! ')
    print('----------------------')
    print('The game were you kill someone if you are not careful!')
    print('Not really... we don\'t hang anyone in this game...')
    print('However, you do have to guess what the word is, letter by letter.')
    print('But be careful! If you guess a letter than isn\'t in the word, you lose a "Life" (They are called "Mistakes" in here, but let\'s just move on...)')
    print('There are three levels.')
    print('1. 10 Mistakes. (That is about 40% of the alphabet!)')
    print('2. 8 Mistakes. (A bit less room for error.)')
    print('3. 6 Mistakes. (You better know how to play this game, otherwise I\'ll have to say sorry...)')
    print('')
    back = input('Enter "1" to go back to the menu. Not a letter, this isn\'t part of the game.: ')
    if back != '1':
        back = input('Okay, it seems you think this is funny... Well, I will have you know I will choose the hardest words for you! So, try again.: ')
    
    while back != '1':
        back = input('This isn\'t even hard. If you want something hard, just play the games. Only geniuses can complete these... Try again!: ')
    
    if back == '1':
        HM_menu()

#Impossible Game
def IG_menu():
    print('')
    print('The Impossible Game')
    print('I think you can win one of these times! ')
    print('----------------------')
    print('1. Single Player')
    print('2. How-to-Play')
    print('3. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')  

        if int(choice) == 1:
            IG()
        elif int(choice) == 2:
            IG_HTP()
        elif int(choice) == 3:
            competetive()
        else:
            print('Please enter a valid option: ')

def IG():   
    keep = 1
    print('')
    print('To exit, enter "Quit" at any time to leave the game.')
    print('Remember that what ever progress you had will be lost.')
    print('')
    while int(keep) == 1:
        while True:
            try:
                choice = input('Enter any number (1 or Higher!): ')
                choice = int(choice)
                print('')
                break
            except:
                if str(choice).upper() == 'QUIT':
                    print('')
                    IG_menu()
                else:
                    print('Not a valid option.')   
        
        if int(choice) > 0:
            mychoice = choice + 1
            print('Your number: ' + str(choice))
            print('My number:   ' + str(mychoice))
            print('You lose!!!!!! Better luck next time!!!!! ')
            time.sleep(1.5)
            IG_menu()
        else:
            print('Your number has to be greater than 0!')
            print('') 

def IG_HTP():
    print('')
    print('The Impossible Game')
    print('I think you can win this game one of these times! ')
    print('----------------------')
    print('No one knows where this game originated from...')
    print('Personally, I like the tale of the peasant and the king.')
    print('     You see, long ago, there was a farmer. He was one of the farmer who grew the crops that fed the')
    print('kingdom of Varthen. The king was... cruel... to say the least. He thought that all the food that ')
    print('grew in the kingdom was his to have, regardless of the farmers wishes. So, he ordered his soldiers')
    print('to take all the food the farmers grew. This upset the farmers. One, whose name is remembered as Petani,')
    print('went to the king. He asked the king to pay for the food he took. The king was upset by this, that the peasant')
    print('was demanding money for what was the kings. The king said, "I will do no such thing. This kingdom is mine,')
    print('which means the food is as well." ')
    print('     Now, the king was known to be great at games. Chess, Checkers, or any other game there was. The King ')
    print('was the greatest at all of them. It was writen that the king beat three separate people at the same time, all')
    print('playing different games. The peasant, knowing this, said to the king, "Oh great king, my skill at this game ')
    print('is superior to yours. And I will play a game of it against you to prove it. So the king, who\'s pride was')
    print('hurt, decided to accept this challenge. ')
    print('     The king decided that if he were to lose, he would pay double the worth of the crops to the farmers for')
    print('the rest of his life. But if the king won, the farmers would give their food willingly to the king, forever.')
    print('The peasant agreed, with one condition. That he, the peasant, would pick the game. The king agreed.')
    print('     The game would happen in the kingdom\'s arena. The king and peasant both approached the table in the ')
    print('middle of the arena. The king sat in a throne, while the peasant sat in a wooden chair. The king asked, ')
    print('"What is the game you have chosen?" And the peasant replied, "Pick a number, 1-through-10. After you pick, I')
    print('will pick a number. Who ever has the higher number wins." The King thought to himself for a few minutes, and')
    print('decided to go with the number 10. The peasant, stands up, and says, "11. I win." The King proclaimed that the ')
    print('peasant needed to pick a number 1-through-10. The peasant replied, "That was the rule for you, while I could ')
    print('choose any number I wanted." The king stood up and proclaimed the peasant to be a cheater. However, the judges')
    print('who were present said the peasant did no such thing. The king... lost...')
    print('     The story continues with the farmers becoming so wealthy that they increase their farms to stretch for')
    print('hundreds of miles. The kingdom grew and the king became more wealthy and powerful, while paying the farmser')
    print('like he agreed too. This farmer, Petani, became the first peasant to be welcomed in the court of the king.')
    print('The kingdom continued to grow...')
    print('-----------------------------------------------------------------------------------')
    print('This game is simple. Pick a number, any number, and then I will pick a number.')
    print('I am sure if you play this game enough, you will understand how this game works.')
    print('Best of luck!')
    print('')
    back = input('Enter "1" to go back to the menu. Not any number... This isn\'t the game yet.: ')
    while back != '1':
        back = input('I just said this isn\'t the game yet! Enter "1" to go back!: ')
    
    if back == '1':
        IG_menu()

#Highest Roll
def HR_menu():
    print('')
    print('Highest Roll')
    print('Try and get the highest roll! ')
    print('----------------------')
    print('1. Single Player')
    print('2. How-to-Play')
    print('3. Back')
    
    keep = 1
    while int(keep) == 1:
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('')
                break
            except:
                print('Not a valid option!!!')
                print('')  

        if int(choice) == 1:
            HR()
        elif int(choice) == 2:
            HR_HTP()
        elif int(choice) == 3:
            competetive()
        else:
            print('Please enter a valid option: ')

def HR():
    min = 1
    max = 6
    cont = 'y'

    time.sleep(1)

    while str(cont).upper() == 'Y':
        print('Your values:')
        number1 = random.randint(min, max)
        number2 = random.randint(min, max)
        number3 = number1 + number2
        print(str(number1) + ' + ' + str(number2) + ' = ' + str(number3))
        time.sleep(1)
        print('')
        print('My values:')
        number4 = random.randint(min, max)
        number5 = random.randint(min, max)
        number6 = number4 + number5
        print(str(number4) + ' + ' + str(number5) + ' = ' + str(number6))
        print('')
        time.sleep(1)

        if(int(number3) > int(number6)):
            print('--Yours----Mine--')
            print('   ' + str(number3) + '   >   ' + str(number6))
            print('You win!!!')
            print('')
        elif(int(number3) < int(number6)):
            print('--Mine----Yours--')
            print('   ' + str(number6) + '   >   ' + str(number3))
            print('Haha, you lose!')
            print('')
        else :
            print('')
            print('--Yours----Mine--')
            print('   ' + str(number3) + '   ==  ' + str(number6))
            print('We tied! Let\'s try again!')

        if(int(number3) == int(number6)):
            print('')
            time.sleep(1)
        else:
            cont = input('Shall we go again? (Type "y" to continue, or any other key to quit.: ')
            print('')
    HR_menu()

def HR_HTP():
    print('')
    print('Highest Roll')
    print('Try and get the highest roll! ')
    print('----------------------')
    print('This is a simple game.')
    print('Roll two dice, try and get a higher score than your opponent. That opponent being me, the computer.')
    print('Just a simple game of luck... but for me, it is all skill... Unless I lose. Then you probably cheated.')
    print('')
    back = input('Enter "1" to go back to the menu. But please remember, I\'ll be number 1 in this game.: ')
    while back != '1':
        back = input('Seeing how you typed something other than 1, you obviously agree! Try again!: ')
    
    
    if back == '1':
        HR_menu()



#Start of the game system
RPS_high_scores = []
RPS_high_scores = RPS_pickle_in()

GTN_high_scores = []
GTN_high_scores = GTN_pickle_in()

CB_high_scores = []
CB_high_scores = CB_pickle_in()

menu()