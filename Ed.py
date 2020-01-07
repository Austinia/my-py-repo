"""
이 프로그램은 연습용 입니다.
"""

print("=" * 50)
print("{0:-^50}".format("EDITABLE")) #f'{"EDITABLE":-^50}'
print("=" * 50)

age = 8
print(f"\n이 프로그램은 각종 실습형 예제들이 포함되어 있습니다.\n본 프로그래머는 {age}년간 프로그래밍을 하지 않았습니다.\n")

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][0])
print(a[:2])
print(a[2:])
print(len(a)) #len은 문자열의 갯수나 리스트의 갯수를 알려주는 함수
print(str(a[1]) + "020\n") #str는 정수나 실수를 문자열로 바꿔주는 함수

print("a = [1, 2, 3]\ndel a[1]\na\n[1, 3]\n")

"""
t1 = (1, 2, 'a', 'b')
del t1[0]는 실행 되지 않는다, 튜플형은 리스트형과 달리 요소값을 변경할 수 없다:
"""

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])
print(t1[1:])

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1119'}
dic['job'] = 'janiter'
print(dic)

