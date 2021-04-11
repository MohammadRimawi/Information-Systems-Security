import math
def rail_fence_enc(plain_text,key):
    cipher_text=""
    for i in range(0,key):
        for j in range(i,len(plain_text),key):
            cipher_text+=plain_text[j]
            # print(plain_text[j],end="")
    return cipher_text

def rail_fence_dec(cipher_text,key):
    k = math.ceil(len(cipher_text)/key)-1
    m = len(cipher_text)%key
    counter = 0
    plain_text=""
    for j in range(1,int(len(cipher_text)/key)+2,1):
        for i in range(key):
            c=i*(k)+j-int(i==0)
            if c < len(cipher_text) and counter <len(cipher_text):
                counter+=1
                # print(c,end =" ")
                plain_text+=cipher_text[c]
                # print(cipher_text[c],end=" ")
    return plain_text
        # print("")


# rail_fence_enc("wearediscoveredfleeatonce",3)
print(rail_fence_enc("wearediscoveredfleeatonce",3))
# print(rail_fence_dec(rail_fence_enc("wearediscoveredfleeatonce",5),))

