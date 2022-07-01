import random
lotto = random.sample(range(1,46),6)
print(lotto)
print("뽑을 수를 입력하세요.(숫자만)")
num = input("갯수 : ")
for i in range(0,int(num)):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)
