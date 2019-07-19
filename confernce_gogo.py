import turtle as t
import random

user = input('number? :')
cong_user = []

t_user_1 = t.Turtle()
t_user_1.setheading(0)
t_user_1.shape("circle")
t_user_1.color("green")
t_user_1.forward(300)
t_user_1.speed(5)

t_user_2 = t.Turtle()
t_user_2.setheading(180)
t_user_2.shape("circle")
t_user_2.color("green")
t_user_2.forward(300)
t_user_2.speed(5)

for i in range(3):
    gogo = random.randint(1, int(user))
    cong_user.append(int(gogo))
    t.write(cong_user, False, "center", ("", 15))

#t.write("おめでとうございます。", False, "center", ("", 20))
