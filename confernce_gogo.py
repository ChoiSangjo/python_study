import random
import turtle as t
 
def generate_random(endNum, numTot):
    alreadyGenerated = set([])
    numCount = 0
    while numCount != numTot and numCount != endNum:
        ranNum = random.randint(1,endNum)
        turtleForward = 0
        if ranNum not in alreadyGenerated:
            alreadyGenerated.add(ranNum)
            numCount += 1
            chrPrint = ("%d번째 당첨된 수는 %d입니다." %(numCount, ranNum))
            t.setheading(90)
            t.ht()
            t.write(chrPrint, False, "center", ("", 20))
            turtleForward += 30
            t.up()
            t.forward(turtleForward)
            t.down()
    
    t.write("おめでとうございます。", False, "center", ("", 40))


numberEnd = int(input("참가자가 몇명인가요?"))
numberCount = 3

t_user_1 = t.Turtle()
t_user_1.setheading(0)
t_user_1.ht()
t_user_1.color("green")
t_user_1.forward(300)
t_user_1.speed(5)

t_user_2 = t.Turtle()
t_user_2.setheading(180)
t_user_2.ht()
t_user_2.color("green")
t_user_2.forward(300)
t_user_2.speed(5)

generate_random(numberEnd,numberCount)
