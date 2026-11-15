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
        secret_num=getSecretNum()
        print("I have thought up a number")
        print("You have",MAX_GUESSES,"guesses to get it.")

        num_guesses=1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) !=NUM_DIGITS or not guess.isdecimal():
                print("Guess #", num_guesses,':', sep='')
                guess = input('\n>')
            clues = #FIXME-04
            print(clues)
            #One more guess has been taken
            #FIXME-05

            if #FIXME-06  #quit asking for guesses:
                break
            if #FIXME-07. #out of guesses:
                print('You ran out of guesses.')
                print('The answer was', #FIXME-08)
        #Ask player if they want to play again
        print('Do you want to play agin? (yes/no)')
        if not input('>').lower().startswith('y'):
            print('Thanks for playing!')
            #FIXME-09
def getSecretNum():
    numbers=list('0123456789')
    random.shuffle(numbers) 
    secret_num=''
    for i in range(NUM_DIGITS):
        secret_num+=str(numbers[i])
        #FIXME-11. #What does this function need to do at the end?
def get
main()