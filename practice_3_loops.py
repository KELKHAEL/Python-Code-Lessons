import time

current_round = int(input("Enter the number of rounds to fight: "))
round_timer = int(input("Enter seconds per round: "))

while current_round > 0:
    print(f"{current_round} rounds left.")
    current_round = current_round - 1
    time.sleep(round_timer)
  
print("Round over.")

# print("Let's start your workout!")
# print("Choose your exercises for today.")
# print("Here are some exercises to choose from:")
# print("1. Dips")
# print("2. Push-ups")
# print("3. Pull-ups")
# print("4. Squats")
# print("5. Lunges")
# print("6. Plank")

# exercise = int(input("Choose your exercise by entering the corresponding number: "))
# exercises = ["dips", "push-ups", "pull-ups", "squats", "lunges", "plank"]

# chosen_exercise = exercises[exercise - 1]

# print(f"You chose: {chosen_exercise}")


# // for loop to print the chosen exercise using slice. // #

# for item in exercises[exercise - 1:exercise]:
#     print("You chose: " + item)