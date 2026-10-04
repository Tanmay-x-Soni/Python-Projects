import random
import sys
import art
import os

cards = [11 , 2 , 3 , 4, 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]


def score_calculator(cards):

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    score = 0
    for num in cards:
        score += num
    return score

def check_score(user_score, computer_score):
    if user_score == 21:
        print(f" YOU WIN WITH A BLACK JACK \U0001F60E \nYour score is {user_score} ")
        return False
    elif user_score > 21:
        print(f"It is a bust !! You went over \U0001F622 , your score is {user_score}")
        return False
    elif computer_score>21:
        print(f"Computer's score is {computer_score} \n")
        return False

def cards_generator(Cards_in_hand):
    Cards_in_hand.append(random.choice(cards))
    return Cards_in_hand
        
def show_cards(user_cards , user_score , computer_cards , computer_score):
    print(f"\nYour cards : {user_cards} , Total score is {score_calculator(cards=user_cards )}")
    if len(computer_cards) <=1:
        print(f"\n Computer's first card : {computer_cards}")
    else:
        print(f" \n Your final hand : {user_cards} , final score {score_calculator(cards=user_cards)}")
        print(f"  Computer's final hand : {computer_cards} , final score {score_calculator(cards=computer_cards)}")


def win_or_lose(user_score, computer_score):
    if computer_score > 21:
        print("\n   -----------YOU WIN!!-----------")

    elif user_score > 21:
        print("\n   -----------YOU LOSE!!-----------")

    elif user_score > computer_score:
        print("\n   -----------YOU WIN!!-----------")

    elif computer_score > user_score:
        print("\n   -----------YOU LOSE!!-----------")

    elif user_score == computer_score:
        print("\n   -----------It's a DRAW! \U0001F601-----------")


def program():

    user_cards = [random.choice(cards) , random.choice(cards)]
    computer_cards = [random.choice(cards)]

    user_score = 0
    computer_score = 0

    running = True
    retry = True

    while running == True:
        user_score = score_calculator(cards=user_cards )
        computer_score = score_calculator(cards=computer_cards )
        show_cards(user_cards = user_cards , user_score = user_score , computer_cards = computer_cards , computer_score = computer_score)
        if check_score(user_score=user_score ,computer_score=computer_score) == False:
            running = False
            break
        else:
            while retry == True:
                next_card = input("Type 'y' to get another card , Type 'n' to pass. ").lower()
                if next_card == 'y':
                    user_cards = cards_generator(Cards_in_hand=user_cards)
                    user_score = score_calculator(cards=user_cards)
                    show_cards(user_cards = user_cards , user_score = user_score , computer_cards = computer_cards , computer_score = computer_score)
                    if check_score(user_score=user_score ,computer_score=computer_score) == False:
                        running=False
                        break
                    
                elif next_card == 'n':
                    retry = False
                    while computer_score <16:
                        computer_cards = cards_generator(Cards_in_hand=computer_cards)
                        computer_score = score_calculator(cards=computer_cards)
                    show_cards(user_cards = user_cards , user_score = user_score , computer_cards = computer_cards , computer_score = computer_score)
                    running = False
                    if check_score(user_score=user_score ,computer_score=computer_score) == False:
                        running = False
                        break
                else:
                    print(" Invalid input! , try again")

    win_or_lose(user_score = user_score , computer_score = computer_score) 

game = True
while game == True:
    
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    os.system('cls')
    if start == 'y':  
        print(art.logo)
        program()
    elif start == 'n':
        break 
    else:
        sys.exit()
                            
                
