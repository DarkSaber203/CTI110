#Jonathan Snodgrass

#11/24/24

#P5HW

#menu system, about random numbers

import random

def generate_random_numbers():
    return random.randint(1, 100), random.randint(1, 100)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def menu():
    print("Menu:")
    print("1. Add two random numbers")
    print("2. Subtract two random numbers")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            num1, num2 = generate_random_numbers()
            result = add_numbers(num1, num2)
            print(f"Two random numbers are: {num1} and {num2}")
            guess = int(input("Guess the sum of these numbers: "))
            if guess == result:
                print("Congratulations! You guessed it right.")
            else:
                print(f"Sorry, the correct sum is {result}.")
        
        elif choice == '2':
            num1, num2 = generate_random_numbers()
            result = subtract_numbers(num1, num2)
            print(f"Two random numbers are: {num1} and {num2}")
            guess = int(input("Guess the remainder of the subtraction: "))
            if guess == result:
                print("Congratulations! You guessed it right.")
            else:
                print(f"Sorry, the correct remainder is {result}.")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
