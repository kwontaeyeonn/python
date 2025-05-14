# while True:
#     try:
#         n_1 = int(input("숫자: "))
#     except ValueError:
#         print("숫자만 입력하세요")
#     else:
#         print(n_1)
#         break
hap = 0
avg = 0
cnt = 0
while True:
    try:
        n = int(input("점수:"))
        cnt += 1
        hap = hap+n
    except:
        break
avg = hap/cnt
print(f'{hap:.1f}')
print(f'{avg:.1f}')