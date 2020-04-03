player_score = int(0)
b1_score = int (0)

p_answer = str('')
b1_answer = str('')
end_round = False
p_turn_end = False
b1_turn_end = False
p_done = False
b1_done = False
another_try = str ('')
invitation = str ('')
shut_down = False

from random import randint

invitation = input ('Start the Game (Y/N)? ')

while invitation != 'Y' and invitation != 'N':
    invitation = input ('Please answer "Y" or "N": ')

if invitation == 'N':
    print (' Come again later !')
    shut_down = True

print ('')

while shut_down == False:

    player_score = 0
    b1_score = 0
    p_turn_end = False
    b1_turn_end = False
    end_round = False

    player_score = randint (2,11)
    b1_score = randint (2,11)

    while end_round == False:
            
            while p_turn_end == False and p_done == False and end_round == False:

                p_answer = input (f'Player, you have {player_score} points. \nPick or Pass ? ')

                while p_answer != 'Pick' and p_answer != 'Pass':
                    p_answer = input ('enter "Pick" or "Pass": ')
                
                if p_answer == 'Pick':
                    player_score += randint (2,11)
                    p_turn_end = True
                    if player_score > 21:
                        end_round = True
                                                         
                elif p_answer == 'Pass':
                    p_done = True
                                 
                if player_score == 21:
                    end_round = True
                if player_score > 21:
                    end_round = True

                                        
            while end_round == False and b1_done == False and b1_turn_end == False:

                if b1_score <= 15:
                    b1_answer = 'Pick'
                else:
                    b1_answer = 'Pass'

                if b1_answer == 'Pick':
                    b1_score += randint (2,11)
                    b1_turn_end = True
                        
                elif b1_answer == 'Pass':
                    b1_done = True
                        
                if b1_score == 21:
                    end_round = True
                if b1_score > 21:
                    end_round = True
    
            p_turn_end = False
            b1_turn_end = False


            if p_done == True and b1_done == True:
                end_round = True

    print (f'   Player scored {player_score} points. \n   Bot_1 scored {b1_score} points.')

    if player_score == b1_score or (player_score > 21 and b1_score > 21):
        print ('friendship wins')
        end_round = True
                    
    elif player_score > 21 and b1_score <= 21:
        i = randint (1,10)
        if i <= 7:
            print ('Bot_1 wins this round')
        elif 8 <= i <= 9:
            print ("Grid is the sin ! That's why you loose" )     
        elif i == 10:
            print ("Looser !" )     
        end_round = True

    elif player_score <= 21 and b1_score > 21:
        print ('Player wins this round. Congratulations !')
        end_round = True

    elif 21 - b1_score > 0 and 21 - player_score > 0 and 21 - b1_score < 21 - player_score:
        print ('Bot_1 wins this round')
        end_round = True

    else:
        print ('Player wins this round. Congratulations !')
        end_round = True       

    another_try = input ('Do you want to try again (Y/N) ?')

    while another_try != 'Y' and another_try != 'N':
                        
        another_try = input ('enter "Y" or "N":')
                    
    if another_try == 'N': shut_down = True
    else:
        print ('')
        p_turn_end = False
        p_done = False
        b1_turn_end = False
        b1_done = False

    if shut_down == True:
        print ('Buy! See you next time.')

  


       
