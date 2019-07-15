def hello():
    print("hello")

hello()
hello()


def hello2(name):
    print("hello", name)
hello2(input())

def sum_func(n):
    s = 0
    for x in range(1, n + 1):
        s = s + x
    return s

print(sum_func(10))
print(sum_func(100))


#factorial

def factorial(k):
    fact = 1
    for y in range (1, k + 1):
        fact = fact * y
    return fact

print(factorial(10))
print(factorial(20))

#거북이 도형 만들기 함수

import turtle as t

def poly(k):
    for xx in range(k):
        t.forward(50)
        t.left(360/k)

def poly2(kk, nn):
    for yy in range(kk):
        t.forward(nn)
        t.left(360/kk)

poly(3)
poly(5)

#그리지 않고 거북이 이동시키기

t.up()
t.forward(100)
t.down()

poly2(3, 75)
poly2(5, 100)

#키보드로 거북이 조종하기

def blank():
    t.clear()

def turn_right():
    t.color("red")
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.color("green")
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.color("yellow")
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.color("blue")
    t.setheading(270)
    t.forward(10)


t.shape("turtle")
t.speed(0)
t.pensize(3)
t.bgcolor("black")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen() #그래픽 창이 키보드 입력을 받는다.
