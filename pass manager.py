#defines vars
chosen = 0
name = ""
age = 0
pas = []
users = []
pass_inpt = ""
i = 0
user = ""
usepas = []
brec = "____________________________ \n"
#intro
print("--welcome to password manager--")

#menu
def menu(name, age):
    
    print("welcome {}" .format(name))
    
    if age < 13:
        print("your are to young to use the password manager!")
        print("goodbye")
        exit()

#start of user input

while True:
    
    try:
        age = int(input("what is your age?: "))
        break
    
    except ValueError:
        print("this is an invalid number")  

name = input("what is your name?: ")

print(menu(name, age))
    
#main
while chosen == 1 or 2 or 0:
    chosen = int(input("-type 1 to add a password.\n-type 2 to view the lists.\n-type 3 to exit the program.\n: "))
    
    if chosen == 1:
        print("")
        site = input("what is this password used for?: ")
        user = input("what is the username you want to add?: ")
        pass_inpt = input("what is the password that goes with this site?: ")
        usepas.append(" {} site: {} \n {} Username: {} \n {} Password: {} {}" .format(brec, site, brec, user, brec, pass_inpt, brec ))
    
    elif chosen == 2:
        print(" ".join(usepas))
    
    elif chosen == 3:
        print("goodbye")
        exit()
    
    else:
    
        print("this is not a eligible number")
    
    main = 0
    
