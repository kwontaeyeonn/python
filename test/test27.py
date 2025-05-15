def abs(num):
    return num if num >= 0 else -num #num >= 0 이 참이면 num 반환, 거짓이면 -num 반환

num = int(input("숫자를 입력하세요: "))

try:
    print(f"|{num}| = {abs(num)}")

except ValueError:
    print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")