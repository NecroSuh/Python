score= int(input("점수를 입력하세요:"))

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>60:
    print("D")
else:
    print("F")

print("학점입니다.")

jumsu=score

res=''
if jumsu>=60:
    res='합격'
else:
    res='불합격'
print(res)
