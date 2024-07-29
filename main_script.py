import os
import datetime

def folder_check():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")
    os.chdir("Logs")

def write():
    text = input("What would you like to write? ")
    title = datetime.datetime.now()
    with open(f"{title}.txt", "a") as file:
        file.write(f"{text}")

folder_check()
write()
