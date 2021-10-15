# ---------------------------------

# File          : Option_Display.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 15/10/2021
# Modified Date : 
# Description   : Program to display menu and details.
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

def read_courses():
    print("Tuple of courses")

def edit_courses():
    print("List of courses")

def pretty_print():
    print("Pretty Print data in the list")

def word_check():
    print("Check for common words in the list")


if __name__ == '''__main__''':

    a=0
    print("")
    print("Display Menu")
    print("------------")
    print("1. Display the list of courses in LYIT")
    a = input("Enter your Choice : ")
    if (a == '1'):
        read_courses()
    elif (a == '2'):
        edit_courses()
    elif (a == '3'):
        pretty_print()
    elif (a == '4'):
        word_check()
    else:
        print("Wrong selection")
    print("")

