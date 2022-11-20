# main function calling below functions together 

def main():
    x= input("enter indoor value :")
    print(indoor(x))
    string= input("enter the string value : " )
    print(playBack(string))
    emo=input(" enter you greeting with smile : ")
    print(emoji(emo))

# make string to lower case

def indoor(string):
    return string.lower()


# PLAYBACK

def playBack(string):
    return (string.replace(" ", "..."))

# convert to emoji

def emoji(string):
    ms1= string.replace(":)", "🙂")
    ms2=ms1.replace(":(" ,"🙁")
    return ms2

#e=mc2
def einstein():
    m=int(input( " enter the mass : "))

    c=300000000
    e= m * (c**c)
    return e

# squre a number

def squre(n):
    return (n**n)

main()


