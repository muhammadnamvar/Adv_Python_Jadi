# importing regex
import re


# Checking username
pattern = '^[A-Za-z]+[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'
username = input("Please Enter username: ")
accept = re.search(pattern, username)
while not accept:
    print("Please Correct your Email Fucking Format")
    username = input("Please Enter username: ")
    accept = re.search(pattern, username)
print("Accept your Email, Thank you!!!")


# Checking password
pattern = '^[A-Za-z0-9]{8,20}$'
password = input("Please Enter Password: ")
accept = re.search(pattern, password)
while not accept:
    print("Please Correct your Password Fucking Format")
    password = input("Please Enter Password: ")
    accept = re.search(pattern, password)
print("Accept your Password, Thank you!!!")
