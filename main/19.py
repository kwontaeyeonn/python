#방법1
fee = 800

card = int(input("카드 잔액을 입력하세요:"))

if card>=fee:
    print("탑승 가능")

else:
    print("탑승 불가능")

#방법2
fee = 800
card = int(input("카드 잔액을 입력하세요:"))

if card<fee:
    print("탑승 불가능")

else:
    print("탑승 가능")