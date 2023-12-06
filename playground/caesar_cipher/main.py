alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Enter your text: \n")
shift = int(input("Enter the shift number: \n"))

# First create encrypt
def encrypt(plain_text, shift):
    encrypted_text = ''
    for letter in plain_text:
        # find the letter index
        idx = alphabet.index(letter)
        new_idx = idx + shift
        while new_idx >= 26:
            new_idx -= 26
        shifted_letter = alphabet[new_idx]
        encrypted_text += shifted_letter
    print(encrypted_text)

def decrypt(cipher_text, shift):
    decrypted_text = ''
    for letter in cipher_text:
        idx = alphabet.index(letter)
        new_idx = idx - shift
        while new_idx < 0:
            new_idx += 26
        shifted_letter = alphabet[new_idx]
        decrypted_text += shifted_letter
    print(decrypted_text)

if direction == 'encode':
    encrypt(text,shift)
else:
    decrypt(text,shift )





