from random import randint

min_number = int(input("Please enter the minimum number: "))
max_number = int(input("Please enter the maximum number: "))

if max_number < min_number:
    print("Invalid input - shutting down...")
else:
    random_number = randint(min_number, max_number)
    print(
        f"Random number between {min_number} and {
            max_number} is: {random_number}."
    )
