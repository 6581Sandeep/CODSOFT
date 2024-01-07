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

                if b == 'st':
                    break

                my.append((b))

                


        elif cc == 'remove':
            print("\nFor stop emoving your list type 'st'.\n")

            while True:
                mm = input("\nEnter a name of task you wanna remove it : ")
                my.remove(mm)

                if b == 'st':
                    break

        elif cc == 'view':
            print("\nYour To - Do - List\n")
            for b in my:
                print(f"---> {b}")

        elif cc == 'exit':
            break
to_do_list() 