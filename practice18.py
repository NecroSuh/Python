def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))
profile("유재석", 20 , "Python")
profile("강호동", 25 , "Java")

def profile1(name, age = 17 , main_lang = "Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile1("하하")
profile1("이광수")
