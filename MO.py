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
print( Fore.WHITE+Back.RED+"-Is 5 characters long")
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
print( Fore.WHITE+Back.RED+"-Is 5 characters long")
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
ans1 = input("What is the missing operator?")

if ans1 == op_list[op]:
    print("You're right!")
elif ans1 != op_list[op]:
    print("NOO!")
    print("Why would you think it's", ans1,"??")
    print("It's obviously", op_list[op])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

#saves the first character in the password.
first_character=op_list[op]


rhs=''
op2_ans= ''
op2=random.randint(0,2)
op3=random.randint(0,1)

if op2==0:
    op2_ans=num_1-num_2
elif op2==1:
    op2_ans=num_1+num_2
elif op2==2:
    op2_ans=num_1*num_2

if op3==0:
    rhs=op2_ans-num_3
elif op3==1:
    rhs=op2_ans+num_3

print()
print()

print("And now the second clue:")
print()
print(num_1,'__',num_2,'___',num_3,'=', rhs)
ans2_first = input("What is the first missing operator?")

print()
print()

if ans2_first == op_list[op2]:
    print("You're right!")
elif ans2_first != op_list[op2]:
    print("NOO!")
    print("Why would you think it's", ans2_first,"???")
    print("It's obviosly", op_list[op2], 'and', op_list[op3])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

ans2_second = input("What is the second missing operator?")

if ans2_second == op_list[op3]:
    print("You're right!")
elif ans2_second != op_list[op3]:
    print("NOO!")
    print("Why would you think it's", ans2_second)
    print("It's obviously", op_list[op2], 'and', op_list[op3])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

print()
print()

print("So the password thus far is:")
print(op_list[op], op_list[op2], op_list[op3], '__', '__')
print("That's 3 characters out of 5! You're Getting closer.")
input(">>")
print()
print()
print("And now the third and final clue:")

#the numbers for the third clue are randomly generated from 1-100 instead of using the numbers that the user gave.
#I might try to figure out how to add division to this one if i have time.

rhs=''
op4=random.randint(0,2)
op5=random.randint(0,1)
num_1_3=random.randint(1,100)
num_2_3=random.randint(1,100)
num_3_3=random.randint(1,100)
op4_ans=''

if op4==0:
    op4_ans=num_1_3-num_2_3
elif op4==1:
    op4_ans=num_1_3+num_2_3
elif op4==2:
    op_ans=num_1_3*num_2_3

if op5==0:
    rhs=op4_ans-num_3_3
elif op5==1:
    rhs=op4_ans+num_3_3

print(num_1_3, '__', num_2_3, '__', num_2_3, '=', rhs)
ans3_first = input("What is the first missing operator?")
if ans3_first == op_list[op4]:
    print("You're right!")
elif ans3_first != op_list[op4]:
    print("NOO!")
    print("Why would you think it's", ans3_first, "???")
    print("It's obviously", op_list[op4], 'and' , op_list[op5])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

ans3_second = input("What is the second missing operator?")
if ans3_second == op_list[op5]:
    print("You're right!")
elif ans3_second != op_list[op5]:
    print("NOO!")
    print("Why would you think it's", ans3_second, "???")
    print("It's obviously", op_list[op4], 'and', op_list[op5])
    print("You just made us lose 57 TRILLION DOLLARS!!!")
    print("You're FIRED!!")
    os._exit(0)

print()
print()
print()

print("So the full password is:")
print(op_list[op], op_list[op2], op_list[op3], op_list[op4], op_list[op5])

print()
print()
print("YOU WIN!!")
print("You have recovered 57 TRILLION DOLLARS!!")
print("As a reward, you can keep all the money!!")
print("Congratulations!! You are now richer than Melon Eusk!!!")
os._exit(0)


# Things to do later if there's time:
#.    - Add division in a 4th question
#     - Add parenthesis 
#.    - Add longer questions?

# I don't think i'll actually have time for all of this




#testing




### EDIT:
### There's some problem with the third clue. The questions are impossible. 
# Note to self: Fix this later.