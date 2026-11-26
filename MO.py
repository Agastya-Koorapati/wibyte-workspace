#imports
import os
import time
import random
import colorama
from colorama import Back, Fore, init, Style

#color resets after each print statement
init(autoreset=True) 

#Ask for numbers
num_1=int(input(Back.YELLOW+"Please enter a number."))
num_2=int(input(Back.YELLOW+"Please enter another number."))
num_3=int(input(Back.YELLOW+"Please enter another number."))

print(Style.RESET_ALL)

#Begin the story
input("Press enter to begin the story")
print('\033[H\033[J', end='')



#greet the user

print("Oh hello!")
name=input("What's your name, detective?")
print("It is good to see you here, "+ Fore.BLUE+"Detective "+ name)
input(">> *press enter*")

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
print()
print()
input(">> *press enter to begin game*")
print('\033[H\033[J', end='')


# restate the rules
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

print()
print()
print()

#-----------

rhs = ''
op_list = ['-','+','*']
op=random.randint(0,2)

if op==0:
    rhs=num_1-num_2
elif op==1:
    rhs=num_1+num_2
elif op == 2:
    rhs = num_1*num_2

print('Clue number one:')
print(num_1, '__', num_2, '=', rhs)
ans = input("What is the missing operator?")

if ans == op_list[op]:
    print("You're right!")
elif ans != op_list[op]:
    print("NOO!")
    print("Why would you think it's", ans,"??")
    print("It's obviously", op_list[op])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

#making sure the os._exit(0) works.
print('TESTING')


#to be continued l8r
#  to be added:
#  - record the first character in the password as a variable
#. - add num_3 to the second clue
#  - iff possible, the second clue should include division. Not sure how that works, but we'll burn that bridge when we get to it.
#  - The third clue should be super hard. it includes division AND three randomly generated numbers instead of the ones that the user has picked. 
#.   These numbers are randomly generatede from 1-100.