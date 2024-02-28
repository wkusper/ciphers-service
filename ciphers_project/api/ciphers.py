def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        c_encoded = ord(c) + shift
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text
