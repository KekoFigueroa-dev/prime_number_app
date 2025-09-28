# Prime Number Finder

A Python app to check if a number is prime or to list all primes in a given range.  
Includes timing for range calculations so you can see how efficient your code is.

## How it works

- Choose to check a single number or list all primes in a range.
- Input validation ensures only positive integers are accepted.
- For a single number, the app tells you if it is prime.
- For a range, the app lists all primes and shows how long the calculation took.
- You can run the app as many times as you want.

## Usage

1. Run `python prime_number_app.py`.
2. Choose an option:
   - Enter `a` to check if a number is prime.
   - Enter `b` to list all primes in a range.
3. Follow the prompts.
4. Repeat or exit as you wish.

## Example

```
Welcome to my Prime Number Finder!
You can choose the following options:
     (a) Determine if a given value is a prime number
     (b) List all prime numbers in a given range
What menu option do you choose? (a or b): b
Enter the lower bound (integer >= 2): 1
Enter the upper bound (integer > lower bound): 20
All prime numbers between 1 and 20:
2, 3, 5, 7, 11, 13, 17, 19
Calculations took a total of 0.0002 seconds.
Would you like to run the program again? (y/n): n
Thank you for using the Prime Number Finder. Goodbye!
```

---

**Great for practicing loops, conditionals, input validation, and timing in Python.**