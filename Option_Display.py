# ---------------------------------

# File          : Option_Display.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 15/10/2021
# Modified Date : 
# Description   : Program to display menu and details.
# Licensing     : Anup Jacob, LYIT
# ----------------------------------
from pprint import pprint


def read_courses():
    print("Selected Choice: View List of courses")
    print("The courses available in LYIT are: ")
    print("1. MSc in Devops (DO)")
    print("2. Msc in Cyber Security (CS)")
    print("3. MSc in Cloud Computing (CC)")
    courses = ('DO','CS','CC')
    return courses

def edit_courses():
    print("Selected Choice: List of courses")

def pretty_print():
    print("Selected Choice: Pretty Print data in the list")

def word_check():
    print("Selected Choice: Check for common words in the list")


if __name__ == '''__main__''':


    print("")
    print("Display Menu")
    print("------------")
    print("1. Display the list of courses in LYIT")
    a = input("Enter your Choice : ")
    if (a == '1'):
        courses = read_courses()
        print("Tuple of Courses available in LYIT is ")
        print(courses)
    elif (a == '2'):
        edit_courses()
    elif (a == '3'):
        pprint(courses)
    elif (a == '4'):
        word_check()
    else:
        print("Wrong selection")
    print("")

