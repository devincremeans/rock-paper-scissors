# game.py

#Imports
import random

import os
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
print(USER_NAME)
# Source: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/dotenv.md

print("Welcome",USER_NAME,"to my Rock-Paper-Scissors game...")

# Ask for a user input
# Source: https://www.w3schools.com/python/ref_func_input.asp
x = input("Please choose one of 'rock', 'paper', 'scissors'")
print(x)

x = x.lower()
print(x)

# Validate user input
if x=="rock" or (x== "paper") or (x=="scissors"):
    print("Valid")
else:
    print("Oops, invalid, please try again")
    exit()

print("You chose:", x)

# Generate computer choice
valid_options =  ["rock", "paper", "scissors"]

c = random.choice(valid_options)

print("The compuer chose:", c)
 
# Determine Winner
# 1. Rock > Scissors
# 2. Paper > Rock
# 3. Scissors > Paper
# 4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
# Source: https://docs.python.org/3/tutorial/controlflow.html#if-statements

w = ("You Won! Congrats!")

if x =="rock" and c =="scissors":
    print(w) 
elif x=="Paper" and c=="Rock":
    print(w)
elif x== "scissors" and c == "paper":
    print(w)
elif x == c:
    print("Tie")
else:
    print("Oh, the computer won. It's ok")

print("-------------------")
print("Thanks for playing",USER_NAME," -- Please play again!")











