'''
Here’s how to test your code manually:

Run your program with python deep.py. Type 42 and press Enter. Your program should output:
Yes 
Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:
Yes
Run your program with python deep.py. Type forty-two and press Enter. Your program should output
Yes
Run your program with python deep.py. Type 50 and press Enter. Your program should output
No
Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. 
Your program should behave as expected, case- and space-insensitively.

You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!
'''


def main():
    ques=input("enter the value ")
    if ques=='42'or ques=='Forty Two' or ques=='forty-two':
        print('yes')
    else:
        print('No')

def usingMatch():
    ques=input("enter the value ")
    match ques:
        case '42'| 'Forty Two' |'forty-two':
            print ("Yes")
        case _:
            print("No")
main()
usingMatch()