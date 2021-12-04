n = 123456789
ans = 0
while n > 0: 
    if n % 10 % 2 == 1:
        ans *= 10 
        ans += (n % 10)
    n //= 10
s = ans.__str__()
print(s[::-1])