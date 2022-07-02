station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

print(abs(-5))  # 절댓값
print(pow(4,2)) # 4^2
print(max(5,12))    # 최댓값
print(min(5,12))    # 최솟값
print(round(3.14))  # 반올림
print(round(4.99))  #반올림

from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))   # 올림
print(sqrt(16))     # 제곱근

from random import *

print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(random()*10)  # 0.0~10.0 미만의 값 생성
print(int(random()*10))   # 0~10 미만의 임의의 값 생성
print(int(random()*10+1))  # 1~10 이하의 임의의 값 생성

print(randrange(1,46))  # 1~46 미만의 임의의 값 생성
print(randint(1,45))    # 1~45 이하의 임의의 값 생성