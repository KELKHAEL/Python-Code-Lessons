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

def print_fighter_profile(fighter):
    profile = f" \nFighter Name: {fighter['name']}\nStance: {fighter['stance']}\nStyle: {fighter['style']}\nWeight: {fighter['weight']} kg\n"
    return profile

print("\nFighters currently in the list: ")
print(f"\n {Khael['name']}\n {Lawrence['name']}\n {Johnny['name']}\n {Jonas['name']}\n")

search_name = input("Enter the fighter name to view their profile: ").lower()
found_fighter = roster.get(search_name)

if found_fighter:
    print(print_fighter_profile(found_fighter))
else:
    print("Fighter not found. Please check the spelling and try again.")