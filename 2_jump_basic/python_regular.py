#정규 표현식
#파이썬만의 고유 문법이 아니라 문자열을 처리하는


import re

data = """
park 999999-1010101
kim 988888-1000000
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


#문자 클래스 []
#정규 표현식이 [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻
#[ - ] 두 문자 사이의 범위 (form - to)
#[0-5] = [012345]
#[a-zA-Z] : 알파벳 모두
#[0-9] : 숫자

#닷 dot
#a.b = "a + 모든문자 + b" / a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치

#반복 (*)
#*바로 앞의 문자가 0부터 거의 무한대로 반복

#반복 (+)
#+바로 앞의 문자가 최소 1번 이상 반복될 때 사용

#반복 ({m, n}, ?)
#반복 횟수 제한
#ca{2}t = "c + a(반드시 2번 반복) + t

#?
#ab?c = "a + b(있어도 되고 없어도 된다) + c"


#파이썬에서 정규 표현식을 지원하는 re 모듈
#match() 문자열의 처음부터 정규식과 매치되는지 조사한다.
#search() 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
#findall() 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
#finditer() 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

p = re.compile('[a-z]+')
m = p.match("python")
n = p.match("445")
print(m)
print(n)

k = p.search("python")
l = p.search("344 python")
print(l)
print(k)

result = p.findall("life is t ttt short")
print(result)

result = p.finditer("life is t ttt short")
print(result)

#match 객체의 메서드
#group() 매치된 문자열을 돌려준다
#start() 매치된 문자열의 시작 위치를 돌려준다
#end() 매치된 문자열의 끝 위치를 돌려준다
#span() 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

#컴파일 옵션
#DOTALL, S 줄바꿈 문자
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

