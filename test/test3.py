a=2
print("result = a:",a)
a+=4
print("result += 4:",a)
a-=2
print("result -= 2:",a)
a*=5
print("result *= 5:",a)
a /= 2
print("result /= 2", )
a %= 3
print("result %= 3:",a)


# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(False and True)     # False
print(False and False)    # False


# 첫 번째 값이 '참'이면 결과는 두 번째 피연자에 의해 결정되므로 두 번째 연산자의 값을 반환
print("1:", 1 and 0)
print("2:", 0 and 1)
print("3:", 1 and 2)
print("4:", 2 and 1)
print("5:", 0 and [])
print("6:", [] and 0)

# 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
print("1:", True or True)     # True
print("2:", True or False)    # True
print("3:", 1 or 0)
print("4:", 0 or 1)

# 첫 번째 값이 '참'으로 평가되면 첫 번째 값을 반환
print("5:", 1 or 2)
print("6:", 2 or 1)

