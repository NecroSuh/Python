class FourCal:
    def __init__(self,first,second):    # __init__() : 무조건 맨 처음 실행된다.   한 번만 사용
        self.first = first 
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first - self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


#a=FourCal(4,2)
#a.setdata(4,2)
#print(a.first)
#print(a.second)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result

a1 = MoreFourCal(4,2)
a2 = SafeFourCal(4,2)
print(a1.pow())
print(a2.div())