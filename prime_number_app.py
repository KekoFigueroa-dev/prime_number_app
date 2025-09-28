# Prime Number App

# 1. Print welcome message
print("Welcome to my Prime Number Finder!")
# 2. Set up main loop control flag
is_running = True

#while active:
while is_running:
    print("\nYou can choose the following options:")
    print("\t (a) Determine if a given value is a prime number")
    print("\t (b) List all prime numbers in a given range")
    #Get user choice
    choice = input("\nWhat menu option do you choose? (a or b): ").lower()
    #input validation
    while not choice:
        print("Sorry option is invalid. Choose a or b")
        choice = input("What menu option do you choose? (a or b): ").lower()
        
        
    number = input("Enter a positive integer to check if it's prime: ")
    while not number.isdigit():
        print("Invalid input. Please enter a positive integer.")
        number = input("Enter a positive integer to check if it's prime: ")
    number = int(number)

    # If user chooses option a:
    if choice == "a":
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number.")
    # Elif user chooses option b: 
    elif choice == "b":
        primes = []
        for prime_candidate in range(2, number):
            is_prime = True
            for i in range(2, prime_candidate):
                if prime_candidate % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(prime_candidate)
        print(f"All prime numbers between 2 and {number} :")
        for prime in primes:
            print(prime, end=", ")
        print()  
    #Else: invalid option
    else:
        print("Invalid option. Please choose 'a' or 'b'.")

    # 8. Ask user if they want to run again
    run_again = input("Would you like to run the program again? (y/n): ").lower()
    if run_again == 'y':
        is_running = True
    # 9. If not, set flag to False and print goodbye message
    else:
        is_running = False
        print("Thank you for using the Prime Number Finder. Goodbye!")
