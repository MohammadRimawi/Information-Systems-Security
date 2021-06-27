import math
from pprint import pprint
def normalize_text(text): # lowers the string and removes everything but the alphabets.
 
    text = text.lower()
    new_text = ""

    for charater in text:
        if charater.isalpha(): new_text+=charater

    return new_text

def rail_fence_enc(plain_text,key,subtype):
    data = {}

    plain_text = normalize_text(plain_text)

    data['plainText'] = plain_text
    data['key'] = key
    data['subtype'] = subtype

    grid = get_grid(plain_text,key,subtype,"enc")

    data['grid'] = grid
   
    cipher_text=""
    
    for i in grid:
        for j in i:
            if j != " ":
                cipher_text += j
        cipher_text += " "
    data['cipherText'] = cipher_text.upper()
    return data
    pass

def rail_fence_dec(cipher_text,key,subtype):
    
    data = {}
    
    cipher_text = normalize_text(cipher_text)

    data['cipherText'] = cipher_text.upper()
    data['key'] = key
    data['subtype'] = subtype

    grid = get_grid(cipher_text,key,subtype,"dec")

    data['grid'] = grid
   
    plain_text=""
    
    j = 0
    i = 0
    
    while j < len(grid[0]):
        while  i < len(grid):
            if grid[i][j] != " ":
                plain_text+=grid[i][j]
            i+=1
        i = 0
        j+=1

    data['plainText'] = plain_text
  
    return data
    pass

def get_grid(text,key,subtype,type):
    if type == "enc":
        grid = []
        for i in range(key):
            grid.append([])
        
        for i in range(len(text)):
            for j in range(key):
                grid[j].append(" ")

        if subtype == "zig-zag":

            step = list(range(key))
            rev = step[1:key-1]
            for i in range(len(rev)):
                step.append(rev[len(rev)-1-i])

            # print(step)
    
            s = 0
            for i in range(len(text)):
                grid[step[s%len(step)]][i] = text[i]
                s+=1

        elif subtype == "normal":

            for i in range((len(text))):
                grid[i%key][i]=text[i]
        
        return grid
    elif type == "dec":
        grid = []
        grid = get_grid(text,key,subtype,"enc")

        i = 0
        j = 0
        k = 0
        while k < len(text):

            while i < len(grid):

                while j < len(grid[0]):
                    # print(k,i,j)
                    if grid[i][j] != " ":
                        grid[i][j] = text[k]
                        k+=1
                        if(k >= len(text)):
                            return grid
                    j+=1
                    
                j = 0
                i+=1
        pass


    return grid


# pprint(rail_fence_enc("wearediscoveredfleeatonce",5,"zig-zag"),width=500)