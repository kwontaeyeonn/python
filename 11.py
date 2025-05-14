a = ['홍길동', '일지매']

print(f'현재 프로그래밍 수강 신청자는 {a}입니다.')

n = input("추가할 학생 이름:")
print(f'{n} 학생의 신청이 완료되었습니다.')
a.append(n)
print(f'현재 이 과목의 최종 신청자는 {a}입니다.')

n = input("철회할 학생 이름:")
a.remove(n)

print(f'{n} 학생의 수강 철회가 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {a}입니다.')

n = input('변경 전 이름:')
de = a.index(n)
del a[de]
ch = input("변경 후 이름:")
a.insert(de, ch)

print(f'요청하신 대로 {n}을(를) {ch}로 변경하였습니다.')
print(f'현재 이 과목의 최종 신청자는 {a}입니다.')