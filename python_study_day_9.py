#주사위 확률

import random

total = 10000
ev = 0

for i in range(total):
    if random.randint(1, 6) == 1:
        ev = ev + 1

core = float(ev / total * 100)


print("%.1f" % core, "%")
print("%.2f" % core, "%")

print("%10.1f" % core, "%")
print("%10.2f" % core, "%")

print("%05.1f" % core, "%")
print("%015.1f" % core, "%")

