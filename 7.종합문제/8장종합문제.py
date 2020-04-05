#Q1 문자열 바꾸기
a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)

#Q2 딕셔너리 값 추출하기
a = {'A':90, 'B':80}
a.get('C', 70)

#Q3 리스트의 더하기와 extend 함수
#+는 두 리스트를 더하여 새로운 리스트를 반환하므로 주소값이 바뀜
#extend는 기존의 리스트를 확장하는 개념이므로 주소값 동일

#Q4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum =0
a=0
while A:
    a = A.pop()
    if A.pop >= 50:
        sum = sum+a
print(sum)

#Q5 피보나치 함수
n= input("정수를 입력하세요")
n=int(n)
i =0
j =1
add = 0
p=[i,j]
while add <=n:
    add=i+j
    i=j
    j=add
    p.append(add)
print(p)


#Q6 숫자의 총합 구하기
numlist = input("숫자를,로 구분하여 입력해주세요")
numnum = numlist.split(",")
sum = 0
for n in numnum:
    sum += int(n)   
print(sum)

#Q7 한 줄 구구단
gu = input("2~9중 숫자를 입력하세요")
gugu = int(gu)
for i in range(1, 10):
    print(i*gugu, end= ' ')

#Q8 역순 저장

f = open('abc.txt', 'r')
lines = f.readlines()  
f.close()
lines.reverse()     
f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  
    f.write(line)
    f.write('\n')  
f.close()

#Q9 평균 값 구하기
f = open("sample.txt")
lines = f.readlines( ) 
f.close( )

total = 0
for line in lines:
    score = int(line) 
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()

#Q10 사칙연산 계산기

class Calculator:
    def init (self, num): 
        self.num = num
        
    def sum(self): 
        result = 0
        for i in self.num: 
            result += i
        return result

    def avg(self):
        hap = self.sum()
        return hap / len(self.num)

cal1 = Calculator([1,2,3,4,5]) 
print (cal1.sum())
print (cal1.avg())

cal2 = Calculator([6,7,8,9,10]) 
print (cal2.sum())
print (cal2.avg())
