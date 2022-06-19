test_list=['one','two','three']
for i in test_list:
    print(i)
print("---------------------------")
a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
print("---------------------------")
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
