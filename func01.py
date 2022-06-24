def sum(a,b):
    result=a+b
    return result
print(sum(1,2))
print("-----------------------")

def sum1(a1,b1):
    print("%d, %d의 합은 %d입니다." %(a1,b1,a1+b1))
print (sum1(5,7))
print("------------------------")
def sum_and_mul(a,b):
    return a+b,a*b,a-b
print(sum_and_mul(1,2))