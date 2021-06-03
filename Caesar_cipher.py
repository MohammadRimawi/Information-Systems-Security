def normalize_text(text): # lowers the string and removes everything but the alphabets.
    print(text,"***********")
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text
    
def caesar_cipher_enc (plain_text,key):
    
    plain_text = normalize_text(plain_text)
    data = {}
    data['key'] = key
    data['plainText'] = plain_text

    key = key % 26
    data['key0'] = key
   
    cipher_text=""

    for i in range(len(plain_text)):
        cipher_text += chr( ( ord(plain_text[i]) - ord('a') + key) % 26 + ord('a') )
    data['cipherText']=cipher_text.upper()
    
    alph=[]
    for i in range(26):
        alph.append(chr(( i - key)%26 + ord('A')))
    
    data['alph']=alph
    return data


def caesar_cipher_dec (cipher_text,key):

    data = {}

    cipher_text = normalize_text(cipher_text)

    data['cipherText'] = cipher_text.upper()
    
    data['key'] = key
    
    key = key % 26
    data['key0']=key

    key_prime = (26 - key) % 26 

    data['keyPrime'] = key_prime
    plain_text=""

    for i in range(len(cipher_text)):
        plain_text += chr( ( ord(cipher_text[i]) - ord('a') + key_prime) % 26 + ord('a') )
    data['plainText'] = plain_text

    alph=[]
    for i in range(26):
        alph.append(chr(( i - key)%26 + ord('A')))
    
    data['alph']=alph
    return data

def caesar_cipher_brute_force(cipher_text):
    data = {}
    cipher_text = normalize_text(cipher_text)

    data['cipherText'] = cipher_text
    data['tries'] = []
    for key in range(26):
        plain_text = ""
        for i in range(len(cipher_text)):
            plain_text += chr( ( ord(cipher_text[i]) - ord('a') + key) % 26 + ord('a') )
        data['tries'].append([key,plain_text])
    return data
        
# msg = "Hello My name is Mohammad Rimawi"
# print(caesar_cipher_enc(msg,17))
# print(caesar_cipher_dec(caesar_cipher_enc(msg,17),17))
