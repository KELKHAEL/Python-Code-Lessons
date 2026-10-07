def calculate_punch_speed(punches_thrown, rounds):
    total_minutes = rounds * 3 #number of rounds
    punches_per_minute = punches_thrown / total_minutes
    return punches_per_minute

def print_fighter_profile(name, stance, weight):
    my_profile = f"Fighter Name: {name}\nStance: {stance}\nWeight: {weight} kg\n"
    return my_profile

def calculate_calories(jump_rope_minutes, heavy_bag_minutes, weight):
    calories_burned = (jump_rope_minutes * 12) + (heavy_bag_minutes * 10) + (weight * 0.1)
    return calories_burned


#Calls
print("\nMy Fighter Profile\n")

#Profile Information
print(print_fighter_profile("Khael", "Southpaw", 57))

#Punch speed (per round)
my_speed = calculate_punch_speed(470, 3)
print(f"Punch speed is {round(my_speed,2)} punches per minute.\n")

#Calories burned
session_burned = calculate_calories(15, 15, 57)
print(f"Calories burned during training: {session_burned} calories.")