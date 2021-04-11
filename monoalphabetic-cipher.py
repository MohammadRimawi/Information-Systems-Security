def monoalphabetic_cipher_enc(plain_text,key):
    key = list(key)
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += key[ord(plain_text[i])-ord('a')]
    print(cipher_text)
    return cipher_text

def monoalphabetic_cipher_dec(cipher_text,key):
    key = list(key)
    plain_text = ""
    key_prime = [None]*26
    for i in range(len(key)):
        key_prime[ord(key[i])-ord('a')] = chr(i+ord('a'))

    for i in range(len(cipher_text)):
         plain_text += key_prime[ord(cipher_text[i])-ord('a')]

    print(plain_text)
    return plain_text

if __name__ == "__main__":
    s = "mohammad"
    k = "qazwsxedcrfvtgbyhnujmikolp"

    monoalphabetic_cipher_dec(monoalphabetic_cipher_enc(s,k),k)
