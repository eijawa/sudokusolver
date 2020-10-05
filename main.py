from pprint import pprint

def solve(table):
    x,y = -1,-1

    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                x,y = j,i
                break
        if x != -1:
            break

    if x == -1:
        return table

    r = pick_range(x,y,table)

    if len(r) == 0:
        return None

    for v in r:
        table[y][x] = v
        table_copy = solve(table)
        if table_copy != None:
            table = table_copy
            break
        else:
            table[y][x] = 0

    return table_copy

def pick_range(x,y,table):
    r = list(range(1,10))

    for col in table[y]:
        if col in r:
            r.remove(col)
    
    for row in table:
        if row[x] in r:
            r.remove(row[x])

    xs = int(x / 3) * 3
    ys = int(y / 3) * 3

    for row in table[ys:ys+3]:
        for col in row[xs:xs+3]:
            if col in r:
                r.remove(col)

    return r

if __name__ == '__main__':
    table = [
        [0,0,9,0,8,0,5,0,0],
        [0,1,0,0,0,0,0,0,2],
        [5,0,0,4,3,0,8,0,6],
        [9,0,6,0,0,5,0,0,3],
        [0,5,0,0,7,0,0,0,0],
        [0,4,0,0,0,8,1,0,9],
        [0,0,1,3,0,0,0,0,4],
        [0,0,4,0,0,9,6,0,0],
        [8,3,0,0,6,0,0,1,0]
    ]

    table = solve(table)
    pprint(table)