import time
import random

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

n = 1
print("준비되면 엔터")
input()
start = time.time()

q = random.choice(w)
while n <= 5:
    print("문제", n)
    print(q)
    x = input()
    if q == x:
        print("pass")
        n = n + 1
        q = random.choice(w)
    else:
        print("nooooooo")

end = time.time()
et = end - start
et = format(et, ".2f") #소수점 둘째자리까지 표시
print("시간", et, "초")
