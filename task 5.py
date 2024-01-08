# --------------------------------------------------------------------------------------Task 5 Contact Book

print("TASK 5")
print("Contact Book")
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
            new_email = int(input("Enter new email :"))
            contact[name3] =  name, new_phone, new_email, address
            print("--------Entered data is updated--------")

        elif update == 3:
            name3 = input("\nEnter your name :")
            new_address = int(input("Enter new address :"))
            contact[name3] =  name, new_phone, email, new_address 
            print("--------Entered data is updated--------")           
    
    elif choice == 4:
        need_watch = input("\nEnter name for search : ")
        print("----------> Result ")
        print("name phone no email id addr")
        print(contact[need_watch])
        for i in contact:
            print("Name: " + contact[i][0])
            print("Phone: " + contact[i][1])
            print("Email: " + contact[i][2])
            print("Addr: " + contact[i][3])



    elif choice == 5:
        print("Contact list\n")
        for i in contact:
            print(f"\n{i}")

    elif choice == 00:
        break
