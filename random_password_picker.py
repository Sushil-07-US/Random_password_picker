# Simple program for random password picker.

import random 
ran_things = ("ASDFGHJKLMNBVCXZQWERTYUIOPasdfghjklzxcvbnm1234567890!@#$%^&*")
lis_thing = list(ran_things)
try:
    Pass = int(input("Enter the length of password: "))

except ValueError as e:
    print("Please enter the valid numbers",e)

if Pass > 8 and Pass < 16:
    ran_password = ""
    for _ in range(Pass):
        ran_password += random.choice(ran_things)

    

    print(f"Your Password is: {ran_password}")
         
    
else:
    print("Password must be greater than 8 and Less than 16 characters")