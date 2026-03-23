"""
i first thought to research about the shuffle function to see if i could control how much it shuffled, or what it shuffled too. Then i realized I probably need to use indexing and a loop to replace each character with the shifted one. Similar to the bulls and cows program, i used index() to find the index of of our text in the alphabet list. I messed around and found out if i plus a number, the indexing shifts by that amount. using that, I decided to print out the shifted index in order to have our encrypted message

for perserving uppercase letters, i created a new list filled with only uppercase letters. If the letter was not in the lowercase list, it would check the uppercase list and shift the index of that uppercase letter.

for looping around the alphabet, if the shifted index was grrater than the highest index in the list, it would be subtracted by 26 to restart the index to the 0 and count up from there if needed. The same was done for decryption, but its subtracted.

for characters that were not in either alphabet list, they would be appended to the string as normal.

    """
import string
no_punct = str.maketrans('','',string.punctuation)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
encrypted_msg = []

def encrypt(message, shift_amount):
    msg_list = list(message) #converting it to a list so each letter can be iterable
    for l in msg_list:
        if l in alphabet:
            shifted = alphabet.index(l)+shift_amount #finds the letter index in alphabet, and increases that index by the shift amount
            if shifted > 25:
                shifted = shifted - 26 #if shifted index is out of bonds, it goes back to the beginning of the alphabet list
            encrypted_msg.append(alphabet[shifted])

        elif l in upper_alphabet:
            shifted = upper_alphabet.index(l) + shift_amount #if the letter is uppercase, it takes from the upppercase list instead
            if shifted > 25:
                shifted = shifted - 26
            encrypted_msg.append(upper_alphabet[shifted])

        elif l not in alphabet and l not in upper_alphabet:
            encrypted_msg.append(l)

    print("You're encrypted message is:")
    print(''.join(map(str, encrypted_msg))) #prints out the encrypted message in a string format

def decrypt(message,shift_amount):
    msg_list = list(message)
    for l in msg_list:

        if l in alphabet:
            shifted = alphabet.index(l)-shift_amount
            if shifted < 0:
                shifted = shifted + 26 #if shifted index is out of bonds it brings it back in bounds
            encrypted_msg.append(alphabet[shifted])

        elif l in upper_alphabet:
            shifted = upper_alphabet.index(l)-shift_amount
            if shifted < 0:
                shifted = shifted + 26 #if shifted index is out of bonds it brings it back in bounds
            encrypted_msg.append(upper_alphabet[shifted])


        elif l not in alphabet and l not in upper_alphabet:
            encrypted_msg.append(l)

    print("You're decrypted message is:")
    print(''.join(map(str, encrypted_msg)))


def main():
    print("Encrypt or Decrypt a message in Ceaser Cipher by giving the shift amount!")
    print("-"*30)

    message = input("Enter your message: ")

    while True:
        e_or_d = input("Are you looking to encrypt or decrypt your message? (encrypt/decrypt): ").translate(no_punct) #e and d stand for encrypt/decrypt
        if e_or_d.lower() == 'encrypt':
            break
        elif e_or_d.lower() == 'decrypt':
            break
        else:
            print("Please respond with 'encrypt' or 'decrypt'")
            print("-"*15)

    while True:
        try:
            shift_amount = int(input("Type in the shift amount: "))
            break
        except ValueError: #edgecase for non digit values
            print("Please type in a positive integer.")
            print("-"*15)

    if e_or_d == 'encrypt':
        encrypt(message, shift_amount)
    elif e_or_d == 'decrypt':
        decrypt(message, shift_amount)

main()
