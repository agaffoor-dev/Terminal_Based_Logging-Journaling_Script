import os
import datetime

if not os.path.exists("Logs"):
    os.mkdir("Logs")

os.chdir("Logs")

title = datetime.datetime.now()

text = input("What would you like to write? ")

with open(f"{title}.txt", "a") as file:
    file.write(f"{text}")
