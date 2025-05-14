arr = []
pas1 = 0

for _ in range(5):
	num = list(map(int,input().split()))
	arr.append(num)

for i in arr:
    avg = (num[0] + num[1] + num[2] + num[3]) / len(num)
    if avg >= 80:
        print("pass")
        pas1 += 1
    else:
        print("fail")

print(f'합격자는 {pas1}명')