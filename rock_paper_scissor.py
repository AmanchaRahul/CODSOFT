# Rock-Paper-Scissors Game
# TASK 4


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
gestures=["rock","paper","scissors"]


game_running=True



while game_running:
   
      
    user_choice=int(input("enter '0' for rock, '1' for paper, '2' for scissors: "))
    
    if user_choice >= 0 and user_choice <= 2:
        
        
       print("you have selected:",gestures[user_choice], game_images[user_choice])
    
    
    
       computer_choice=random.randint(0,2)
       print("computer have selected:",gestures[computer_choice],game_images[computer_choice])

       if user_choice==computer_choice:
        print("it's a tie!")
        game_running=False
        
       elif user_choice==0 and computer_choice==2:
        print("you won!")
        game_running=False
        
       elif user_choice==2 and computer_choice==1:
        print("you won!")
        game_running=False
        
       elif user_choice==1 and computer_choice==0:
        print("you won!")
        game_running=False
        
       else:
        print("you lose!")
        game_running=False
    
       print("\n")
       opinion=input("Do you want to Play Again? yes or no: ")
       if opinion=="yes":
         game_running=True
       elif opinion=="no":
        game_running=False
       print("\n")
        
    else:
        print("Invalid User input!")
        game_running=False
        
        
        
