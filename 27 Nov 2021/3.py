n = 123456789
sum1 = 0
while n > 0:
    if n > 9:
        sum1 += (n % 10)
        n //= 10
        sum1 -= (n % 10)
        n //= 10
    else:
        sum1 += (n % 10)
        n //= 10
print(sum1)