from random import randint

game_on = True

#first_bot

first_bot_a = randint (2, 11)
first_bot_b = randint (2, 11)
first_bot_c = randint (2, 11)
first_bot_d = randint (2, 11)
first_bot_e = randint (2, 11)

first_bot_another = randint(1, 2)

if first_bot_another == 1:
    
    first_bot_another2 = randint(1, 2)

    if first_bot_another2 == 1:

        first_bot_another3 = randint(1, 2)

        if first_bot_another3 == 1:

            first_bot_result = first_bot_a + first_bot_b + first_bot_c + first_bot_d + first_bot_e

        elif first_bot_another3 == 2:
            
            first_bot_result = first_bot_a + first_bot_b + first_bot_c + first_bot_d

    elif first_bot_another2 == 2:
    
        first_bot_result = first_bot_a + first_bot_b + first_bot_c

elif first_bot_another == 2:
    
    first_bot_result = first_bot_a + first_bot_b


#second_bot

second_bot_a = randint (2, 11)
second_bot_b = randint (2, 11)
second_bot_c = randint (2, 11)
second_bot_d = randint (2, 11)
second_bot_e = randint (2, 11)

second_bot_another = randint(1, 2)

if second_bot_another == 1:
    
    second_bot_another2 = randint(1, 2)

    if second_bot_another2 == 1:

        second_bot_another3 = randint(1, 2)

        if second_bot_another3 == 1:

            second_bot_result = second_bot_a + second_bot_b + second_bot_c + second_bot_d + second_bot_e

        elif second_bot_another3 == 2:
            
            second_bot_result = second_bot_a + second_bot_b + second_bot_c + second_bot_d

    elif second_bot_another2 == 2:
    
        second_bot_result = second_bot_a + second_bot_b + second_bot_c

elif second_bot_another == 2:
    
    second_bot_result = second_bot_a + second_bot_b


#user

while game_on:
    a = randint (2, 11)
    b = randint (2, 11)
    c = randint (2, 11)
    d = randint (2, 11)
    e = randint (2, 11)
    print("You have two cards. On the first the number is", a)
    print("On the second the number is", b)
    print("Sum of your cards is", a + b)

    another = input("Another one?(y/n) ")

    if another == "y":
        
        print(f"You got a {c} card")
        print("The sum now is", a + b + c)

        if a + b + c <= 21:
            another2 = input("Another one?(y/n) ")

            if another2 == "y":
            
                print(f"You got a {d} card")
                print("The sum now is", a + b + c + d)

                if a + b + c + d <= 21:
                    another3 = input("Another one?(y/n) ")

                    if another3 == "y":
                        
                        print(f"You got a {e} card")
                        print("The sum now is", a + b + c + d + e)

                        if a + b + c + d + e == 21:
                            
                            print("You won. Congrats")
                            
                        elif a + b + c + d + e < 21:
                            
                            print(f"You have {a + b + c + d + e} points. Let's see what your opponents have.")
                            print("First opponent have", first_bot_result, "points")
                            print("Second opponent have", second_bot_result, "points")
                            if (a + b + c + d + e > first_bot_result  or first_bot_result > 21) and (a + b + c + d + e > second_bot_result or second_bot_result > 21):
                                
                                  print("You won. Congrats")
                                  
                            elif a + b + c + d + e == first_bot_result == second_bot_result:
                                
                                  print("Draw. Try again")
                                  
                            else:
                                print("You lost. Try again")
                        else:
                            print("You lost. Try again")

                    elif another3 == "n":
                        
                        if a + b + c + d == 21:
                            
                            print("You won. Congrats")
                            
                        elif a + b + c + d < 21:
                            
                            print(f"You have {a + b + c + d} points. Let's see what your opponents have.")
                            print("First opponent have", first_bot_result, "points")
                            print("Second opponent have", second_bot_result, "points")
                            if (a + b + c + d > first_bot_result  or first_bot_result > 21) and (a + b + c + d > second_bot_result or second_bot_result > 21):
                                
                                  print("You won. Congrats")
                                  
                            elif a + b + c + d == first_bot_result == second_bot_result:
                                
                                  print("Draw. Try again")
                                  
                            else:
                                print("You lost. Try again")
                        else:
                            print("You lost. Try again")
                else:
                    print("You lost. Try again")
                    
            elif another2 == "n":
            
                if a + b + c == 21:
                    
                    print("You won. Congrats")
                    
                elif a + b + c < 21:
                    
                    print(f"You have {a + b + c} points. Let's see what your opponents have.")
                    print("First opponent have", first_bot_result, "points")
                    print("Second opponent have", second_bot_result, "points")
                    if (a + b + c > first_bot_result  or first_bot_result > 21) and (a + b + c > second_bot_result or second_bot_result > 21):
                        
                        print("You won. Congrats")
                        
                    elif a + b + c == first_bot_result == second_bot_result:
                        
                        print("Draw. Try again")
                        
                    else:
                        print("You lost. Try again")
                else:
                    print("You lost. Try again")
        else:
            print("You lost. Try again")
    elif another == "n":
        
        if a + b == 21:
            
            print("You won. Congrats")
            
        elif a + b < 21:
            
            print(f"You have {a + b} points. Let's see what your opponents have.")
            print("First opponent have", first_bot_result, "points")
            print("Second opponent have", second_bot_result, "points")
            if (a + b > first_bot_result or first_bot_result > 21)  and (a + b > second_bot_result or second_bot_result > 21):
                
                print("You won. Congrats")
                
            elif a + b == first_bot_result == second_bot_result:
                
                print("Draw. Try again")
                
            else:
                print("You lost. Try again")
        else:
            print("You lost. Try again")
            
    again = input("Let`s play again? (y/n)")
    if again == "n":
        print("----------GAME_OVER----------")
        game_on = False
    else:
        print("----------NEW_GAME----------")
    






