#defines vars

name = ""
age = 0
pass = []
users = []


#intro
print("welcome to password manager")

#menu
def menu(name, age):
    print("hello" name)
    if int(input("how old are you")) < 13:
        print("your are to young to use the password manager!")
        print("goodbye")
        exit()
    else:
        print("")