'''ceaser cypher is a simple cypher that shifts the alphabet by a certain amount of letters
to encrypt a message it was used by julius ceaser to encrypt his messages its a subtitution
cypher which means it replaces letters with other letters because of this it is very easy to
break and is not used in modern cryptography'''

#basic implementation of ceaser cypher
def encrypt(message, shift):
    '''encrypts a message using the ceaser cypher'''
    letter_set=[x for x in 'abcdefghijklmnopqrstuvwxyz']
    message=message.lower()
    encrypted_message=''
    for i in message:
        if i in letter_set:
            encrypted_message = encrypted_message + letter_set[(letter_set.index(i)+shift)%26]
    return encrypted_message

def decrypt(message, shift):
    '''decrypts a message using the ceaser cypher'''
    letter_set=[x for x in 'abcdefghijklmnopqrstuvwxyz']
    message=message.lower()
    decrypted_message=''
    for i in message:
        if i in letter_set:
            decrypted_message = decrypted_message + letter_set[(letter_set.index(i)-shift)%26]
    return decrypted_message

if __name__ == '__main__':
    #main function
    print("1 to encrypt a message and choice 2 to decrypt a message")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift: "))
        print("The encrypted message is: ", encrypt(message, shift))
    elif choice == 2:
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift: "))
        print("The decrypted message is: ", decrypt(message, shift))
    else:
        print("Invalid choice")