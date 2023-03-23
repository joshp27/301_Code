# # Script: Ops 301 Class 09 Code Challenge
# # Joshua Phipps
# # 3/23/2023
# # Purpose: Python Conditional Statements

#!/usr/bin/env python3

# Define variables for comparison
worst_hero1 = "cyclops"
worst_hero2 = "wolverine"

# Check if user input matches the first worst hero
hero = input("Who is the lamest superhero?: ").lower()
if hero == worst_hero1:
    print("He is useless")
# Check if user input matches the second worst hero
elif hero == worst_hero2:
    print("He is also weak")
# If user input does not match either worst hero
elif hero != worst_hero1 and hero != worst_hero2:
    print("Why are they on the team?")
# If all other conditions are not met
else:
    print("They are the lamest")