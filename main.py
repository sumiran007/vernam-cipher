def vernam_decrypt(ciphertext, key):
    # Ensure the ciphertext and key are of the same length
    if len(ciphertext) != len(key):
        print("Ciphertext and key must be the same length.")
        return 
    
    # Perform XOR decryption
    plaintext_chars = []
    for c, k in zip(ciphertext, key):
        decrypted_char = chr(ord(c) ^ ord(k))
        plaintext_chars.append(decrypted_char)
    
    plaintext = ''.join(plaintext_chars)
    return plaintext

# Example usage:
ciphertext = input("Enter the text that needs to be decrypted: ")
key = input("Enter the key: ")

if len(ciphertext) == len(key):
    plaintext = vernam_decrypt(ciphertext, key)
    print(f"Decrypted Text: {plaintext}")
else:
    print("Ciphertext and key must be the same length.")