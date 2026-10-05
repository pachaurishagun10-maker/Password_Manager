import random
import string  
password={}

try:
    with open("password.txt" , "r") as file:
        for line in file: 
            website , password= line.strip().split(":")
            password[website]= password

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-.,?/;:'"
    password = "".join(random.choice(chars) for _ in range(10))
    return password

while True:
    print("\n~~~~~~PERSONAL_RESULT_MANAGER~~~~~~")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")