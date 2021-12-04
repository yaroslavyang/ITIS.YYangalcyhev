n = 123456789
maxi = 0
while n > 0:
    maxi = max(maxi, n % 10) 
    n //= 10
print(maxi)