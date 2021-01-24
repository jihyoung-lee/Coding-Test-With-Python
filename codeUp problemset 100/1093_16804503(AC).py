a = int(input())
b = input().split()
li = []

for i in range(24):
    li.append(0)
for i in range(a):
    li[int(b[i])] +=1
for i in range(1,24):
    print(li[i], end=' ')
