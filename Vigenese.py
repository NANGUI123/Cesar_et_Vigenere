from Cesar import cesar_cipher
from Cesar import alphabet
from Cesar import cesar_uncipher

def convert_password_to_list_of_keys(password):
    list_of_keys = []
    for char in password:
        list_of_keys.append(alphabet.index(char))
        return list_of_keys

    
    
def vigenere_cipher(message, password, reverse = False):
    list_of_keys = convert_password_to_list_of_keys(password)
    crypt_message = ""
    for index, char in enumerate(message):
        current_key = list_of_keys[index % len(password)]
        #crypt_message += cesar_cipher(char, ord(current_key) - 32)
        if reverse:
            crypt_message += cesar_uncipher(char, current_key)
        else:
            crypt_message += cesar_cipher(char, current_key)
    return crypt_message

print(vigenere_cipher("abc", "def"))
