import os


def main():
    if not os.path.exists("mrclean.config"):
        print("where is my config file? :(")
    print("Hello World!")
