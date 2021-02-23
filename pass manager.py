#defines vars

chosen = 0
name = ""
age = 0
pass_ = []
users = []
pass_inpt = ""
i = 0

#intro
print("welcome to password manager")

#menu
def menu(name, age):
    print("hello " + name)
    if age < 13:
        print("your are to young to use the password manager!")
        print("goodbye")
        exit()
    else:        
        mode = int(input("1, 2, 3?"))
        return mode
#START OF user input
while True:
    try:
        age = int(input("what is your age?: "))
        all()
    except ValueError:
        print("invalid age") 
    except:
        print("an unknown error has ")

def all():
    name = input("what is your name?: ")
    print(menu(name, age))
    
    #main
    while chosen == 1 or 2 or 0:
        chosen = menu(name, age)
        if chosen == 1:
            pass_inpt = input("pass?")
            pass_.append(pass_inpt)
        elif chosen == 2:
            for i in pass_:
                print(pass_[i])
                i += 1
        
        elif chosen == 3:
            print("goodbye")
            exit()
        else:
            print("this is not a eligible number")
        main = 0
