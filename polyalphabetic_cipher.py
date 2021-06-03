def normalize_text(text): # lowers the string and removes everything but the alphabets.
 
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text

def polyalphabetic_cipher_enc(plain_text,key):
    data ={}
    plain_text = normalize_text(plain_text)
    
    data['plainText'] =plain_text

    print(key)
    key = list(key)

    new_key = []

    for i in key:
        new_key.append(str(i))
    data['key'] = "".join(new_key)



    cipher_text = ""

    for i in range(len(plain_text)):        
        cipher_text+= chr( ((ord(plain_text[i])-ord('a')) + ((key[i%len(key)])))%26 + ord('a') )
    
    # print(cipher_text)

    data['cipherText'] = cipher_text.upper()
    return data
    pass

def polyalphabetic_cipher_dec(cipher_text,key):

    data = {}

    cipher_text = normalize_text(cipher_text)

    data['cipherText'] = cipher_text.upper()
    key = list(key)

    new_key = []

    for i in key:
        new_key.append(str(i))

    data['key'] = "".join(new_key)


    plain_text = ""

    
    for i in range(len(cipher_text)):        
        plain_text+= chr( ( ord(cipher_text[i]) - ord('a') - ((key[i%len(key)])) ) %26 + ord('a'))
    
  
    data['plainText'] =plain_text

    return data


    pass

# if __name__ == "__main__":
#     s = "mohammad"
#     k = [6,8,4,2]
#     polyalphabetic_cipher_dec(polyalphabetic_cipher_enc(s,k),k)
    