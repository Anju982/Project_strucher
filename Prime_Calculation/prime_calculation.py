import Prime_Calculation.constant as cons
import Prime_Calculation.helper as hlp

class Prime:
    
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        
    def calculate_prime(self):
        primes = []
        
        for n in range(self.start, self.finish):
            if hlp.is_prime(n) and n not in cons.SKIP_RANGE:
                primes.append(n)
        
        return primes
    
    def prettier(self):
        body = ""
        
        for result in self.calculate_prime():
            body += f"This is prime number: {result}\n"
            
        return body