#모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일

# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#if __name__ == "__main__": // 다른 파일에서 이 모듈을 부르면 거짓이 되어 실행하지 않음

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
