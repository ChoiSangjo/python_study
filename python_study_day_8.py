#터틀런 만들기

import turtle as t
import random

#오브젝트 설정

te = t.Turtle() #악당 거북이 te
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle() #먹이 ts
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

# 움직임 함수

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

#실행 함수

def play():
    t.forward(10)
    ang = te.towards(t.pos()) #pos x, y 값 가져오기
    te.setheading(ang)
    te.forward(9)
    if t.distance(ts) < 12: #먹이와 플레이어 캐릭터의 거리가 12보다 작으면 먹이 재생성
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)
    if t.distance(te) >= 12: #악당 거북이와 플레이어 캐릭터의 거리가 12와 같거나 크면 play 함수 실행
        t.ontimer(play, 100) #단위는 1000 = 1초 ontimer(실행할 함수, 시간)

#플레이어 거북이

t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

#작동
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()

play() #게임 시작
