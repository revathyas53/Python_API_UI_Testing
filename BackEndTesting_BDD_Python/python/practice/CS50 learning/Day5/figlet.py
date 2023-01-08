import sys
from pyfiglet import Figlet
import random
msg=input("Input: ")
figlet=Figlet()
if len(sys.argv)==1:
    isRandomFont=True
elif (len(sys.argv)==3) and (sys.argv[1]=="-f")or (sys.argv[1]=="--font"):
    isRandomFont =False
else:
    print(" Invalid usage ")
    sys.exit()

#Figlet.getFonts()

if isRandomFont ==False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    except:
        print("Invalid usage")
        sys.exit()
else:

    randomfont=random.choice(figlet.getFonts())
    figlet.setFont(font=randomfont)
    print(figlet.renderText(msg))
