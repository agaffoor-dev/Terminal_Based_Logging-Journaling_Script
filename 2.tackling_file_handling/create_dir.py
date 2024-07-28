import os

if not os.path.exists("Logs"):
    os.mkdir("Logs")

os.chdir("Logs")
print(os.getcwd())
