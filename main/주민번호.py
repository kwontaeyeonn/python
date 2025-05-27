def birth(number):
    front, back = number.split('-')
    year = front[:2]
    last = back

    year = int(year)

    if last in ['1', '2']:
        year += 1900
    elif last in ['3', '4']:
        year += 2000
    else:
        return "잘못된 주민번호입니다."
    return year


number = input()
print(birth(number))
