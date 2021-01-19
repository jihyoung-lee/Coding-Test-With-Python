a = int(input())
a_list=[]
ans = 0
for i in range(0,a):
    a_list.append(i)
    a_list.sort(reverse=True)
for k in a_list:
    print(k)
