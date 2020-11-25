import random
from art import logo,vs
from game_data import data

# #'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'

#print logo
print(logo)
print("Who has the most instagram followers?")


compare_A = random.choice(data)
compare_B = random.choice(data)

name_A = compare_A["name"]
name_B = compare_B["name"]
description_A = compare_A["description"]
description_B = compare_B["description"]
country_A = compare_A["country"]
country_B = compare_B["country"]
A_followers = int(compare_A["follower_count"])
B_followers = int(compare_B["follower_count"])

print(f"Compare A: {name_A}, a {description_A}, from {country_A}")

print(vs)

print(f"Compare B: {name_B}, a {description_B}, from {country_B}")

user_choice = input("Who has more followers? Type 'A' or 'B': ")
if user_choice.lower() == "a":
  user_choice = True
else:
  user_choice = False

def compare():
  if A_followers > B_followers:
    print("well done, correct!")
    A_followers = B_followers

  
  

