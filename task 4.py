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