# 20x20 크기의 2차원 리스트 d 생성
d = []

for i in range(20):
    d.append([])  #빈 리스트를 추가(행 생성)
    for j in range(20):
        d[i].append(0)  # 각 행에 0을 20번 추가 (열 생성)


# n을 입력받고, n번 동안 x, y 좌표를 입력받음
n = int(input()) 
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1  #(x, y) 위치에 1을 설정

# d 배열의 (1, 1)부터 (19, 19)까지 출력
for i in range(1, 20): 
    for j in range(1, 20): 
        print(d[i][j], end=' ')  
    print()  