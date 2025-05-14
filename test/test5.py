#h, m = map(int, input().split())
#print((h-1)%24, (m-30)%60)

#import calendar
#print(calendar.prmonth(2025,3))

#import random
#print(random.random()) #0 이상 1미만 실수 중 난수를 생성

#import random
#num=random.uniform(1,10)
#print(num)

#import random
#pop = list(range(1,10))
#print(random.sample(pop,3))

import random
pop = list(range(1,10))
num = random.sample(pop,3)
print(random.sample(pop,1))