import os
import subprocess
import readline
import datetime

def folder_check():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")
    os.chdir("Logs")

def autocomplete():
    readline.set_completer_delims(" \t\n;")
    readline.parse_and_bind("tab: complete")
    parsed = input("Enter some text or hit tab to list directories/files: ")
    return parsed

def write():
    folder_check()
    text = input("What would you like to write? ")
    with open(f"{datetime.datetime.now()}.txt", "a") as file:
        file.write(f"{text}")

def read():
    parsed = autocomplete()
    with open(f"{parsed}", "r") as file:
        print(file.read())

def edit():
    parsed = autocomplete()
    subprocess.call(['nvim', parsed])

def main():
    prompt = input("Would you like to:\n 1. Write a new entry (w)\n 2. Read an entry (r)\n 3. Edit an entry with neovim (e)?\n")
    match prompt:
        case 'w':
            write()
        case 'r':
            read()
        case 'e':
            edit()

if __name__ == "__main__":
    main()

# Useful Resources
# https://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input
# https://parezcoydigo.wordpress.com/2012/08/11/call-vim-from-inside-a-python-script/
