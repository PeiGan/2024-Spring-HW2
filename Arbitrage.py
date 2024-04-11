liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}


def test(path): 
    token = {
        "tokenA": 0,
        "tokenB": 5,
        "tokenC": 0,
        "tokenD": 0,
        "tokenE": 0
    }

    for i in range (0, len(path)-1):
        x = path[i]
        y = path[i+1]
        if x < y:
            (a, b) = liquidity[(x,y)]
        else:
            (b, a) = liquidity[(y,x)]
        token[y] = b - a * b / (a + token[x])
        token[x] = 0
        # print(f"{y}:{token[y]}")
    
    return token["tokenB"]

import itertools
it = list(itertools.permutations(["tokenA", "tokenB", "tokenC","tokenD","tokenE"]))

path = []
mx = 0

for p in it:
    if p[0] != "tokenB":
        continue
    p = list(p)
    p.append("tokenB")
    ret = test(p)
    if ret > mx:
        mx = ret
        path = p

print(f"path: ",end='')
for i in range (0, len(path)):
    if i != len(path) - 1:
        print(f"{path[i]}->", end='')
    else:
        print(f"{path[i]}, ", end='')
print(f"tokenB balance={mx}")
