import string
alphabet = string.printable
def cesar_cipher(crypted_message, key):
    alphabet = string.printable
    crypt_message = ""
    for char in crypted_message:
            inedx_char = alphabet.index(char)
            index_decrypt_char = (inedx_char + key) % 26
            crypt_message += alphabet[index_decrypt_char]
    return crypt_message

def cesar_uncipher(crypted_message, key):
    return cesar_cipher(crypted_message, -key)

def brute_dechiffrer(crypted_message):
    for possible_key in range(len(alphabet)):
       # print(cesar_uncipher(crypted_message, possible_key))
        print("Décalage de ", possible_key, ":", cesar_uncipher(crypted_message, possible_key))

cesar = cesar_cipher("abc", 3)
print(cesar)
decesar = cesar_uncipher("def", -3)
print(decesar)
brute_dechiffrer("def")