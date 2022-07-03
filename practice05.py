subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호","박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하") # 맨 뒤에 추가
print(subway)

subway.insert(1,"정형돈")  # 사이에 추가
print(subway)

subway.append("유재석")
print(subway.count("유재석"))

num_list=[5,1,4,3,2]
num_list.sort() # 오름차순
print(num_list)

num_list.reverse()  # 내림차순
print(num_list)

#num_list.clear()    # 모두 삭제
#print(num_list)

mix_list=["유재석",20,True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)