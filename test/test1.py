# class Car:
#     def __init__(self,displ,drv):
#         self.displ = displ
#         self.drv = drv

#         def info(self):
#             print(f'자동차정보:{self.displ}, {self.drv} 구동')


# car_ obj = car(3000, '4륜')
# car_obj.info()

# class TV:
#     def __init__(self,channel,volume,on):
#         self.channel = channel
#         self.volum = volume
#         self.on = o

#     def show(self):
#         print(self.channel, self.volum, self.on)
#     def setChannel(self,channel):
#         self.channel = channel
    
#     def getChannel(self, channel):
#         return self.channel 

#67
# class Counter:
#     def __init__(self):
#         self.cnt = 0

#     def reset(self,initValue):
#         self.cnt = initValue

#     def increment(self):
#         self.cnt += 1

#     def get(self):
#         return self.cnt
    
# a = Counter()
# b = Counter()

# a.rest(0)
# a.increment()
# print(a.get())

# b.rest(100)
# b.increment()
# print(b.get())
class BankAccount:
    def __init__(self,acnt):
        self.acnt = acnt
        self.balance = 0

    def deposit(self,amt):
        print(f'통장에 {amt}원이 입금됨')
        self.balance += amt
        print(f'현재 잔액은 {self.balance}원\n')
        return self.balance
    
    def withdraw(self,amt):
        print(f'통장에 {amt}원이 출금됨')
        self.balance -= amt
        print(f'현재 잔액은 {self.balance}원\n')
        return self.balance
    
    def transfer(self,target,amt):
        if amt>self.balance:
            print("잔액이 부족합니다")
        else:
            target.balance += amt
            self.balance -= amt
            print(f'{self.acnt}님이 {target.acnt}님과 {amt}원 이체했습니다.')
            print(f'{target.acnt}의 잔액 {target.balance}')
    
a = BankAccount('123-456')
a.deposit(10000)
a.withdraw(5000)

b = BankAccount('456-789')
b.deposit(2000)

a.check()
a.transfer(b,100)
a.check()