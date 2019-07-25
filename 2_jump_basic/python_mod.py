import mod1 #모듈 불러오기
import mod2
from mod1 import add, sub #모듈 이름 안붙임
from mod1 import *

print(mod1.add(3, 4)) #모듈명.함수명
print(add(3, 4))

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))

result = mod2.add(3, 4)
print(result)
