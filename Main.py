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
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{password}\n")

        print("Saved!")

    elif choice == "2":
        if not password:
            print("No data")
        else:
            for site,password in password.items():
                print(f"Website: {site} | Password: {password}")

    elif choice == "3":
        new_password = generate_password()
        print(f"Generated Password: {new_password}")

    elif choice == "4":
        print("Exiting Window...")
        break

    