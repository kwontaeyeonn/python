def rev(n):
    i = list(n)
    li = list()
    for j in range(1, len(i) + 1):
        li.append(i[-j])
    return(li)

a = input()
print(*rev(a),sep="")