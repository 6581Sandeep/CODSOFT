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
