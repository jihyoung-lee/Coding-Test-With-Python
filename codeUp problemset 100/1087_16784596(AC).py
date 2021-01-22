num = int(input())
ans = 0
for i in range(0,num+1):
    ans = i + ans
    if ans >= num:
        break
print (ans)
