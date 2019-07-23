#r > 읽기모드
#w > 쓰기모드
#a > 추가모드

f = open("new_file.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()



#readline()함수

f = open("new_file.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#readlines() 함수 > 파일의 모든 줄

f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read() 함수 > 파일 전체

f = open("new_file.txt", 'r')
data = f.read()
print(data)
f.close()

#a 모드

f = open("new_file.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with 문

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
