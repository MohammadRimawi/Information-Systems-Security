from collections import deque

get_bin = lambda x: format(x, 'b')


p10 = [3,5,2,7,4,10,1,9,8,6]
p8 = [6,3,7,4,8,5,10,9]
p4 = [2,4,3,1]

s0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3], 
    [3,1,3,2],
]

s1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0], 
    [2,1,0,3],
]

key = int('0010010111',2)
key = get_bin(key)

ip = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(p10)):
    ip[i] = key[p10[i]-1]

LS1l = ip[0:5]
LS1r = ip[5:10]
LS1l = deque(LS1l)
LS1r = deque(LS1r)
print("IP :",ip)
print("LS1 :",LS1l,LS1r)

LS1l.rotate(-1)
LS1r.rotate(-1)

print("LS1 after SHL:",LS1l,LS1r)

stage1 = deque(LS1l)
stage1.extend(LS1r)

k1 = [0,0,0,0,0,0,0,0]

for i in range(len(p8)):
    k1[i] = stage1[p8[i]-1]

print("k1 :",k1)


LS1l.rotate(-2)
LS1r.rotate(-2)

print("LS2 after SHL:",LS1l,LS1r)

stage2 = deque(LS1l)
stage2.extend(LS1r)

k2 = [0,0,0,0,0,0,0,0]

for i in range(len(p8)):
    k2[i] = stage2[p8[i]-1]

print("k2 :",k2)




