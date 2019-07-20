#https://wikidocs.net/13

#문자 정렬
a_left = "{0:<10}".format("hi")
print(a_left)

a_right = "{0:>10}".format("hi")
print(a_right)

a_center = "{0:^10}".format("hi")
print(a_center)

#값 넣기
text_1 = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(text_1)

#f 문자열 포매팅 (문자열 앞에 f붙이기)
name = "최상조"
age = 30

text_2 = f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(text_2)

#문자 수 세기 count
a = "    hobby    "
print(a.count('b'))
print(text_2.count("입"))

#위치 알려주기 index
print(text_2.index("입"))

#문자열 삽입 join
print(",".join(text_2))

#대문자 upper / 소문자 lower 변경
print(a.upper())

#공백 지우기 왼쪽 lstrip 오른쪽 rstrip 양쪽 strip
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#문자열 변경
print(text_2.replace("최상조", "이름이..?"))

#삼중 리스트
a_list = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a_list[2][2][0])

#중첩 리스트 슬라이싱
b_list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(b_list[2:5])
print(b_list[3][:2])

c_list = [1, 2, 3]
print(len(c_list))
del c_list[1]
print(c_list)
c_list.append([5, 1])
print(c_list)
c_list.insert(0, 999)
print(c_list)
c_list.remove(1)
print(c_list)
print(c_list.count(999))

#리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다.
#튜플 > ( )

#딕셔너리
#딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
print(dic['name'])
print(dic.keys())
list(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get('name'))
print('name' in dic)
print('email' in dic)
