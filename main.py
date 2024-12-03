def vernam_decrypt(ciphertext, key):
    # Ensures the ciphertext and key are of the same length
    if len(ciphertext) != len(key):
        print("Ciphertext and key must be the same length.")
        return 
    
    #XOR decryption
    plaintext_chars = []
    for c, k in zip(ciphertext, key):
        decrypted_char = chr(ord(c) ^ ord(k))
        plaintext_chars.append(decrypted_char)
    
    plaintext = ''.join(plaintext_chars)
    return plaintext

#input key and text to be decrypted
ciphertext = input("Enter the text that needs to be decrypted: ")
key = input("Enter the key: ")
#checks to see if decryption is possible
if len(ciphertext) == len(key):
    plaintext = vernam_decrypt(ciphertext, key)
    print(f"Decrypted Text: {plaintext}")
else:
    print("Ciphertext and key must be the same length.")
