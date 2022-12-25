# should output nutrition value of fruit entered by user 

dict={"apple":130, "avacado":50, "banana":110, "Watermelon":80,"Tangerine":50,"SweetCherries":100, "Grapefruit":60,"Honeydew Melon": 50, "Grapes":90, "plum":70, "Pine apple": 50, "pear":100, "peach":60, "lime":20, "orange":80}
fruit=input("enter the fruit name: ")
for i in dict:
    if i.lower()==fruit.lower():
        print("Callories :",dict[i])
        break



