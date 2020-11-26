# Display art
# Generate a random account from the game data.
# Format account data into printable format.
# Ask user for a guess.
# Check if user is correct.
## Get follower count.
## If Statement
# Feedback.
# Score Keeping.
# Make game repeatable.
# Make B become the next A.
# Add art.
# Clear screen between rounds.

from game_data import data
import random
from art import logo, vs
from replit import clear

def format_account(account):
  """Format the data values into an account"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(guess, a_followers, b_followers):
  """Take the users guess and compares with followers then returns if correct """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


print(logo)
score = 0
game_continues = True
account_b = random.choice(data)

while game_continues:

  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
  print(f"Compare A: {format_account(account_a)}")
  print(vs)
  print("")
  print(f"Against B: {format_account(account_b)}")
  print("")
  guess = input("Who has more instagram followers? Type 'A' or 'B' ").lower()

  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_account, b_follower_account)
  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"Well done, you're correct! You're score is {score}")
  else:
    game_continues = False
    print(f"Who would have thought it, however Unfortunately you're wrong this time. You're final score is {score}")