import json
from collections import Counter

def find_common_counters(enemyHeroes, jsonObject):
    # Convert the JSON object to a Python dictionary
    heroes_data = jsonObject
    
    # Create a dictionary with hero names as keys and their counters as values
    hero_counters = {hero['hero']: hero['counters'] for hero in heroes_data}
    
    # Initialize a list to store all counters for the enemy heroes
    all_counters = []
    
    # Loop through the enemy heroes and add their counters to the list
    for hero in enemyHeroes:
        if hero in hero_counters:
            all_counters.extend(hero_counters[hero])
    
    # Use Counter to find the most common counters
    counter = Counter(all_counters)
    
    # Return the top 3 most common counters
    return [hero for hero, count in counter.most_common(6)]

# Test the function
enemyHeroes = ["Pharah", "Mercy", "Ana", "Winston","Widowmaker"]
with open('C:\\Users\\bryan\\Desktop\\CodeProjects\\ow2herobuddy\\Python-app\\HeroCounterDB.json', 'r') as f:
    jsonObject = json.load(f) 

print(find_common_counters(enemyHeroes, jsonObject))