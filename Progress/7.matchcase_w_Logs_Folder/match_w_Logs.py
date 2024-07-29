import os
import datetime

def write():
    prompt = input("What would you like to write?\n ")
    with open(f"{datetime.datetime.now()}.txt", "a") as file:
        file.write(prompt)

def foldercheck():
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')
    os.chdir('Logs')

def directory_listing():
    print(os.listdir(os.getcwd()))

def prompting():
    foldercheck()
    prompt = input("Would you like to write a new entry (W) or list entries (L)? ")
    match prompt:
        case 'L':
            directory_listing()
        case 'W':
            write()

prompting()
