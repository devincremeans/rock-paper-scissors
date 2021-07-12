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

print("User Choice", x)

# Generate computer choice
valid_options =  ["rock", "paper", "scissors"]

c = random.choice(valid_options)

print("Computer Choice", c)
 
# Determine Winner
# 1. Rock > Scissors
# 2. Paper > Rock
# 3. Scissors > Paper
# 4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
# Source: https://docs.python.org/3/tutorial/controlflow.html#if-statements

if x =="rock" and c =="scissors":
    print("User Won") 
elif x=="Paper" and c=="Rock":
    print("User Won")
elif x== "scissors" and c == "paper":
    print("User Won")
elif x == c:
    print("Tie")
else:
    print("Computer Won")











