#!/usr/bin/python3
'''
Task 1 - Game 21

Create a game - 21.
There are 10 cards representing values 2-11.
The goal is to get max points, but less then 21. Each turn a player should decide pick a new card o pass.
Pick - value of a card should be added to player's points. If player gets more then 21 points - he lost.
Pass - no new cards, player stays with current points.
Results should be shown only after all the players passed.

Level 1 - one player.
Level 2 - one player + one bot.
Level 3 - one player + two bots.

To generate a random card use:
# Import function randint from module random
from random import randint

# Usage example
randint(2, 11)
'''
from random import randint

print ("Welcome to game 21!")
print ("Choose level")
print ("Level 1: One Player Game")
print ("Level 2: One Player One Bot")
print ("Level 3: One Player Two Bots")

level = 0

while True:
    level = int (input ("Please, input level:"))
    if level < 1 or level > 3:
        print  ("Wrong choice, please try again...")
        continue
    break

print ("You have choosen to play level ",level,"Let's rock")

if level == 1:
    print ("In this level, you must have 18,19,20 or 21 points or you will loose")
    userscore = 0
    attempt = 0
    choice = 0

    input ("Pess ENTER to continue")

    attempt = randint(2,11)
    userscore += attempt

    print ("You getting two cards, the fist one is", attempt) 
    attempt = randint(2,11)

    input ("Pess ENTER to continue")
    if attempt == 11 and userscore == 11:
        prtint ("Unbelievelly you have achived two 11 in the row. You WON THIS MATCH!!!")
    else:
        userscore += attempt
        print ("The second one is", attempt, " so you have totally", userscore,"scores")
        input ("Pess ENTER to continue")

        while True:
            if userscore > 21:
                print ("Sorry, but you loose with your last attempt", attempt, "and scores", userscore)
                break;
            if userscore >= 18 and userscore <= 21:
                print ("You WiN with", userscore,"scores. Congrats!!!")
                break;
            print ("Now you have", userscore, "scores")
            choice = int (input ("Do you want to continue? YES-1 NO-0:"))
            if choice != 1:
                print ("You have choosen to end game having only", userscore, "so you loose this game without a fight!")
                break
            attempt = randint(2,11)
            print ("Next card is", attempt)
            userscore += attempt

if level == 2:

        print ("In this game you will play with one bot. First BOT makes choices, than you")
        print ("If BOT gets more than 21 you wont know this until you end the game")
        print ("Now Bot starts and gets his two first cards")
        input ("Pess ENTER to continue")
    
        userscore = 1
        bot1score = 0
        attempt = 0
        choice = 0

        attempt = randint(2,11)
        bot1score += attempt

        attempt = randint(2,11)
        bot1score += attempt


        while True:
            if bot1score > 17:
                print ("Bot thinks that he is done. So you can play now.")
                input ("Pess ENTER to continue")
                break
            print ("Bot thinks that that he wants one more card")
            attempt = randint(2,11)
            bot1score += attempt
            input ("Pess ENTER to continue")

        print ("Now you getting two cards one by one")
        input ("Pess ENTER to continue")
        attempt = randint(2,11)
        userscore += attempt

        print ("Your first card is:", attempt)
        input ("Pess ENTER to continue")
        attempt = randint(2,11)
        userscore += attempt

        print ("Your second card is:", attempt)
        input ("Pess ENTER to continue")

        if userscore == 22:
            print ("You GET 22 scores and WIN this MATCH!")
        else:
            while True:
                if userscore > 21:
                    print ("Ups... Seems you have more than 21")
                    break
                print ("Now you have", userscore, "scores")
                choice = int (input ("Do you want to continue? YES-1 NO-0:"))
                if choice != 1:
                    break
                attempt = randint(2,11)
                userscore += attempt
                print("This attempt gives you", attempt, "scores")
            print ("Game was finished, let's check results:")
            input ("Pess ENTER to continue")
            print ("Your scores are", userscore)
            input ("Pess ENTER to continue")
            print ("Bot scores are", bot1score)
            input ("Pess ENTER to continue")
    
            if userscore > 21 and bot1score <= 21:
                print ("YOU LOOSE")
            elif bot1score > 21 and userscore <= 21: 
                print ("YOU WIN")
            elif userscore > bot1score and userscore <= 21: 
                print ("YOU WIN")
            elif userscore < bot1score and userscore > 21:
                print ("YOU WIN")
            elif userscore == bot1score:
                print ("DRAW")
            else:
                print ("YOU LOOSE")
                
