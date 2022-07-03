menu = ("돈까스", "메밀")
print(menu[0])
print(menu[1])

#menu.add("생선까스")

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name, agem hobby)

(name, age, hobby) = ("김종국", 20, "health")
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3,}
print(my_set)

java = {"유재석", "양세찬", "지석진"}
python = set(["유재석", "노홍철"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("송지효")
print(python)

java.remove("지석진")
print(java)