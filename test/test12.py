n = int(input())
mx = 0
cnt = 0
while True:
	cnt += 1
	num = int(input())
	if cnt == n:
		break
	if num < mn:
		mn = num
	if num > mx:
		mx = num
print(f'최댓값은 {mx}, 최소값은 {mn}')
