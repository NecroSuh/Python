jumin = "000123-1234567"
print("성별 : "+jumin[7])
print("연 : "+jumin[0:2]) # 0부터 2 직전까지
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : "+jumin[-7:]) # 맨 뒤에서 7번째부터 마지막까지

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("검정","빨강"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("검정","빨강"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("검정","빨강"))

print("나는 {age}살이며, {color}색을 좋아합니다.".format(age=20, color="검정"))


