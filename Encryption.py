# ---------------------------------

# File          : Encryption.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  15/10/2021
# Modified Date : 
# Description   : Encryption sample using reverse and Pipe(|) symbol
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import time

def timecounter(messlen):

    print("Loading ....")
    for i in range (1,messlen+1):
        time.sleep(1)
        print(i)
        messlen -= 1
    # Added loading and time counter print functionality


if __name__ == '''__main__''':

    message = input("Enter the message to be encrypted : ")
    mess_len = len(message)
    # Input from the user asking for the message to be encrypted
    print("\t")

    #print("The message entered is :"+message)
    # Message input check

    encrypt_message = ''
    # initialising the encrypt variable
    i = mess_len - 1
    timecounter(mess_len)
    while(i >= 0):
        if(message[i]==" "):
            encrypt_message = encrypt_message + "||"
        else:
            encrypt_message = encrypt_message + message[i]
        i -= 1;
    # Encryption process
    print("")
    print("The length of the message is : "+format(mess_len))
        # Message length check
    # The reversing and Pipe(|) addition functionality as part of encryption

    print("The encrypted message is : "+encrypt_message)
    # Displaying the encrypted message
    print("\t")
    print("Thank you for using my application")
