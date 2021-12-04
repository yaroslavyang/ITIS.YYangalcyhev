ans = 0
n = 10
number = 1 
for i in range(0, n):
    ans += number
    number *= 10 
    number += 1
print(ans)