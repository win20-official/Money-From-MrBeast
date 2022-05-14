import os as o
from getpythonfiles import getbypath

path = o.getcwd()
getbypath.path(f"{path}/intro/main.py")
o.system("cls")

money = input("Do you want get MrBeast money? yes or no: ")

if money == 'yes':
    print("MrBeast have 0$")
    print("and you have 100,000,000$")
    input()

if money == 'no':
    print("MrBeast have 100,000,000$")
    print("and you have 0$")
    input()