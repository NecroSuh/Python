class Calculator:   # 1. Class를 입력 2. 대문자로 시작하는 클래스의 이름을 작성 3. 안에 들어갈 함수와 변수 설정
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
