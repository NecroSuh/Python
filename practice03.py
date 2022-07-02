from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+" 일로 선정되었습니다.")

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("n"))
print(python.find("Java")) # -1 반환
#print(python.index("Java")) 오류

print(python.count("n"))