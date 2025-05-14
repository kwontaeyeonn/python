def get_data():
    a1, b1 = map(int,input("(x1,y1) :").split('.'))
    a2, b2 = map(int,input("(x2,y2) :").split('.'))
    return a1,b1,a2,b2
def get_line(a1, b1, a2, b2):
    ret = ""
    if a1 == a2:
        ret = f"x = {a1}"
    else:
        slp = (b2-b1)/(a2-a1)
        y_i = b1 - (slp * a1)
        ret = f'y = {slp}x + ({y_i})'
    return ret
x1,y1,x2,y2 = get_data()
line = get_line(x1,y1,x2,y2)
print(line)