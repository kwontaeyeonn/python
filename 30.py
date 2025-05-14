count = 0
sum = 0
avg = 0

while True:
    n = int(input("점수:"))
    if n==-1:
        break
    elif n!=-1:
        sum += n
        avg += n
        count = count + 1



print(10*'=')
avg = int(sum)/int(count)
print(f"합계:{sum:5.1f}")
print(f"평균:{avg:5.1f}")