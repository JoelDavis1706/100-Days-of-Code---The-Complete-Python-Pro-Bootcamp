# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            encrypt_index = (alphabet.index(letter) + shift_amount) % 26
            encrypted_text += alphabet[encrypt_index]

    print(f"Your encoded text is : {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            decrypt_index = (alphabet.index(letter) - shift_amount) % 26
            decrypted_text += alphabet[decrypt_index]

    print(f"Your encoded text is : {decrypted_text}")

if direction == "encode":

    encrypt(original_text=text,shift_amount=shift)

elif direction == "decode":

    decrypt(original_text=text, shift_amount=shift)

else:
    print("Sorry we couldn't quite understand what you wanted to type, please type encode or decode.")




