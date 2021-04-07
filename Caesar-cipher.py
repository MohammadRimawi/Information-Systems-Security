def normalize_text(text): # lowers the string and removes everything but the alphabets.
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text
    
def caesar_cipher_enc (plain_text,key):
    
    key = key % 26
    plain_text = normalize_text(plain_text)
    cipher_text=""

    for i in range(len(plain_text)):
        cipher_text += chr( ( ord(plain_text[i]) - ord('a') + key) % 26 + ord('a') )
    
    return cipher_text


def caesar_cipher_dec (cipher_text,key):

    key_prime = (26 - key) % 26 
    cipher_text = normalize_text(cipher_text)
    plain_text=""

    for i in range(len(cipher_text)):
        plain_text += chr( ( ord(cipher_text[i]) - ord('a') + key_prime) % 26 + ord('a') )

    return plain_text


msg = "Hello My name is Mohammad Rimawi"
print(caesar_cipher_enc(msg,17))
print(caesar_cipher_dec(caesar_cipher_enc(msg,17),17))
