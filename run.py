import Prime_Calculation.constant as cons
import Prime_Calculation.helper as hlp
from Email.email import Email
from Prime_Calculation.prime_calculation import Prime


def run():
    p = Prime(start=cons.START, finish=cons.FINISH)
    primes = p.calculate_prime()
    print(primes)
    prettier = p.prettier()
    print(prettier)
    new_email = Email()
    new_email.to = "f.anju6448@gmail.com"
    new_email.subject = "Prime Numbers{cons.START} to {cons.FINISH}"
    new_email.body = prettier
    new_email.send()
    
    
if __name__ == "__main__":
    run()