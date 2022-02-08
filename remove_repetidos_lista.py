lis = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

def remove_repetidos(lis):
    l = []
    for i in lis:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lis = remove_repetidos(lis)
print (lis)
