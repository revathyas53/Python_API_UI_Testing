# program should eliminate vowels in the string
def main():
    string=input("enter the twit string: ")
    twttr(string)

def twttr(str):
    for letter in str:
        if letter not in ["A","E", "I", "O", "U","a", "e", "i" ,"o" , "u"]:
            print(letter, end="")
        else:
            print(end="")
    print()

main()