pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print("----------------------------------")
pocket1=['paper','cellphone']
card=True
if 'money' in pocket1:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
print("----------------------------------")
treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print("나무를 %d번찍었습니다."%treeHit)
    if treeHit==10:
        print("나무가 넘어갑니다.")
print("----------------------------------")
prompt="""
1. Add
2. Del
3. List
4. Quit
Enter number: """
number=0
while number !=4:
    print(prompt)
    number=int(input())


