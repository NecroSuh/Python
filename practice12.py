for waiting_no in range(1,6): # [0,1,2,3,4,]
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "닥터 스트레인지"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

cust = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(cust, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
