import random
lotto = [i for i in range(1,46)]
for i in range(5):
    random.shuffle(lotto)
    print("로또번호: ",sorted(lotto[0:6]))
