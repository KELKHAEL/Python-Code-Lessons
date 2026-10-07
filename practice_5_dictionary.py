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

# print(f"\n{myStats['name']} standing on a weight of {myStats['weight']}kg and uses a {myStats['style']} style, facing a formidable opponent that goes by {firstOpponent['name']} who is a {firstOpponent['stance']} fighter, that uses a {firstOpponent['style']} style and weighs {firstOpponent['weight']} kg.")

def print_fighter_profile(fighter):
    profile = f" \nFighter Name: {fighter['name']}\nStance: {fighter['stance']}\nStyle: {fighter['style']}\nWeight: {fighter['weight']} kg\n"
    return profile

print("\nFighters currently in the list: ")
print(f"\n {Khael['name']}\n {Lawrence['name']}\n {Johnny['name']}\n {Jonas['name']}\n")

fighter = input("\nTo view the fighters info enter the name of the fighter: ")

if fighter.lower() == "khael":
    print(print_fighter_profile(Khael))
elif fighter.lower() == "lawrence":
    print(print_fighter_profile(Lawrence))
elif fighter.lower() == "johnny":
    print(print_fighter_profile(Johnny))
elif fighter.lower() == "jonas":
    print(print_fighter_profile(Jonas))
else:
    print("Fighter not found. Please check the spelling and try again.")