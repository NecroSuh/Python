a=1
def vartest(a): #지역변수(임시변수)
    #global a
    a=a+1       #vartest 안에서만 사용
    return a
#vartest()
a=vartest(a)
print(a)
print("----------------------")
#def add(a,b):
#    return a+b
add=lambda a,b: a+b
print(add(2,4))
print("----------------------")
myList=[lambda a2,b2: a2+b2, lambda a2,b2: a2*b2]
print(myList[0](4,5))
print(myList[1](4,5))