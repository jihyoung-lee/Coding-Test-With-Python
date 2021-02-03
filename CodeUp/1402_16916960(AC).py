n = input()
array = list(map(int,input().split()))
array.sort(reverse=True)
for i in array:
    print(i,end=' ')
