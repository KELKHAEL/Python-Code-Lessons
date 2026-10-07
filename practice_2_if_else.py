weight = float(input("Enter your current weight in kg: "))

if weight >= 57.0:
    print("You are overweight.")
elif weight >= 54.0:
    print("Keep cutting weight.")
elif weight >= 53.0:
    print("You are at your target weight.")
else:
    print("You are underweight.")