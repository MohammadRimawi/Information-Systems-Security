from re import split


def normalize_text(text): # lowers the string and removes everything but the alphabets.
 
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text

def remove_duplicates(key):
    alph = [False]*25
    new_key = []

    for i in key:
        if(i == "j"): i = "i"
        if  not alph[ord(i)-ord('a')]:
            new_key.append(i)
            alph[ord(i)-ord('a')] = True
    return new_key
    pass


def get_grid(key):
    grid = [
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
            ["","","","",""],
           ]

    alph=[False]*25

    for i in key:
        if(i == "j"): i = "i"
        if i > 'i':
            alph[ord(i)-ord('a')-1]=True
        else:
            alph[ord(i)-ord('a')]=True

    print(alph)

    k = 0
    for i in range(5):
        for j in range(5):
            if(k < len(key)):
                grid[i][j] = key[k]
                k+=1
            else:
                for a in range(25):
                    if alph[a]==False:
                        if(chr(a+ord('a'))>'i'):
                            grid[i][j] = chr(a+ord('a')+1)
                        else:
                            grid[i][j] = chr(a+ord('a'))
                        alph[a]=True
                        break


    return grid
    pass

def shift(grid,a,b,type):
    indx_a = [-1,-1]
    indx_b = [-1,-1]

    new_a = ""
    new_b = ""

    for i in range(5):
        for j in range(5):
            if grid[i][j] == a:
                indx_a = [i,j]
            if grid[i][j] == b:
                indx_b = [i,j]
    if type == "enc":
        if indx_b[0] == indx_a[0]: #shift right
            new_a = grid[indx_a[0]][(indx_a[1]+1)%5]
            new_b = grid[indx_b[0]][(indx_b[1]+1)%5]
        elif indx_b[1] == indx_a[1]: #shift left
            new_a = grid[(indx_a[0]+1)%5][indx_a[1]]
            new_b = grid[(indx_b[0]+1)%5][indx_b[1]]
        else: # shift diagonal
            new_a = grid[indx_a[0]][indx_b[1]]
            new_b = grid[indx_b[0]][indx_a[1]]
    elif type == "dec":
        if indx_b[0] == indx_a[0]: #shift right
            new_a = grid[indx_a[0]][(indx_a[1]-1)%5]
            new_b = grid[indx_b[0]][(indx_b[1]-1)%5]
        elif indx_b[1] == indx_a[1]: #shift left
            new_a = grid[(indx_a[0]-1)%5][indx_a[1]]
            new_b = grid[(indx_b[0]-1)%5][indx_b[1]]
        else: # shift diagonal
            new_a = grid[indx_a[0]][indx_b[1]]
            new_b = grid[indx_b[0]][indx_a[1]]

    print(new_a+new_b)
    return new_a,new_b
    pass
def play_fair_enc(plain_text,key):

    data = {}

    plain_text = normalize_text(plain_text)
    data["plainText"] = plain_text

    key = normalize_text(key)
    key = remove_duplicates(key)

    data['key'] = "".join(key)
    
    g = get_grid(key)

    data['grid'] = g

    plain_text = list(plain_text)
    for i in range(1,len(plain_text),2):
        if plain_text[i] == plain_text[i-1]:
            plain_text.insert(i,'x')
            print (plain_text[i] ,plain_text[i-1])

    cipher_text = []

    splitList = []
    for i in range(0,len(plain_text),2):
        
        a = plain_text[i]
        b = plain_text[i+1]
        
        new_a,new_b = shift(g,a,b,type="enc")

        splitList.append(a+b)

        cipher_text.append(new_a+new_b)

    cipher_text = "".join(cipher_text).upper()
    data["splitList"] = splitList
    data['cipherText'] = cipher_text
    # print(key)
    # print(plain_text)
    # print(cipher_text)
    
    # print(data)
    return data
    pass


def play_fair_dec(cipher_text,key):

    data = {}

    cipher_text = normalize_text(cipher_text)
    data["cipherText"] = cipher_text.upper()

    key = normalize_text(key)
    key = remove_duplicates(key)

    data['key'] = "".join(key)
    
    g = get_grid(key)

    data['grid'] = g

    cipher_text = list(cipher_text)

    plain_text = []

    splitList = []
    for i in range(0,len(cipher_text),2):
        
        a = cipher_text[i]
        b = cipher_text[i+1]
        
        new_a,new_b = shift(g,a,b,type="dec")

        splitList.append(a+b)

        plain_text.append(new_a+new_b)

    plain_text = "".join(plain_text)
    data["splitList"] = splitList
    data['plainText'] = plain_text
    
    # print(data)
    return data
    pass






# play_fair_enc("balloon","monarchy")
# play_fair_dec("IBSUPMNA", "monarchy")
