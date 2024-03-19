
class Nums:
    def isPrime(self, num: int) -> bool :
        factors = []
        for n in range(1, num+1):
            if num % n == 0:
                factors.append(n)
            else:
                pass    
        if len(factors) == 2:
            return True
        else:
            return False
        
    def isEven(self, num: int) -> bool:
        if num % 2 == 0:
            return True
        else:
            return False

    def isOdd(self, num: int) -> bool:
        if num % 2 == 1:
            return True
        else: 
            return False
        
    def list_factors(self, num: int) -> list:
        factor = []
        for n in range(1, num+1):
            if num % n == 0:
                factor.append(n)
            else:
                pass
        return f"factors of {num} are {factor}"
    
    def isTriangle(self, num: int) -> bool:
        counter = 0
        for i in range(1, num+1):
            counter+=i
        if counter == num:
            return True
        return False

    

nums = Nums()

