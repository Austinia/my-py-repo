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
a.sort()
a.reverse()
print(a)

# 연습문제 7
a = ['life', 'is', 'too', 'short']
print(" ".join(a))

# 연습문제 8
a = (1, 2, 3)
b = (4,)
print(a + b)

# 연습문제 9
"""
a[[1]] = 'python' key의 자리에 리스트형은 오지 못함
"""

# 연습문제 10
a = {'A': 90, 'B': 80, 'C': 70}
print(a.get('B'))

# 연습문제 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

# 연습문제 12
"""
a = b = [1, 2, 3]
a[1] = 4
print(b)
를 했을 경우 [1, 4, 3]으로 출력 될 것이다 두 변수는 다른 객체를 포인팅 하고 있기 때문.
"""

pocket = ['paper', 'cellphone', 'money', 'card']
money = 2000
card = True
if 'money' or 'card' in pocket:
    if money >= 3000:
        print("택시 ㄱㄱ")
    else:
        if 'card':
            print('카카오택시 ㄱㄱ')
        else:
            pass
else:
    print("뚜벅이")

# elif 사용

if 'money' in pocket:
    print('use your money')
elif 'card':
    print('get a Kakao')
else:
    pass

# If문 한줄 정리

if 'money' in pocket : pass
else: print("use your card")

# 조건부 표현식

if money >= 3000:
    message = "Enough"
else:
    message = "Not enough"
print(message)
#OR
message = "Enough" if money >= 3000 else "Not enough"
print(message)

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    if treeHit > 1:
        print("You Hit the tree %d Times" % treeHit)
    else:
        print("You Hit the tree %d Time" % treeHit)
    if treeHit == 10:
        print("You got that tree")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

"""number = 0
while number != 4:
    print(prompt)
    number = int(input())"""

coffee = 10
money = 300
while money:
    print("I got cash so give it to her")
    coffee -= 1
    if coffee == 1:
        print("And We got only %d" % coffee)
    else:
        if coffee == 0:
            print("We RuNnEd OuT!! GeT OuT oF hErE")
            break
        else:
            print("And We got %d" % coffee)

"""Poke = 10
while True:
    money = int(input("How much you Got?:"))
    if money == 300:
        print("Ok, That's enough to order it")
        Poke -= 1
        if Poke == 1:
            print("Jimmy, we got only %d poke anyway." % Poke)
        else:
            if Poke == 0:
                print("Ooh,hoo We Got that Out!, Shut that freaking Door jimmy, we're done")
                break
            else:
                print("Jimmy, we got %d pokes anyway." % Poke)
    elif money > 300:
        print("oh, hoho, that's pretty big number to me boy, let me give you change, here %d" % (money -300))
        Poke -= 1
        if Poke == 1:
            print("Jimmy, we got only %d poke anyway." % Poke)
        else:
            if Poke == 0:
                print("Ooh,hoo We Got that Out!, Shut that freaking Door jimmy, we're done")
                break
            else:
                print("Jimmy, we got %d pokes anyway." % Poke)
    else:
        print("hey my man, You ain't got anything yo, Get out of my area")
        if Poke == 1:
            print("Jimmy, we got only %d poke anyway." % Poke)
        else:
            if Poke == 0:
                print("Ooh,hoo We Got that Out!, Shut that freaking Door jimmy, we're done")
                break
            else:
                print("Jimmy, we got %d pokes anyway." % Poke)"""

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

test_list = ['un', 'deux', 'trois']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

classes = [90, 25, 67, 45, 80]

number = 0
"""for mark in classes:
    number += 1
    if mark >= 60:
        print("number %d student is passed" % number)
    else:
        print("number %d student is not passed" % number)
    if mark < 60:
        continue
    print("number %d student congrat!" % number)"""

add = 0
for k in range(1, 11):
    add += k

print(add)

for number in range(len(classes)):
    if classes[number] < 60:
        continue
    print("number %d student congrat!" % (number+1))

