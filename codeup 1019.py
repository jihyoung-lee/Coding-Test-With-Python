#코드업 기초100제 1015번
#입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.

y,m,d = input().split('.') #.으로 나누어 입력
print(y.zfill(4)+'.'+m.zfill(2)+'.'+d.zfill(2)) #zfill 함수를 이용하여 빈 자리에는 0을 집어넣도록 함 
