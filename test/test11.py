data = [30, 10, 20]
print(f'현재 리스트: {data}')

print(f'리스트 데이터 개수: {len(data)}')

data.append(40)
print(f'40 추가 후의 리스트: {data}')


print(f'리스트의 마지막 데이터: {data[-1]}')

print(f'추출 후 리스트: {data}')

data.sort()
print(f'오름차순 정렬: {data}')

data.sort(reverse = True)
print(f'리스트 역순: {data}')

print(f'데이터 20의 위치(index): {data.index(20)}')

data.insert(2, 222)
print(f'index 2 위치에 222 삼입 후의 리스트: {data}')

#data.pop(2)
data.remove(222)
print(f'222 삭제 후의 리스트: {data}')

data2 = [77,88,77]

data.extend(data2)
print(f'data 리스트에 data2 리스트 연결: {data}')
data.append(data2)
print(data)
print(f'77 값의 개수: {data.count(77)}')

del data[2]
print(f'index 2 위치의 데이터 삭제 후 리스트: {data}')

