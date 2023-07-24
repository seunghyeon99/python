# 동일한 블록에서는 들여쓰기를 맞추어야 하지만, 다른 블록의 경우에는 맞출 필요가 없다.
num = 20
if num >= 10:
    print("10보다 크거나 같다")
else:
    print("10보다 작다")


# 주석
"""
이 문장은 문자열 상수를 만드는 문장인데,
대입하지 않았고 출력에도 이용하지 않았기 때문에 주석처럼 처리됩니다.
"""


data = "Hello Python"
print(dir(data))
help(sum)
print(sum([1, 2, 3]))  # 리스트
print(sum((1, 2, 3)))  # 튜플
print(sum({1, 2, 3}))  # 셋


import keyword
print(keyword.kwlist)


import sys
print(sys.path)


print("PyCharm")


a = 10
b = 10
print(id(a))
print(id(b))


print(dir(list))  # __iter__ : iterable하다.
print(dir(set))  # __iter__ : iterable하다.
print(dir(int))  # __iter__가 없음 : iterable하지 않다.


# data가 가장 밖이자 제일 큰 블록에 있으므로, data는 모두 한 가지 데이터로 동일하다.
data = 10
if data > 5:
    print(data)
    data = 20
print(data)

# data가 각각 다른 블록에 있으므로, data는 다른 데이터로 가장 큰 블록에서 출력이 불가능하다.
# 그러나 파이썬은 Block Scope가 따로 존재하지 않기 때문에, if문 안에서 선언했어도 구분없이 사용할 수 있다.
condition = 20
if condition > 5:
    data = 20
else:
    data = 30
    print(data)
print(data)


print([1, 2, 3] + [4, 5]) # 데이터의 모임의 경우는 결합
# print("문자열" + 3) # 파이썬에서 문자열과 숫자는 종류가 다르기 때문에 덧셈이 불가하다. 에러가 난다.
print((1, 2, 3) * 3) # 데이터의 모임과 정수를 곱하면 반복한다.
print("Hello Python\n" * 5)  # Hello Python을 줄바꿈하면서 5번 반복


print(20 & 17) # 16
print(20 | 17) # 21
print(20 ^ 17) # 5
print(~20) # -21
print(20 << 3) # 2^3=8을 곱해준 것과 같다.
print(20 >> 3) # 2^3=8으로 나눈 몫과 같다.


cnt = 0  # 12의 배수의 개수를 저장하기 위한 변수
loop = 0 # 조건 확인한 개수를 저장하기 위한 변수
for idx in range(1, 101): # 1 ~ 100
    loop = loop + 1
    if idx % 3 == 0:
        loop = loop + 1
        if idx % 4 == 0:
            cnt = cnt + 1
print("12의 배수의 개수:", cnt)
print("조건 확인 개수:", loop)

cnt = 0  # 12의 배수의 개수를 저장하기 위한 변수
loop = 0  # 조건 확인한 개수를 저장하기 위한 변수
for idx in range(1, 101):  # 1 ~ 100
    loop = loop + 1
    if idx % 4 == 0:
        loop = loop + 1
        if idx % 3 == 0:
            cnt = cnt + 1
print("12의 배수의 개수:", cnt)
print("조건 확인 개수:", loop)


year = 2023  # 년도
# 윤년의 조건 - 둘 중 하나만 True이면 True
# 1. 4의 배수이고, 100의 배수가 아닌 경우
# 2. 400의 배수인 경우
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # True에 가까운 것을 or 앞에 배치해야 한다. and 대신 &, or 대신 |을 사용해도 된다.
    print(year, "는 윤년")
else:
    print(year, "는 윤년이 아님")


print(type(10.3))
print(type(10))


tot = 0.0
for i in range(1, 1001):
    tot += 0.1
print(tot) # 실수(float)는 항상 오차를 발생시킬 수 있음.


x = 10
y = 10.3
result = x + y # 묵시적 형변환 : 자료형이 다르기 때문에 연산이 불가능하다. 그래서 컴퓨터가 x를 float형으로 알아서 형변환을 해주었다.
print(result)


help(print) # print 함수를 공부하기 위해 찾아보자.
help(input) # input 함수를 공부하기 위해 찾아보자.


# 입력받고 출력
name = input("이름 입력:")
print(name)


try:
    # 문자열을 정수로 변환 int()
    age = int(input("나이 입력:")) # 이곳에 문자를 입력하면 정수로 전환할 수 없기 때문에 예외처리(try, except)를 해줘야 한다.
    print(age + 1) # print(age + 1) -> 문자를 입력하면, 문자열과 숫자는 자료형이 다르기 때문에 더할 수 없으므로 에러가 발생한다.
except:
    print("문제 발생")
print("프로그램 종료")

# 여러개 입력
hobbys = input("취미를 ,로 구분해서 입력").split(",")
for hobby in hobbys:
    print(hobby)