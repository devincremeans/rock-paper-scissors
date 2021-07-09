# game.py

#Imports
 import random

print("Rock, Paper, Scissors, Shoot!")



# Ask for a user input
# Source: https://www.w3schools.com/python/ref_func_input.asp
x = input("Please choose one of 'rock', 'paper', 'scissors'")
print(x)




# Validate user input
if x=="rock" or (x== "paper") or (x=="scissors"):
    print("Valid")
else:
    print("Oops, invalid, please try again")
    exit()



# Generate computer choice
valid_options =  ["rock", "paper", "scissors"]

c = random.choice(valid_options)
print(random.choice(valid_options))
 
 print("Computer Choice")
 
# Determine Winner





