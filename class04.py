class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

# 내장함수
#abs => 절대값 all => 모두 참인지 any => 하나라도 참이 있는가 chr => ASCII코드 입력받아 문자출력
#dir => 자체적으로  가진 변수나 함수를 보여줌 divmod => 몫과 나머지를 튜플 형태로 돌려줌
#enumerate => 열거
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
#eval => 실행 후 결과값을 돌려줌
#filter => 함수를 통과하여 참인 것만 돌려줌
def positive(x):
    return x>0
a = list(filter(positive,[1,-3,2,0,5,6]))
print(a)

a = list(filter(lambda x:x>0,[1,-3,2,0,-5,6]))
print(a)