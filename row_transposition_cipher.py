import math
def normalize_text(text): # lowers the string and removes everything but the alphabets.
 
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text


def transpose(grid,key):
    new_grid = []

    mx = 0
    new_new_grid = []

    for i in range(len(grid)):
        new_new_grid.append([])

    for k in range(len(key)):
        for i in range(len(grid)):
            if key[k] == grid[i][0]:
                for j in grid[i]:
                    new_new_grid[k].append(j)

    grid = new_new_grid

    for g in grid:
        print(g)
    
    for i in range(len(grid)):
        if len(grid[i])> mx:
            mx = len(grid[i])

    for j in range(mx):
        new_grid.append([])

    for i in range(len(new_grid)):
        for j in range(len(grid)):
            new_grid[i].append("")


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[j][i]=grid[i][j]


    return new_grid
    pass

def row_transposition_enc(plain_text,key):
    data = {}

    data['key'] = key

    key = list(key)
    plain_text = normalize_text(plain_text)
    
    for i in range(len(key)):
        if key[i].isdigit():
            key[i] = int(key[i])
        elif key[i].isalpha():
            key[i] = ord(key[i].lower())-ord('a')

    data['plainText'] = plain_text

    grid = []

    for i in key:
        grid.append([i])

    for i in range(len(plain_text)):
        grid[i%len(key)].append(plain_text[i])

    grid.sort()

    data['grid'] = transpose(grid,key)

    cipher_text=""
    for i in grid:
        for j in range(1,len(i)):
            cipher_text+=i[j]

    data['cipherText'] = cipher_text.upper()
    return data
    pass

def row_transposition_dec(cipher_text,key):

    data = {}
    data['key'] = key
    cipher_text = normalize_text(cipher_text)
    key = list(key)
    
    for i in range(len(key)):
        if key[i].isdigit():
            key[i] = int(key[i])
        elif key[i].isalpha():
            key[i] = ord(key[i].lower())-ord('a')


    data['cipherText'] = cipher_text.upper()

    grid = []

    r = len(cipher_text)%len(key)
    q = int(len(cipher_text)/len(key)) + 1 


    for i in key:
        grid.append([i])
    
    grid.sort()


    for k in range(r):
        for i in range(q):
            grid[k].append(cipher_text[k*q+i])
    
    
    for k in range(len(key) - r):
        for i in range(q-1):
            grid[k+r].append(cipher_text[k*(q-1) + (r*q) +i])
    

    data['grid'] = transpose(grid,key)
    plain_text = ""
    
    count = 0
    j = 1


    while count < len(cipher_text):
        for k in key:
            for i in range(len(grid)):
                if(k == i+1):
                    count += 1
                    plain_text+=grid[i][j]
            if(count==len(cipher_text)):
                break
        j+=1
    data['plainText'] = plain_text
    # transpose(grid)
    # print(plain_text)
    return data      
    pass


# print(row_transposition_enc("attackpostponeduntiltwoam","4312567"))
print(row_transposition_dec("ttnaaptmtsuoaodwcoiknlpet","4312567"))