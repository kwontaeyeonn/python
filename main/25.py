a, b = input().split(',')

b = int(b)

if b==1 or b==2 or b==3 or b==4:
    pass
else:
        print("존재하지 않습니다.")

n = int(a[0:2])

if b==1 or b==2:
    n = 100 - n + 26
    print("현재나이는 ", n, "살 입니다.", sep='')

elif b==3 or b==4:
    n = 26 - n
    print("현재나이는 ", n, "살 입니다", sep='')