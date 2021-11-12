def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False

def gen_primes(n, limit):
    current = n 
    while current < limit:
        if isPrime(current) == True:
            yield current
        current += 1
        
for val in gen_primes(2,2000):
    print(val)