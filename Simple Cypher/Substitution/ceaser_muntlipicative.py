'''The process of muntlipicative cyper is same as addative cypher but instead of adding the shift
we muntliply the shift with the index of the letter in the letter set and then take the mod of 26
but important is decryprion part in which we have to find the inverse of the shift to decrypt the
message'''
'''Inverse can be found by using the extended euclidean algorithm in which we find the gcd of the
shift and 26 and then we find the inverse of shift it is not simple as dividing and gcd of shift
and 26 should be 1'''

#basic implementation of ceaser cypher
def encrypt(message, shift):
    '''encrypts a message using the ceaser cypher'''
    letter_set=[x for x in 'abcdefghijklmnopqrstuvwxyz']
    message=message.lower()
    encrypted_message=''
    for i in message:
        if i in letter_set:
            encrypted_message = encrypted_message + letter_set[(letter_set.index(i)*shift)%26]
    return encrypted_message
