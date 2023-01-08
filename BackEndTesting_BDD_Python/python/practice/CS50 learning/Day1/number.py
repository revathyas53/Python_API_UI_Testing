x=input("enter first number? ")
y=input("2nd number?")
z=x+y # gives string since input function consider in string format
#9.99
#z1=int(x)+int(y)
print(z)
#9.999print(z1)
z2=float(x)+float(y)
z3=round(z2, 3)
print(z2)
print(z3)

print(f'{z2:,}')
print(f'{z2:2f}')

div=282/8
print(div)