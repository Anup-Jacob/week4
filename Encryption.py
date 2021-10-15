# ---------------------------------

# File          : Encryption.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  15/10/2021
# Modified Date : 
# Description   : Encryption sample
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == '''__main__''':

    message = input("Enter the message to be encrypted : ")
    mess_len = len(message)
    print("\t")

    print("The message entered is :"+message)
    print("The length of the message is : "+format(mess_len))

    encrypt_message = ''

    i = mess_len - 1

    while(i >= 0):
        if(message[i]==" "):
            encrypt_message = encrypt_message + "||"
        else:
            encrypt_message = encrypt_message + message[i]
        i -= 1;

    print("The encrypted message is : "+encrypt_message)

    print("\t")
    print("Thank you for using my application")
