Khael = {
    "name": "Khael", "stance": "Southpaw", "style": "peek-a-boo", "weight": 57
}

Lawrence = {
    "name": "Lawrence", "stance": "Orthodox", "style": "Hitman", "weight": 65
}

Johnny = {
    "name": "Johnny", "stance": "Southpaw", "style": "Counterpuncher", "weight": 75
}

Jonas = {
    "name": "Jonas", "stance": "Southpaw", "style": "Brawler", "weight": 67
}

roster = {
    "khael": Khael,
    "lawrence": Lawrence,
    "johnny": Johnny,
    "jonas": Jonas
}

fighter_roster = {
    "khael": {"name": "Khael", "stance": "Southpaw", "style": "peek-a-boo", "weight": 57},
    "lawrence": {"name": "Lawrence", "stance": "Orthodox", "style": "Hitman", "weight": 65},
    "johnny": {"name": "Johnny", "stance": "Southpaw", "style": "Counterpuncher", "weight": 75},
    "jonas": {"name": "Jonas", "stance": "Southpaw", "style": "Brawler", "weight": 67},
}

def print_fighter_profile(fighter):
    profile = f" \nFighter Name: {fighter['name']}\nStance: {fighter['stance']}\nStyle: {fighter['style']}\nWeight: {fighter['weight']} kg\n"
    return profile

# search_name = input("Enter the fighter name to view their profile: ").lower()
# found_fighter = roster.get(search_name)

# if found_fighter:
#     print(print_fighter_profile(found_fighter))
# else:
#     print("Fighter not found. Please check the spelling and try again.")
    


# NOTE: REFACTORS ON THE FIFTH LESSON

def print_fighter_roster(fighter):
    profile = f" \nFighter Name: {fighter['name']}\nStance: {fighter['stance']}\nStyle: {fighter['style']}\nWeight: {fighter['weight']} kg\n"
    return profile

def add_fighter_to_roster(roster_key, name, stance, style, weight):
    fighter_roster[roster_key] = {
        "name": name,
        "stance": stance,
        "style": style,
        "weight": weight
    }
    return f"Fighter {name} has been added to the roster."

print(f"Fighters currently in the list: {list(fighter_roster.keys())}\n")

add_name = input("Enter the fighter name to add: ").title()
add_stance = input("Enter the fighter stance: ").capitalize()
add_style = input("Enter the fighter style: ").capitalize()
add_weight = input("Enter the fighter weight: ")

new_roster_key = add_name.lower()

print(add_fighter_to_roster(new_roster_key, add_name, add_stance, add_style, add_weight))

print(f"\nUpdated list: {list(fighter_roster.keys())}\n")

search_name = input("Enter the fighter name to view their profile: ").lower()
found_fighter = fighter_roster.get(search_name)

if found_fighter:
    print(print_fighter_profile(found_fighter))
else:
    print("Fighter not found. Please check the spelling and try again.")