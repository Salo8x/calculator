
class ZeroNotError(Exception):
    def __init__(self, message='Hey we cannot divide a number with zero'):
        self.message = message
        super().__init__(self.message)

class Calculator:
    def add(self, numbers):
        a = 0
        for num in numbers:
            a = a +num
        return a
    def subtract(self, numbers):
        a = numbers[0]
        
        for num in range(1, len(numbers)):
            a = a - numbers[num]
            
        return a
    
    def divide(self,numbers ):
        a = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise ZeroNotError()
            a = a/num
        return a
            
    def multiply(self,numbers):
        a = 1
        for num in numbers:
            a = a *num
        return a
    

  








