#수식 계산하기

print("1+1=", 1+1)
print("2*2=", 2*2)
print("2/4=", 2/4)
print("2**2=", 2**2)
print("5%3=", 5%3)

#변수 사용하기

import turtle as t
d = 100

t.forward(d)
t.left(120)
t.forward(d)
t.left(120)
t.forward(d)
t.left(120)

#for문 사용하기

for x in range(10):
    print("hello!")

for y in range(3):
    print(100)
    print(200)
    print(300)

#반복 기능으로 도형 그리기

for i in range(3):
    t.forward(100)
    t.left(120)

for ii in range(4):
    t.forward(50)
    t.left(90)

#숫자의 합계 구하기

s = 0
for k in range(1, 10+1):
    s = k + s
    print("k:", k, "sum:", s)

#정오각형 그리기

n = 5
t.color("purple")
t.begin_fill()
for abc in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()

#원을 반복해서 그리기

m = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for g in range(m):
    t.circle(80)
    t.left(360/m)

#선을 반복해서 그리기

angle = 70
t.shape("turtle")
t.bgcolor("green")
t.color("yellow")
t.speed(0)
for h in range(200):
    t.forward(h)
    t.left(angle)




    
