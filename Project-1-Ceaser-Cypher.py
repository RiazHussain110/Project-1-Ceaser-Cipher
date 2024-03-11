alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text
def decryption(cipher_text, shift_key, position_=alphabet[new_position]):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += position_
        else:
            plain_text += char
    return plain_text
what_to_do = input("Type 'Encrypt' for encryption and 'Decrypt' for decryption:\n")
text = input("Type your Message:\n")
shift = int(input("Enter a Shift Key:\n"))
if what_to_do == "Encrypt":
    encrypted_text = encryption(plain_text=text, shift_key=shift)
    print(f"Here is the text after encryption: {encrypted_text}")
elif what_to_do == "Decrypt":
    decrypted_text = decryption(cipher_text=text, shift_key=shift)
    print(f"Here is the text after decryption: {decrypted_text}")
