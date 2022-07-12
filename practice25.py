#score_file=open("score.txt","w", encoding="utf8")
#print("수학: 0", file = score_file)
#print("영어: 50", file = score_file)
#score_file.close()

#score_file=open("score.txt","a",encoding="utf8")
#score_file.write("과학: 80")
#score_file.write("\n코딩: 100")
#score_file.close()

#score_file=open("score.txt","r", encoding="utf8")
#print(score_file.read())
#score_file.close()

score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()
