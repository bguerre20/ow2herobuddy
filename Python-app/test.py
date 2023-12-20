import json
from collections import Counter

def find_common_counters(enemyHeroes, jsonObject, playerRole):
    # Create a dictionary with hero names as keys and their counters as values
    hero_counters = {hero['hero']: hero['counters'] for hero in jsonObject}
    # Create a dictionary with hero names as keys and their roles as values
    hero_roles = {hero['hero']: hero['role'] for hero in jsonObject}

    # Initialize a list to store all counters for the enemy heroes
    all_counters = []
    
    # Loop through the enemy heroes and add their counters to the list
    for hero in enemyHeroes:
        if hero in hero_counters:
            # Check the role of each counter before adding it to the list
            all_counters.extend(counter for counter in hero_counters[hero] if counter in hero_roles and hero_roles[counter] == playerRole)
    
    # Use Counter to find the most common counters
    counter = Counter(all_counters)
    
    # Return the top 3 most common counters
    return [hero for hero, count in counter.most_common(3)]

# Test the function
enemyHeroes = ["Hanzo", "Zenyatta", "Mercy", "Wrecking Ball","Echo"]
with open('C:\\Users\\bryan\\Desktop\\CodeProjects\\ow2herobuddy\\Python-app\\HeroCounterDB.json', 'r') as f:
    jsonObject = json.load(f) 

print(find_common_counters(enemyHeroes, jsonObject,playerRole='damage'))