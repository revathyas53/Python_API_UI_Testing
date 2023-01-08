'''

I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and , inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

'''

import random

##num=random.randint(1, 100)
#print(num)


def main():

    while True:
        try:
            level=int(input("Level: "))
            if level>0:
                num=random.randint(1, level)
                guess(num)
                break
        except:
            pass
def guess(num):
    while True:
        try:
            num_input=int(input("Guess the number: "))
            if num_input>0:
                if num_input ==num:
                    print("Just right!")
                    break
                elif num_input>num:
                    print("Too large!")
                else:
                    print("Too small!")
        except:
            pass

if __name__=="__main__":
    main()