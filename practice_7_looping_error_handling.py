while True:
    try:
        targetWeight = float(input("Enter your target weight (in kg): "))
        print(f"Official weight-in recorded: {targetWeight} kg")

        break

    except ValueError:
        print("Invalid entry, Enter numbers only (e.g., 53.5).")


        # user = input("Do you want to try again? (Y/N): ")

        # if user == "Y":
        #     continue
        # elif user == "N":
        #     print("Session ended.")
        # else:
        #     print("Invalid entry, please enter Y or N. Session terminated.")