import datetime

x = datetime.datetime.now()

with open(f"{x}.txt", "a")as file:
    file.write("This is a text document titled with date and time")
