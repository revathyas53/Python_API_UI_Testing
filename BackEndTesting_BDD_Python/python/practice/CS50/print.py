''' print("hello world!")
# ask user to enter their name

def greeting():
    name=input("what's your name? : ")
# say hello to user



    print(f'hello,'name.title()}, end='\n')
greeting() 

#print function -  print(*objects, sep=' ', end='\n', file=None, flush=False)
#print quates print("hello dear \"how do you do?" \"") === o/p ==hello dear "how do you do?"
print("hello dear \"how do you do?\"")
print("hello", "name " ,sep='??? ', end='\n')  # hello??? name

print("hello", end="\n")
print("hello", "name " ,sep='??? ', end='!!!!') # hello??? name !!!!


def greeting():
    name=input("what's your name? : ").strip().title()
# remove white
    #name=name.split()
# capitalise 
    #cap_name=name.capitalize()
    #print(cap_name)
# say hello to user
    print(f'hello, {name}')
greeting() 


'''


def greeting(Name):
    print(f' helloo to {Name.strip().title()}')

name=input("hello to ? :")


print(greeting(name))