for h in range(2,10):
    for j in range(1,10):
        print(h*j, end=" ")
    print('')

"""a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)"""

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
""" [표현식 for 항목 in 반복가능객체 if 조건문
 ...       for 항목 in 반복가능객체 if 조건문]"""

# 연습문제 1
# shirt

# 연습문제 2
number = 0
result = 0
while number < 1000:
    number += 1
    if (number % 3) == 0:
        result += number
print(result)

# 연습문제 3
star = 0
while star < 5:
    star += 1
    print("*" * star)

# 연습문제 4
for r in range(1, 101):
    print (r)

# 연습문제 5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result = 0
for E in A:
    result += E
print(result / len(A))

# 연습문제 6
"""numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)"""
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

"""def add(a, b):
    return a+b

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result"""

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

def say_myself(name, old, man=True): #초깃값 설정해 놓은 매개변수는 항상 맨뒤!
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d살입니다" % old)
    if man:
        print("나는 남자입니다")
    else:
        print("나는 여자입니다")

print(say_myself("김도윤", 26, False))

a = 1
def vartest(a):
    a += 1
    # return a 와 a = vartest(a)를 했으면 함수 내부에서 외부 변수 변경 가능
vartest(3)
print(a)
# 함수안의 매개변수는 함수밖의 변수와 다른 것!
# global a로 가져올 수 있는 있지만 비추천

# 함수 간결하게 간단 생성시 lambda 사용
add = lambda a, b: a+b
result = add(3, 4)
print(result)

# 사용자입력
# number = input("숫자를 입력하세요")
# print(number)

for i in range(10):
    print(i, end=' ')

f = open("C:/Users/Administrator/Desktop/New file.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

p = open("C:/Users/Administrator/Desktop/New file.txt", 'r')
while True:
    line = p.readline()
    if not line: break
    print(line)
p.close()

f = open("C:/Users/Administrator/Desktop/New file.txt", 'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

"""with opern("foo,txt, 'w') as f:
    f.write("THUG LIFE")"""
# f.close() 하지 않아도 with함수를 벗어나면 닫힘

# 연습문제 1
def is_odd(a):
    if (a % 2) == 0:
        return "짝수"
    else:
        return "홀수"

print(is_odd(2))

# 연습문제 2
def aver(*args):
    result = 0
    for w in args:
        result += w
    result = result / len(args)

# 연습문제 3
"""input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))
"""
# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

# 연습문제 4
"""
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") 이것만 츨력 값이 다름
print("".join(["you", "need", "python"]))"""

# 연습문제 5

"""f1 = open("test.txt", 'w')
f1.write("life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())"""

# 연습문제 6

"""f1 = open("test.txt", 'a')
f1.write(input())
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())"""

# 연습문제 7
"""f1 = open("test.txt", 'w')
f1.write("life is too short\nyou need java")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
data = f2.read()
f2.close()

data = data.replace("java", "python")

f3 = open("test.txt", 'w')
f3.write(data)
f3.close()

f4 = open("test.txt", 'r')
print(f4.read())
f4.close()"""

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result= self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return  result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
b = FourCal(3, 7)
print(type(a))
#a.setdata(4, 2)
#b.setdata(3, 7)
print(a.first)
print(a.second)
print(b.first)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return  result

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

b = SafeFourCal(4, 0)
print(b.div())
print(b.add())

import mod1
print(mod1.add(3, 4))

from mod1 import add, sub
print(add(3, 4))

import mod2
a = mod2.Math()
print(a.solv(2))

"""from game.sound.echo import echo_test
echo_test()"""

from game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

import sys
print(sys.argv)

import os
os.environ

os.system("dir")

f = os.popen("dir")
print(f.read())

import time
print(time.ctime())
import calendar
print(calendar.calendar(2020))
print(calendar.weekday(2020, 1, 14))
import random
print(random.randint(1, 100))

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# import webbrowser
# webbrowser.open_new("https://wikidocs.net/33")

# 5장 외장 함수까지 끝
