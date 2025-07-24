def caesar_cipher_encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            encoded_message += chr(shifted)
        else:
            encoded_message += char
    return encoded_message


def caesar_cipher_decode(message, shift):
    return caesar_cipher_encode(message, -shift)



message = input()
shift = int(input())

encoded = caesar_cipher_encode(message, shift)
print("Encoded:", encoded)

decoded = caesar_cipher_decode(encoded, shift)
print("Decoded:", decoded)
