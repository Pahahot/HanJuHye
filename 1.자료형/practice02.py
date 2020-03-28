#01 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

kor = 80
eng = 75
math = 55

sum = kor+eng+math
avg = sum/3
print(avg)


#02 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

z = input("숫자를 입력하세요")
z = int(z)
rest = z%2
if rest == 0 :
    print('짝수')
else :
    print('홀수')


#03 홍길동 씨의 주민등록번호는 881120-1068234이다. 
#홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

id ='881120-1068234'
bd = id[:6]
q = id[7:]
print(bd)
print(q)


#04 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

id = input("주민번호를 숫자만 입력하세요")
print(id[6])


#05 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"
a.replace(':','#')
print(a)

#06 [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

l = [1, 3, 5, 4, 2] 
l.sort(reverse = True)
print(l)


#07 ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

h = ['Life', 'is', 'too', 'short']
h = h[0] +' '+ h[1] +' '+ h[2] +' '+ h[3]
print(h)


#08 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자. 
t = (1,2,3)
t = t + (4,)
print(t)


#09 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a = dict()
""" 답: a[[1]] = 'python' / key값은 불변의 값이어야 하므로 list는 key가 될수없음."""


#10 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a['B'])

#11 a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = set(a)

#12 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
#  다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
a = b = [1, 2, 3]
a[1] = 4
print(b)

'''[1, 4, 3]이 출력된다. a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있기 때문이다.'''