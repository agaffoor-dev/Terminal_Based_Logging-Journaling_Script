import os
import readline

def foldercheck():
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')
    os.chdir('Logs')

def autocomplete():
    readline.set_completer_delims(" \t\n;")
    readline.parse_and_bind("tab: complete")
    parsed = input("Enter some text or hit tab to list directories/files: ")
    return parsed

def read():
    parsed = autocomplete()
    with open(f"{parsed}", "r") as file:
        print(file.read())

read()
