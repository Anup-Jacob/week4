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

if __name__ == '''__main__''':

    a=0
    print("")
    print("Display Menu")
    print("------------")
    print("1. Display the list of courses in LYIT")
    a=input("Enter your Choice : ")
    if (a == 1):
        read_courses()
    else:
        print("Wrong selection")
    print("")

