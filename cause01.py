money=2000
card=1
if True and False:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print("---------------------------------")

poket=['paper','cellphone']
card=True
if 'money' in poket:
    pass
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

print("---------------------------------")

score=70
if score>=60:
    message="success"   # 3항 연산자 ?
else:
    message="failure"
message="succes" if score >= 60 else "failure"
print(message)

