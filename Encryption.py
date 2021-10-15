# ---------------------------------

# File          : Encryption.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  15/10/2021
# Modified Date : 
# Description   : Encryption sample using reverse and Pipe(|) symbol
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == '''__main__''':

    message = input("Enter the message to be encrypted : ")
    mess_len = len(message)
    # Input from the user asking for the message to be encrypted
    print("\t")

    #print("The message entered is :"+message)
    # Message input check
    print("The length of the message is : "+format(mess_len))
    # Message length check
    encrypt_message = ''
    # initialising the encrypt variable
    i = mess_len - 1

    while(i >= 0):
        if(message[i]==" "):
            encrypt_message = encrypt_message + "||"
        else:
            encrypt_message = encrypt_message + message[i]
        i -= 1;
    # The reversing and Pipe(|) addition functionality as part of encryption

    print("The encrypted message is : "+encrypt_message)
    # Displaying the encrypted message
    print("\t")
    print("Thank you for using my application")
