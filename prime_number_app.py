import time

# Prime Number App

print("Welcome to my Prime Number Finder!")  # Welcome message

is_running = True  # Main loop control flag

while is_running:
    # Display menu options
    print("\nYou can choose the following options:")
    print("\t (a) Determine if a given value is a prime number")
    print("\t (b) List all prime numbers in a given range")
    choice = input("\nWhat menu option do you choose? (a or b): ").lower()

    # Validate menu choice
    while not choice:
        print("Sorry option is invalid. Choose a or b")
        choice = input("What menu option do you choose? (a or b): ").lower()

    if choice == "a":
        # Get and validate number to check
        number = input("Enter a positive integer to check if it's prime: ")
        while not number.isdigit() or int(number) < 2:
            print("Invalid input. Please enter an integer greater than 1.")
            number = input("Enter a positive integer to check if it's prime: ")
        number = int(number)

        # Prime check logic
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        # Output result
        if is_prime:
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number.")

    elif choice == "b":
        # Get and validate range bounds
        lower = input("Enter the lower bound (integer >= 2): ")
        while not lower.isdigit() or int(lower) < 2:
            print("Invalid input. Please enter an integer >= 2.")
            lower = input("Enter the lower bound (integer >= 2): ")
        lower = int(lower)

        upper = input("Enter the upper bound (integer > lower bound): ")
        while not upper.isdigit() or int(upper) <= lower:
            print("Invalid input. Please enter an integer greater than the lower bound.")
            upper = input("Enter the upper bound (integer > lower bound): ")
        upper = int(upper)

        # Time the prime search
        start_time = time.time()

        primes = []
        for prime_candidate in range(lower, upper + 1):
            is_prime = True
            for i in range(2, prime_candidate):
                if prime_candidate % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(prime_candidate)

        end_time = time.time()
        delta_time = round(end_time - start_time, 4)

        # Output primes and timing
        print(f"All prime numbers between {lower} and {upper}:")
        if primes:
            print(", ".join(map(str, primes)))
        else:
            print("No primes found in this range.")
        print(f"Calculations took a total of {delta_time} seconds.")

    else:
        # Handle invalid menu option
        print("Invalid option. Please choose 'a' or 'b'.")

    # Prompt to run again or exit
    run_again = input("Would you like to run the program again? (y/n): ").lower()
    if run_again == 'y':
        is_running = True
    else:
        is_running = False
        print("Thank you for using the Prime Number Finder. Goodbye!")
