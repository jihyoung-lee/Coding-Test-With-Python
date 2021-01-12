a,b,c=input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(0,a):
    for k in range(0,b):
        for m in range(0,c):
            print(i,k,m)
print(a*b*c)
