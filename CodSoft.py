"""
CODSOFT TASKS

SANDEEP SWAMI
3RD YEAR 
"""
# --------------------------------------------------------------------------------------Task 1 To Do List 

def to_do_list():
    print("TASK 1")
    print("TO - DO - LIST ")
    print("Name : SANDEEP SANJAYKUMAR SWAMI\n")
    my = []
    while True:
        print('\n')
        print("1. For Add task type 'add'.")

        print("2. For Remove task type 'remove'.")
        print("3. For Exit type 'exit'")
        print("4. For view type 'view'.\n")

        cc = input("Enter your choice : ")
        if cc == 'add':
            print("\nFor stop adding your list type 'st'.\n")

            while True:
                b = input("Enter your task :")
                my.append((b))

                if b == 'st':
                    break


        elif cc == 'remove':
            print("\nFor stop emoving your list type 'st'.\n")

            while True:
                mm = input("\nEnter a name of task you wanna remove it : ")
                my.remove(mm)

                if b == 'st':
                    break

        elif cc == 'view':
            noo = 0
            print("\nYour To - Do - List\n")
            for b in my:
                print(f"---> {b}")

        elif cc == 'exit':
            break
to_do_list() 


# -------------------------------------------------------------------------------------Task 2 calculater
print("TASK 2")
print("calculater")
print("Name : SANDEEP SANJAYKUMAR SWAMI\n")
input1 = int(input("\nEnter your 1st input : "))
operation = input("Enter your operation like +, -, *, /: ")
input2 = int(input("Enter your 2nd input : "))
if operation == '+':
    print("\n------------------------------")
    print("\nAns is --- [",input1+input2,"]")

elif operation == '*':
    print("\n------------------------------")  
    print("\nAns is --- [",input1*input2,"]")

elif operation == '-':
    print("\n------------------------------")
    print("\nAns is --- [",input1-input2,"]")

elif operation == '/':
    print("\n------------------------------")
    print("\nAns is --- [",input1/input2,"]")
    



# --------------------------------------------------------------------------------------Task 3 PASSWORD GENERATOR

print("TASK 3")
print("------ PASSWORD GENERATOR ------")
print("Name : SANDEEP SANJAYKUMAR SWAMI\n")
import random

user = int(input("how many digit pass you want : "))
a2 = "!@#$%^&*"
a1 = "QWERTYUIOASDFGHJKLZXCVBNM"
a3 = "1234567890"
a4 = "qwertyuiopasdfghjklzxcvbnm"
comp = user - 3

passward = ""
passward += random.choice(a1)
passward += random.choice(a2)
passward += random.choice(a3)
for i in range(comp):
    passward += random.choice(a4)

print(f"\n --------->Your generated pass is :[ {passward} ]")



# --------------------------------------------------------------------------------------Task 4 game Rock-Paper-Scissors Game
def game():
    print("TASK 4")
    print("Rock-Paper-Scissors Game")
    print("Name : SANDEEP SANJAYKUMAR SWAMI\n")
    import random

    s1 = "rock"
    s2 = "paper"
    s3 = "scissor"

    user = input("""
    rock
    paper
    scissor
                 
    Enter your choice : """)
    comp = random.randint(1,3)

    def dta():
    # user
        if user == "rock":
            print(f"user = {s1}")

        elif user == "paper":
            print(f"user = {s2}")

        elif user == "scissor":
            print(f"user = {s3}")

    # comp
        if comp == 1:
            print(f"comp = {s1}")

        elif comp == 2:
            print(f"comp = {s2}")

        elif comp == 3:
            print(f"comp = {s3}")


    if (user == "scissor" and comp == 2) or (user == "rock" and comp == 3) or (user == "paper" and comp == 1):
        dta()
        print("user win")
        print("\nfor quite press 'q' ")
        game()

    elif (comp == 3 and user == "paper") or (comp == 1 and user == "scissor") or (comp == 2 and user == "rock"):
        dta()
        print("comp win")
        print("\nfor quite press 'q' ")
        game()

    elif (user == "rock" and comp == 1) or (user == "paper" and comp == 2) or (user == "scissor" and comp == 3):
        dta()
        print("tie")
        print("\nfor quite press 'q' ")
        game()

    elif user == "q":
        print("thanku")
game()


# --------------------------------------------------------------------------------------Task 5 Contact Book

print("TASK 3")
print("Rock-Paper-Scissors Game")
print("Name : SANDEEP SANJAYKUMAR SWAMI\n")

contact = {}
while True:
    print("""
        1.For inter a date plz type '1'.
           
        2.For remove contact info specific person type '2'.
          
        3.For update type  '3'.

        4.For view search type '4'.

        5.For list of contact type'5'.

        6.For exit type '00'.""")
    choice = int(input("\nEnter your choice only 'int' : "))

    if choice == 1:
        name = input("\nEnter your name :")
        phone_number = int(input("Enter Phone no :"))
        email = int and input("Enter email id: ")
        address = int and input("Enter address : ")
        contact[name] =  name, phone_number, email, address
        print("\n-------- DATA IS FILLED --------")

    elif choice == 2:
        name2 = input("\nEnter name for remove:")
        contact.pop(name2)
        print("--------Entered data is removed--------")

    elif choice == 3:# --------------------------------> update options 
        print("""
            \n1.For update phone no plzz type '1'.

            2.For update email plzz type '2'.

            3.For update address plzz type '3'.

            4.If person name is false means whole data is false then plzz delete person information plzz.""")
        update = int(input("\nWhich one you need to upadte : "))

        if update == 1:
            name3 = input("\nEnter your name :")
            new_phone = int(input("Enter new no :"))
            contact[name3] =  name, new_phone, email, address
            print("--------Entered data is updated--------") 

        elif update == 2:
            name3 = input("\nEnter your name :")
            new_email = int(input("Enter new no :"))
            contact[name3] =  name, new_phone, new_email, address
            print("--------Entered data is updated--------")

        elif update == 3:
            name3 = input("\nEnter your name :")
            new_address = int(input("Enter new no :"))
            contact[name3] =  name, new_phone, email, new_address 
            print("--------Entered data is updated--------")           
    
    elif choice == 4:
        need_watch = input("\nEnter name for search : ")
        print("----------> Result ")
        print(contact[need_watch])

    elif choice == 5:
        print("Contact list\n")
        for i in contact:
            print(f"\n{i}")

    elif choice == 00:
        break
