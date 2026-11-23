#imports
import time
import random
import colorama
from colorama import Back, Fore, init, Style

#color resets after each print statement
init(autoreset=True) 

#Ask for numbers
num_1=input(Back.YELLOW+"Please enter a number.")
num_2=input(Back.YELLOW+"Please enter another number.")
num_3=input(Back.YELLOW+"Please enter another number.")

print(Style.RESET_ALL)

#Begin the story
input("Press enter to begin the story")
if True:
    print('\033[H\033[J', end='')



#greet the user

print("Oh hello!")
name=input("What's your name, detective?")
print("It is good to see you here, "+ Fore.BLUE+"Detective "+ name)
input(">> *press anything*")

#explain the premise of the story
print("Yes, I know you are on vacation. But this is an "+ Fore.WHITE+Back.RED+ "emergency!!!")
time.sleep(.2)
print("The "+Fore.GREEN+ "Agastya Bank "+Fore.WHITE+" (The richest bank in the BUnited BStates of BAmerica!) has been"+Fore.WHITE+Back.RED+ " robbed!")
print("The theif stole over "+Back.RED+"57 trillion dollars in cash!!")
print()
time.sleep(.2)
input(">>")
print("You are the greatest detective in the world, so we have come seeking your help, "+ Fore.BLUE+"Detective " + name)
print("We don't know who did it, but the theif has unknowingly left us a clue")
print()
print('>>')
time.sleep(.2)
print("He has forgotten his phone behind, which contains all his secrets, and may reveal the location where he has hidden the money!")
print("But we need your help to find the password!")
input(">>")
print()
print()
print( "We know that the password:")
time.sleep(.2)
print( Fore.WHITE+Back.RED+"-Is 3 characters long")
time.sleep(.2)
time.sleep(.2)
print( "Each of these characters can be one of the following:")
time.sleep(.2)
print( Fore.WHITE+Back.RED+"+")
time.sleep(.2)
print( Fore.WHITE+Back.RED+"-")
time.sleep(.2)
print( Fore.WHITE+Back.RED+"x")