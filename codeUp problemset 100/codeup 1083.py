a = int(input())
sam = []
for i in range(1,a+1):
    if (i%3 == 0):
        i = 'X'
        sam.append(i)
    else :
        sam.append(i)
print(' '.join(map(str, sam)))
