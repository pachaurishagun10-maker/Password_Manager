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