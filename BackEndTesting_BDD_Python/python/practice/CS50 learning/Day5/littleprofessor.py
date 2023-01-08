import random


def main():
    score=0
    i=10
    l=get_level()
    while i:
        try:  
            x,y=generate_integer(l)
            try:
                print(f"{x}+{y}= ?")
                ans=int(input(""))
                if ans==(x+y):
                    score+=1
                    i=i-1
                else:
                    print("EEE")
                    i=i-1
            except:
                print("EEE")
                i=i-1
                pass
        except:
            break

    print(f"SCORE:{score}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level  
        except ValueError:
            print(ValueError)


def generate_integer(level):
    while level:
        try:
            if level==1:
                x=random.randint(level,10)
                y=random.randint(level,10)
                return x, y
            elif level==2:
                x=random.randint(10,100)
                y=random.randint(10,100)
                return x, y
            elif level==3:
                x=random.randint(100,1000)
                y=random.randint(100,1000)
                return x, y
            else:
                raise ValueError
        except :
            print()
            break 

if __name__ == "__main__":
    main()