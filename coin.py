n = int(input())
count = 0
#큰 단위의 동전부터 확인 

coin = [500,100,50,10]
for i in coin:
    count += n // i
    n%=i #나머지계산 

print(count)
