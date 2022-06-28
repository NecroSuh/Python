def add_many(*args):
    result=0
    for i in args:
        result=result+i # *args에 입력받은 모든 값을 더한다.
    return result
print(add_many(1,4,6,8,5))  

