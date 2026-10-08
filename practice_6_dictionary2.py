sparring_log = {

}

opponent = input("Enter the name of your sparring opponent: ")

rounds = int(input("Enter the number of rounds you sparred: "))

def log_sparring(opponent, rounds):
    sparring_log[opponent] = rounds
    return f"Sparring session with {opponent} longed for {rounds} rounds."

print(log_sparring(opponent, rounds))