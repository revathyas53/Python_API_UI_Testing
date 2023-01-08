# this program helps to convert camel case to snake case
# camelase= revathyAnilaSreekumar
# snake_case= revathy_anila_sreekumar
def main():
    camelCase=input("enter a name :")
    print("snake case : ", end="")
    snakeCase(camelCase)

def snakeCase(str):
    for letter in str:
        if letter.isupper():
            print("_"+(letter.lower()), end="")
        else:
            print(letter, end="")
    print()
main()