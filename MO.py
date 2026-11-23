#imports
import time
import random
import colorama
from colorama import Back, Fore, Style, init

#color resets after each print statement
init(autoreset=True) 


#greet the user

print("Oh hello!")
name=input("What's your name, detective?")
print("It is good to see you here, "+ Fore.BLUE+"Detective "+ name)
print()
print()
time.sleep(.2)

#explain the premise of the story
print("Yes, I know you are on vacation. But this is an "+ Fore.WHITE+Back.RED+ "emergency!!!")
time.sleep(.2)
print("The "+Fore.GREEN+ "Agastya Bank "+Fore.WHITE+" (The richest bank in the BUnited BStates of BAmerica!) has been"+Fore.WHITE+Back.RED+ " robbed!")
print("The theif stole over "+Back.RED+"57 trillion dollars in cash!!")
print()
time.sleep(.2)
print("You are the greatest detective in the world, so we have come seeking your help, "+ Fore.BLUE+"Detective " + name)
print("We don't know who did it, but the theif has unknowingly left us a clue")
print()
time.sleep(.2)
print("He has forgotten his phone behind, which contains all his secrets, and may reveal the location where he has hidden the money!")
print("But we need your help to ")