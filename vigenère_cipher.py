def polyalphabetic_cipher_enc(plain_text,key):
    key = list(key)

    cipher_text = ""

    
    for i in range(len(plain_text)):        
        cipher_text+= chr( ((ord(plain_text[i])-ord('a')) + (ord(key[i%len(key)])-ord('a')))%26 + ord('a') )
    
    print(cipher_text)
    return cipher_text
    pass

def polyalphabetic_cipher_dec(cipher_text,key):
    key = list(key)

    plain_text = ""

    for i in range(len(cipher_text)):        
        plain_text+= chr( ( ord(cipher_text[i]) - ord('a') - (ord( key[i%len(key)] ) - ord('a')) ) %26 + ord('a'))
    
    print(plain_text)
    return plain_text
    pass

if __name__ == "__main__":
    s = "mohammad"
    k = "jubiter"
    polyalphabetic_cipher_dec(polyalphabetic_cipher_enc(s,k),k)
    