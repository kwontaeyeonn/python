import random, time
w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
n = 0
q = 1
print("[타자게임]준비되면 엔터")

while True:
    a = random.sample(w,5)
    for i in range(5):
        print()
        print(f'[문제{q}]')
        q+=1
        print(a[i])
        word = input()
        if word==a[i]:
            print("pass")
        else:
            print("fail")
        
    break