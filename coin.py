#카운터에는 거스름돈으로 사용하라 동전 500,100,50,10 원이 있다.
#동전은 무한히 존재하며, 손님에게 거슬러주어야 할 돈이 n원일때,
#거슬러주어야하는 동전의 최소 개수를 구하여라.


n = int(input())
count = 0
#큰 단위의 동전부터 확인 

coin = [500,100,50,10]
for i in coin:
    count += n // i
    n%=i #나머지계산 

print(count)
