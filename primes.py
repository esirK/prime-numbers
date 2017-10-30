import math

def is_prime(num):
    if isinstance(num, float):
        return False
    try:
        num=int(num)
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    except:
        return "Please enter a valid number"
