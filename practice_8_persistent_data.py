while True:
    try:

        user = input("Enter 'a' to record weight, 'r' to view history of the recorded logs and 'q' to quit: \n")

        if user == "a":
            with open("weight_log.txt", "a") as file:
                weightLogs = float(input("Enter weight to append: "))
                file.write(f"New recorded weight data: {weightLogs}\n")

        elif user == "r":
            with open("weight_log.txt", "r") as file:
                saved_data = file.read()
                print("\nHere is your saved history: ")
                print(saved_data)

        elif user == "q":
            
            print("Session Terminated.")

            break

        else:
            print("Invalid entry, please enter 'a', 'r', 'q' in lowercase.")
    
    except ValueError:

        print("Invalid entry, please enter 'a', 'r', or 'q' in lowercase.")