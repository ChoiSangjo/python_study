#거북이 대포 게임

import turtle as t
import random

#입력 함수 정의
def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0: #거북이가 땅 위에 있는 동안 반복
        t.forward(15)
        t.right(5)

    d = t.distance(target, 0) #거북이와 목표 지점과의 거리 구하기
    t.sety(random.randint(10, 100)) #성공 또는 실패를 표시할 위치 지정
    if d < 25: #거리 차이가 25보다 작으면 목표 지점에 명중한 것
        t.color("blue")
        t.write("Good", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10) #거북이 발사 위치로 되돌리기
        t.setheading(ang) #각도 처음 기억해둔 각도로 되돌리기

# 땅 그리기
t.goto(-300, 0)
t.down()
t.goto(300, 0)

#목표 지점을 설정하고 그리기
target = random.randint(50, 100) #목표 지점을 무작위로 설정
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

#거북이 되돌리기
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

#거북이가 동작하는데 필요한 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen() #거북이 그래픽 창이 키보드 입력 받도록 설정
