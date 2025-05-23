print("*** 도형 넓이 계산***")
print("1. 삼각형 2. 사각형 3. 원")

a = int(input("도형종류:"))
b = int(input("밑변(cm):"))
c = int(input("높이(cm):"))

n = 0
if a==1:
    n = b * c / 2
    print("삼각형의 넓이는 ", n, "cm^2 입니다.", sep='')
elif a==2:
    n = b * c 
    print("사각형의 넓이는 ", n, "cm^2 입니다.", sep='')
else:
    b = b/2
    n = b**b * 3.14 
    print("원의 넓이는 ", n, "π입니다.", sep='')
