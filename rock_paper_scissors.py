    
#!/usr/bin/env python
# coding: utf-8

# ##### How to play Rock Paper Scissors

# In[3]:


import random

user_choice = ""

user_score = 0

computer_score = 0

while user_choice.upper() != "QUIT":
    
    #  get user choice
    user_choice = input()

    #  get computer choice
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_choice = "rock"
    if random_number == 2:
        computer_choice = "paper"
    if random_number == 3:
        computer_choice = "scissors"
    #  evaluate outcome; User_Choice=Rock/Paper/Scissors and Computer_Choice=Rock/Paper/Scissor, then declare winner

    #  computer chooses rock

    if computer_choice == "rock" and user_choice.lower() == "rock":
        print ("Computer chooses rock. TIE!")
    
    if computer_choice == "rock" and user_choice.lower() == "paper":
        print ("Computer chooses rock. Paper covers rock! User wins!")
    
    if computer_choice == "rock" and user_choice.lower() == "scissors":
        print ("Computer chooses rock. Rock crushes scissors! Computer wins!")

    #  computer chooses paper

    if computer_choice == "paper" and user_choice.lower() == "rock":
        print ("Computer chooses paper. Paper covers rock! Computer wins!")
    
    if computer_choice == "paper" and user_choice.lower() == "paper":
        print ("Computer chooses paper. TIE!")
    
    if computer_choice == "paper" and user_choice.lower() == "scissors":
        print ("Computer chooses paper. Scissors cut paper! User wins!")
    
    #  computer chooses scissors

    if computer_choice == "scissors" and user_choice.lower() == "rock":
        print ("Computer chooses scissors. Rock crushes scissors! User wins!")
    
    if computer_choice == "scissors" and user_choice.lower() == "paper":
        print ("Computer chooses scissors. Scissors cut paper! Computer wins!")

    if computer_choice == "scissors" and user_choice.lower() == "scissors":
        print ("Computer chooses scissors. TIE!")

print("GAME OVER!")
