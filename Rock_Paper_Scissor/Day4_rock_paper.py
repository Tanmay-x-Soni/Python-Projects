import random
import sys

Rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)'''

Paper ='''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)'''

Scissors ='''
      _______
  ---'   ____)____
            ______)
         __________)
         (____)
  ---.__(___)'''


Choice = [Rock , Paper , Scissors]
computer_2=["Rock" , "Paper" , "Scissors"]
computer_choice = random.randint(0,2)

print("\n Welcome to Rock Papper Scissors!!")
user = int(input("\n Type 0 for 'rock'  1 for 'papper' , 2 for 'scissors'.\n"))

if user > 2 or user < 0 or computer_choice < 0 or computer_choice > 2 :
    print("   You typed an invalid number. Try Again :) \n ")
    sys.exit()  # will exit the entire program , like exit()  or die() function.

    
print(f"\n {Choice[computer_choice]} \n\n  Computer chose {computer_2[computer_choice]}. \n")


# (user - computer choice) 0 - 2 /  1 - 0 / 2 - 1  == win 

print(f"{Choice[user]}\n\n")


if user == 0  and computer_choice == 2 :
    print("  You win!\n")
elif user == 1 and computer_choice == 0 :
    print("  You win!\n")
elif user == 2 and computer_choice == 1 :
    print("  You win!\n")
elif user == computer_choice:
    print("   Draw :) \n ")
else:
    print("  You Lose :( \n")

