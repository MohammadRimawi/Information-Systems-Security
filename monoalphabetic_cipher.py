def normalize_text(text): # lowers the string and removes everything but the alphabets.
    print(text,"***********")
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text

def monoalphabetic_cipher_enc(plain_text,key):
    
    data ={}
    
    plain_text = normalize_text(plain_text)
    data['plainText'] = plain_text
    
    key = normalize_text(key)
    
    data['key'] = key

    key = list(key)
    

    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += key[ord(plain_text[i])-ord('a')]

    data['cipherText'] = cipher_text.upper()
    return data

def monoalphabetic_cipher_dec(cipher_text,key):

    data = {}

    cipher_text = normalize_text(cipher_text)

    data['cipherText'] = cipher_text.upper()

    key =normalize_text(key)

    data['key'] = key

    key = list(key)


    plain_text = ""
    key_prime = [None]*26
    for i in range(len(key)):
        key_prime[ord(key[i])-ord('a')] = chr(i+ord('a'))

    for i in range(len(cipher_text)):
         plain_text += key_prime[ord(cipher_text[i])-ord('a')]

    data['keyPrime'] = "".join(key_prime).upper()
    data['plainText'] = plain_text
    return data

# if __name__ == "__main__":
#     s = "mohammad"
#     k = "qazwsxedcrfvtgbyhnujmikolp"

#     monoalphabetic_cipher_dec(monoalphabetic_cipher_enc(s,k),k)
