myList=[1,2,3]
print(myList.append(4)) #None
print(myList.pop())     #4
print("------------------------")
def say():
    print('Hi')
print(say())
print("------------------------")
def sum_many(*args):    #*문자 몇 개든 상관없다.
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(sum_many(1,2,3))
print("------------------------")
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k=="name"):
            print("당신의 이름은 :"+k)
print(print_kwargs(name="int 조수",b="2"))
print("------------------------")
def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다."%name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("Alex",22)
say_myself("Ann",23,False)