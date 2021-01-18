num = input().split()
num = list(map(int,num))

for i in num:
    if i%2==0:
        print('even') #짝수
    else:
        print('odd') #홀수
