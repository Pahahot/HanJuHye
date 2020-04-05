#Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

#Q2

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value>100:
            self.value = 100

cal1 = MaxLimitCalculator()
cal1.add(50) # 50 더하기
cal1.add(60) # 60 더하기

print(cal1.value) # 100 출력


#Q3
#하나 : False
#둘 : True
hana = all([1, 2, abs(-3)-3])
dul = chr(ord('a')) == 'a'
print(hana)
print(dul)

#Q4
q4 = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(q4)

#Q5
q5 = int('0xea', 16)
print(q5)

#Q6 map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
q6 = list(map(lambda a: a*3, [1, 2, 3, 4]))
print(q6)

#Q7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
l1 = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(l1)+min(l1))

#Q8
print(round(17 / 3 ,4))

#Q10
import os
os.chdir("c:/doit")
q10 = os.popen("dir")
print(q10.read())

#Q11
import glob
q11 = glob.glob("c:/doit/*.py")
print(q11)

#Q12
import time
time.strftime('%c', time.localtime(time.time()))

#Q13
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45) 
    if num not in result:
        result.append(num)

print(result)   