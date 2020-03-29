# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(num):
    if num%2 ==0:
        print('짝수')
    else:
        print('홀수')
is_odd(1)

# Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg(*num):
    sum=0
    for i in num:
        sum = sum+i
        avrg = sum/len(num)
    print(avrg)

avg(1,5,3,9)

# Q3 
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)

# Q4 >> print("you", "need", "python") you need python

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())

# Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
f = open("test.txt", 'a')
f.write(input("입력하세요"))
f.close

# Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

data = """Life is too short
you need java"""
f3 = open("test.txt", 'w')
f3.write(data)
f3.close()

f3 = open("test.txt", 'r')
data = f.read()
f3.close()

data.replace('java','python')
f3 = open("test.txt", 'w')
f3.write(data)
f3.close()