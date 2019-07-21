#return문을 만나면 함수를 빠져나감

def test(a, b): #a, b는 매개변수
    result = a + b
    return result

print(test(3, 5)) #3, 5는 인수


def say(): #매개변수가 없는 함수
    return 'hi'

a = say()
print(a)

def add(c, d): #결과값이 없는 함수
    print("%d, %d의 합은 %d입니다." % (c, d, c + d))

add(3, 5)
k = add(3, 4) #결과값이 없다.
print(k)

def resay(): #입력 인수를 받는 매개변수도 없고 return문도 없으니 입력값도 결괏값도 없는 함수
    print("hi")

resay()


def add_many(*args): #여러개의 입력값을 받을 때, 매개변서 (*args) / **는 딕셔너리
    result = 0 
    for i in args:
        result = result + i 
    return result

result = add_many(1, 2, 3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

#매개변수에 초기값 설정
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("asdzd", 3333, True)
say_myself("kjdas", 34, False)

#함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.
#함수 안에서 함수 밖의 변수를 변경하는 방법

#(1)return 사용하기
q = 1
def vartest(q):
    q = q + 1
    return q

q = vartest(q)
print(q)

#(2)global 함수 사용하기

qr = 1
def vartest2():
    global qr
    qr = qr + 1

vartest2()
print(qr)

#lambda
#def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

addd = lambda z, x: z + x
resultz = addd(3, 4)
print(resultz)
