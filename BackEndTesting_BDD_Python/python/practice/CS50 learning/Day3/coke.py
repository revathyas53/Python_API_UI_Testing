#coke value 50 cents
# user can inputb  25 or 10 or 5 cents one after other to buy coke
# program should printr balance or due after each entry from user until the amount<=50 
def check():
    sum=0
    while sum<50:
        amount=int(input("Enter the amount( only accept 25,10,and 5):"))
        sum=sum+amount
        if sum<50:
            due= 50-sum
            print("Amouunt Due: ", due)
        else:
            change=sum-50
            print("Change Owed: ", change)

check()

