# ---------------------------------

# File          : OS_details.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 11/10/2021
# Modified Date : 15/10/2021
# Description   : Displaying the machine and Operating System details
# Licensing     : Anup Jacob, LYIT
# ----------------------------------
import os
import platform
import sys
# importing the standard modules of python to fetch the sys, os and related information from the machine


def os_details():
    # information regarding the Operating system and the machine details are displayed in the body of this function
   print("")
   print("The owner of the PC : " + os.environ["USERNAME"])
    # Displays the name of the owner of the machine.
   #print("The name of the machine : " + os.environ["COMPUTERNAME"])
   print("The name of the machine : " + platform.node())
    #Displays the name of the machine.
   print("The processor in the machine :  : "+platform.machine())
    # Displays the processor of the machine.
   #print("The processor in the machine : " + os.environ["PROCESSOR_ARCHITECTURE"])
   print("The number of processors in the system : " + os.environ["NUMBER_OF_PROCESSORS"])
    # Displays the number of processors of the machine.
   print("\nThe OS and version of the system is : " + platform.system() + " " + platform.release())
    # Displays the OS and the version used in the machine.

if __name__ == '''__main__''':
    os_details()
    # os_details function is called to get the details of the Operating System
    python_path = sys.exec_prefix
    print("\nThe path in which the current file is present : "+python_path)
    # infomation regarding the python file path is displayed here
    python_version = sys.path[5]
    print("The python version used in my system: "+python_version[17:len(python_version)])
    # infomation regarding the python version is displayed here

    #print(sys.path)
    # print function to fetch the details based on the position during initial phase of programming