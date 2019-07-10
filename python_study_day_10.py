#match simulator

import random


user = int(0)
minUser = input("최소 참여 유저수: ")
maxUser = input("최대 참여 유저수: ")

reagueNum = input("오늘 개최 리그수: ")
entryFee = input("리그 입장료: ")

highUserReward = input("상위 유저 보상금: ")
middleUserReward = input("중위 유저 보상금: ")
lowUserReward = input("하위 유저 보상금: ")

highUserRate = float(0.001)
middleUserRate = float(0.3)
lowUserRate = float(1 - (highUserRate + middleUserRate))

todayIncome = float(0)



for i in range (int(reagueNum)):
    print ("리그 번호", i+1)
    print ("----------------------")
    user = random.randint(int(minUser), int(maxUser))
    totalIncome = user * float(entryFee)
    entryIncome = totalIncome * 0.1
    highReward = (user * highUserRate) * float(highUserReward)
    middleReward = (user * middleUserRate) * float(middleUserReward)
    lowReward = (user * lowUserRate) * float(lowUserRate)
    netIncome = totalIncome - (highReward + middleReward + lowReward)

    todayIncome = todayIncome + netIncome

    print("참여 유저수: ", user)
    print("리그 총 수익: ", totalIncome)
    print("리그 입장 수수료: ", entryIncome)
    print("리그 상위 유저 보상: ", highReward)
    print("리그 중위 유저 보상: ", middleReward)
    print("리그 하위 유저 보상: ", lowReward)
    print("리그 순 수익: ", netIncome)
    print ("=======================")


print ("/////////////////////")
print ("오늘 순 수익: ", todayIncome)

if todayIncome >= 0:
    print ("좋은 하루였다...")
else:
    print ("적자다...")
