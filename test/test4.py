mk, mw = map(int, input().split())
kk, kw = map(int, input().split())

print(mk>kk and mw>kw)


n = int(input())

print("숫자를 입력 받아 홀수이면 True 아니면 False 출력", "\n", (n/2)!=0)




w, h, b = map(int,input().split())

p = w*h*b/8/1024/1024
print(format(p, ".2f"),"MB")

n = int(input())

cnt = 0
a = 0

for i in range(n):
    cnt += i
    a += 1
    
    if cnt>=n:
        print(a)
        break