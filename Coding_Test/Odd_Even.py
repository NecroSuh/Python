def solution(num_list):
    ans=[]
    odd, even=0,0
    for num in num_list:
        if num%2==0:
            even+=1
        else:
            odd+=1
    ans=[even,odd]
    return ans
