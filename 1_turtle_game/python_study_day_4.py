#입력 받기

name = input("your name?")
print("hello", name)

#입력 받은 값으로 연산하기

x = input("?")
a = int(x)

x = input("?")
b = int(x)

print(a * b)

#시간 세기

import time

input("enter/ 20s")
start = time.time()

input("re")
end = time.time()

et = end - start

print("real", et, "s")
print("-", abs(et - 20), "s") #abs 절대값 구하기

#if문

i = 3

if i == 2:
    print("ok")
else:
    print("nnnnn")

#문제 맞추기

q = input("5 + 5 = ")
w = int(q)

if q == 5+5:
    print("good")
else:
    print("????")

#random modle

import turtle as t
import random

t.shape("turtle")
t.speed(0)

for ii in range(10):
    c = random.randint(1, 360)
    t.setheading(c) #방향을 c 각도로 돌리기
    t.forward(10)

for iii in range(10):
    t.color("red")
    d = random.randint(1, 360)
    t.setheading(d)
    k = random.randint(1, 20)
    t.forward(k)

#덧셈 문제 무작위로 만들기

for iiii in range(3):
    question = random.randint(1, 30)
    question_re = random.randint(1, 30)

    print(question, "+", question_re)
    an = input()
    na = int(an)

    if question + question_re == na:
        print("ohhh")
    else:
        print("????")

#while문

print("[1-10]")

xx = 1

while xx <= 10:
    print(xx)
    xx = xx + 1

#숫자 맞추기

nn = random.randint(1, 30)

while True: #계속 반복하기
    xxx = input("찍어보자")
    ggg = int(xxx)
    if ggg == nn:
        print("ohhhhhhhhhhhh")
        break #while문 빠져나오기
    if ggg > nn:
        print("크다")
    if ggg < nn:
        print("작다")
