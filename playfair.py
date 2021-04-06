config = {
    "shift_horizantal":1,
    "shift_vertical":1,
    "gird_size":5,
    "key":"monnnnakaaaaacyaaaaaaaaaaa",
}


alphabit = [0]*26

for i in config["key"].lower():
    alphabit[ord(i)-ord('a')]+=1

print(alphabit)

new_key=""
for character in config["key"]:
    # print(character)
    i = ord(character)-ord('a')
    if alphabit[i] > 0 : 
        new_key+=chr(i+ord('a'))
        alphabit[i] = -1

print(new_key)
def print_grid(grid):
    for row in grid:
        print(row)

def generate_gird(key,size):
    grid = []
    for i in range(size): grid.append(['None']*size)



    k = 0
    for i in range(size):
        for j in range(size):
            if k >= len(key): break
            grid[i][j % size]=key[k]
            k+=1

    while k < 26:
        


    print_grid(grid)

generate_gird(new_key,5)
#test