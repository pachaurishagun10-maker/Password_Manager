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
    print("1. Add Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        site=input("Enter the website name: ")
        password=input("Enter your password: ")
        password[site] = password
