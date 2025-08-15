#calc.py
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        if self.second==0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return self.first/self.second
