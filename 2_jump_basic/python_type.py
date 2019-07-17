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
