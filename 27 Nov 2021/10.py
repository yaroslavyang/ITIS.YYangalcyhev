array = [1,2,3,4,5,6,7,8,9]
ans = 0 
for i in range(len(array)):
    n = array[i]
    chet = 0 
    nechet = 0
    lenth = 0 
    while n > 0:
        if n % 10 % 2 == 1:
            nechet += 1 
        else: 
            chet += 1 
        lenth += 1 
        n //= 10
    if lenth == 3 or lenth == 5:
        if chet == 0 or nechet == 0:
            ans += 1 
if ans == 2:
    print(True)
else:
    print(False)