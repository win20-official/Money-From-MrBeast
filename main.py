import os as o

print("Welcome to MrBeast geting money game")
name = input("What is your name? ")
print(f"OK, {name} let's start")
input()
o.system("cls")

money = input("Do you want to get MrBeast's money? yes or no: ")

if money == 'yes':
    print("MrBeast haves 0$")
    print("and you have 100,000,000$")
    input()

if money == 'no':
    print("MrBeast haves 100,000,000$")
    print("and you have 0$")
    input()