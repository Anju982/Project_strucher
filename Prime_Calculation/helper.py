#Function that are going to help prime numbers


def is_prime(number):
    if number > 1:
        for n in range(2, number):
            if number % n != 0:
                continue
            else:
                return False
    return True
