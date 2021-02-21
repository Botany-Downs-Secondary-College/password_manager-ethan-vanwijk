#defines vars

main = 1
name = ""
age = 0
pass_ = []
users = []
pass_inpt

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
        print("you are elegible")

#main
while main == 1 or 2:
    main = input("1, 2, 3?")
    if main == 1:
        pass_inpt = input("pass?")
        append.pass_(pass_inpt)