if level == 3:

        print ("In this game you will play with two bots. First BOTs make choices, than you")
        print ("If BOTs get more than 21 you wont know this until you end the game")
        print ("Now Bots start and get their two first cards")
        input ("Pess ENTER to continue")
    
        userscore = 1
        bot1score = 0
        bot2score = 0
        attempt = 0
        choice = 0

        attempt = randint(2,11)
        bot1score += attempt

        attempt = randint(2,11)
        bot1score += attempt

          
        attempt = randint(2,11)
        bot2score += attempt

        attempt = randint(2,11)
        bot2score += attempt


        while True:
            if bot1score > 17:
                print ("Bot one thinks that he is done. So bot 2 starts to play.")
                input ("Pess ENTER to continue")
                break
            print ("Bot one thinks that that he wants one more card")
            attempt = randint(2,11)
            bot1score += attempt
            input ("Pess ENTER to continue")

        while True:
            if bot2score > 17:
                print ("Bot two thinks that he is done. So you can play now.")
                input ("Pess ENTER to continue")
                break
            print ("Bot two thinks that that he wants one more card")
            attempt = randint(2,11)
            bot2score += attempt
            input ("Pess ENTER to continue")

        print ("Now you getting two cards one by one")
        input ("Pess ENTER to continue")
        attempt = randint(2,11)
        userscore += attempt

        print ("Your first card is:", attempt)
        input ("Pess ENTER to continue")
        attempt = randint(2,11)
        userscore += attempt

        print ("Your second card is:", attempt)
        input ("Pess ENTER to continue")

        if userscore == 22:
            print ("You GET 22 scores and WIN this MATCH!")
        else:
            while True:
                if userscore > 21:
                    print ("Ups... Seems you have more than 21")
                    break
                print ("Now you have", userscore, "scores")
                choice = int (input ("Do you want to continue? YES-1 NO-0:"))
                if choice != 1:
                    break
                attempt = randint(2,11)
                userscore += attempt
                print("This attempt gives you", attempt, "scores")
            print ("Game was finished, let's check results:")
            input ("Pess ENTER to continue")
            print ("Your scores are", userscore)
            input ("Pess ENTER to continue")
            print ("Bot one scores are", bot1score)
            input ("Pess ENTER to continue")
            print ("Bot two scores are", bot2score)
            input ("Pess ENTER to continue")


            if userscore > 21 and bot1score <= 21:
                print ("YOU LOOSE BOT ONE")
            elif bot1score > 21 and userscore <= 21: 
                print ("YOU WIN BOT ONE")
            elif userscore > bot1score and userscore <= 21: 
                print ("YOU WIN BOT ONE")
            elif userscore < bot1score and userscore > 21:
                print ("YOU WIN BOT ONE")
            elif userscore == bot1score:
                print ("DRAW WITH BOT ONE")
            else:
                print ("YOU LOOSE BOT ONE")

            input ("Pess ENTER to continue")

            if userscore > 21 and bot2score <= 21:
                print ("YOU LOOSE BOT TWO")
            elif bot2score > 21 and userscore <= 21: 
                print ("YOU WIN BOT TWO")
            elif userscore > bot2score and userscore <= 21: 
                print ("YOU WIN BOT TWO")
            elif userscore < bot2score and userscore > 21:
                print ("YOU WIN BOT TWO")
            elif userscore == bot2score:
                print ("DRAW WITH BOT TWO")
            else:
                print ("YOU LOOSE BOT TWO")
