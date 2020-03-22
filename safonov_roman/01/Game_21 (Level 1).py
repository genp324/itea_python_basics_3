player_score = int(0)

answer = str('')
another_try = str ('')
invitation = str ('')
shut_down = False

from random import randint

while shut_down == False:

        player_score = randint (2,11)

        while answer != 'Pick' or answer != 'Pass':

            answer = input (f'Player, you have {player_score} points. \nPick or Pass ? ')
                        
            if answer == 'Pick':
                player_score += randint (2,11)
                if player_score > 21: break
                
            elif answer == 'Pass':
                break
            
            elif answer != 'Pick' and answer != 'Pass':
                print('enter "Pick" or "Pass": ')

        if player_score == 21: print (f'Your score is {player_score}. You won')
        if player_score != 21: print (f'Your score is {player_score}. You loose')
        

        another_try = input ('Do you want to try again (Y/N) ?')
        while another_try != 'Y' and another_try != 'N':
                
            if another_try != 'Y' and another_try != 'N':
                another_try = input ('enter "Y" or "N":')
        if another_try == 'N': shut_down = True

  
"""
while invitation != 'Y':

    invitation = input ('Start the Game?\n (Please answer Y/N):')
    
    if invitation == 'N':
        
        break

    else: print ('Please answer "Y" or "N"')
    
print ('Buy! See you next time')
"""


       
