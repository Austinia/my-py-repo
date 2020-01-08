"""
이 프로그램은 연습용 입니다.
"""

print("=" * 50)
print("{0:-^50}".format("EDITABLE"))  # f'{"EDITABLE":-^50}'
print("=" * 50)

age = 8
print(f"\n이 프로그램은 각종 실습형 예제들이 포함되어 있습니다.\n본 프로그래머는 {age}년간 프로그래밍을 하지 않았습니다.\n")

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][0])
print(a[:2])
print(a[2:])
print(len(a))  # len은 문자열의 갯수나 리스트의 갯수를 알려주는 함수
print(str(a[1]) + "020\n")  # str는 정수나 실수를 문자열로 바꿔주는 함수

print("a = [1, 2, 3]\ndel a[1]\na\n[1, 3]\n")

"""
t1 = (1, 2, 'a', 'b')
del t1[0]는 실행 되지 않는다, 튜플형은 리스트형과 달리 요소값을 변경할 수 없다:
"""

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])
print(t1[1:])

dic = {'name' : 'pey', 'phone' : '0119993323', 'birth' : '1119'}
dic['job'] = 'janiter'
print(dic)

del dic['job']
print(dic)

print(dic['name'])
# print(dic['pey'])는 실행되지 않는다.

print(dic.keys())
print(dic.values())
print(dic.items())
print('job' in dic)

s1 = set([1, 2, 3])
print(s1)
s2 = set('hello')
print(s2)  # 순서x 중복x
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

print(s3 & s4)
print(s3 | s4)
print(s3 - s4)

s1.add(4)
print(s1)
s1.remove(4)
print(s1)

"""
bool
"""

# a = True
# b = False

print(1 == 1)
print(2 > 1)
print(2 < 1)

a = [1, 2, 3, 4]
while a:  # 조건문이 참인 동안 조건문 안에 있는 문장을 반복해서 수행한다.
    print(a.pop())  # pop 함수는 리스트의 마지막을 꺼내는것

a = [1, 2, 3, 4]
b = a
print(id(a))
print(a is b)

a[1] = 5

print(a)
print(b)

a = [1, 2, 3, 4]
b = a[:]

a[1] = 5
print(a)
print(b)

a = [1, 2, 3, 4]
from copy import copy
b = copy(a)

print(b is a)

# 연습문제 1
a = 80
b = 75
c = 55
print((a + b + c)/3)

# 연습문제 2
a = 13
if [a % 2]:
    print("홀수")
else:
    print("짝수")

# 연습문제 3
a = "881120-1068234"
print(a[:6])
print(a[7:])

# 연습문제 4
print(a[7])

# 연습문제 5
a = "a:b:c:d"
print(a.replace(":", "#"))

# 연습문제 6
a = [1, 3, 5, 4, 2]
print(a.sort())
print(a.reverse())
