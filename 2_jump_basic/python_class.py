class Calculator: #클래스(과자 틀)
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator() #객체(과자) / Calculator의 인스턴스
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal3.sub(10))
print(cal3.sub(5))

#사칙연산 클래스 만들기

class FourCal:
    #def __init__(self, first, second): #생성자
        #self.first = first
        #self.second = second
        
    def setdata(self, first, second): #클래스 안에 구현된 함수는 메서드(Method) = 일반 함수와 동일
        self.first = first
        self.second = second
        #파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 
        #pass 아무것도 수행하지 않는 문법 (임시 사용시 활용)

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(8, 4)

print(a.add())
print(b.add())

print(a.sub())
print(b.sub())

print(a.mul())
print(b.mul())

print(a.div())
print(b.div())


#클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지
#객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법
#생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미


    

