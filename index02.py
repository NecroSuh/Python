s1=set([1,2,3])
s1={1,2,3}
print(type(s1))
print("-------------------------------")
l=[1,2,3,4,5]
newList=list(set(l))
print(newList)
print("-------------------------------")
s2=set([1,2,3,4,5])
s3=set([4,5,6,7,8,9])
print(s2&s3)    #교집합
print(s2.intersection(s3))
print(s2 | s3)  #합집합
print(s2.union(s3))
print(s2-s3)    #차집합
print(s2.difference(s3))
print("-------------------------------")
s2.add(6)   # 한개 추가
print(s2)
print("-------------------------------")
s2.update([7,8,9])  #여러개 추가
print(s2)
print("-------------------------------")
a=[1,2,3,4]
while True:
    a.pop()
    print(a)

