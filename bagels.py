import random
NUM_DIGITS = 3
MAX_GUESSES=10

def main():
    print("'Bagels, a deductive logic game. by Al Sweighart'")
    print("I am thinking of a {}-digit number with no repeated digits." .format(NUM_DIGITS))
    print("Try to guess what it is. Here are some clues:")
    print("When I say:     That means:")
    print("Pico            One digit is correct but in the wrong position")
    print("Fermi           One digit is correct and in the right position")
    print("Bagels          No digit is correct")
    print()
    print("For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.")
    while True: #Main game loop
        #This stores the secret number the player needs to guess.
        secret_num=