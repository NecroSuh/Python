cabinet = {3:"유재석", 100:"조세호"}
print(cabinet[3])
print(cabinet[100])

#print(cabinet.get(3))  #없을 때 오류
print(cabinet.get(5))   #없을 때 none
print(cabinet.get(5,"사용가능"))
print("hi")

print(3 in cabinet) #True
print(6 in cabinet) #False

cabinet1 = {"A-3":"유재석", "B-100":"이광수"}
print(cabinet1["A-3"])
print(cabinet1["B-100"])

print(cabinet1)
cabinet1["A-3"] = "김종국"
cabinet1["C-20"]= "조세호"
print(cabinet1)

del cabinet1["A-3"]
print(cabinet1)

print(cabinet1.keys())

print(cabinet1.values())

print(cabinet1.items())

cabinet1.clear()
print(cabinet1)