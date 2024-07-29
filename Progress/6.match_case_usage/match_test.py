import os
import datetime

def runMatch():
    prompt = input("List directory (L), Read (R), or Write (W)?: ")
    match prompt:
        case 'L':
            listing()
        case 'W':
            write()
        case 'R':
            read()

def listing():
    cwd = os.getcwd()
    print(os.listdir(cwd))

def write():
    with open(f"{datetime.datetime.now()}.txt", "a") as file:
        prompt = input("What would you like to write?")
        file.write(prompt)

def read():
    listing()
    choice = input("Which of these would you like to read? ")
    with open(f"{choice}", "r") as f:
        print(f.read())

runMatch()
