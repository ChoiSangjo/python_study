import random

sc1 = 0
sc2 = 0

def make():
    for no in range(5):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        result = a + b
        global sc1
        global sc2
        print(a, "+", b)
        ans = int(input("= "))
        if result == ans:
            print("ok")
            sc1 = sc1 + 1
        else:
            print("no")
            sc2 = sc2 + 1

make()

print("정답 수 : ", sc1, "오답 수 : ", sc2)
if sc1 == 5:
    import turtle as t

    t.bgcolor("black")
    t.color("red")
    t.pensize(40)
    t.circle(140)
