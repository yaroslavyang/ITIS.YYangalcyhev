array = [13,15,10]
ans = 0
for i in range(len(array)):
    chislo = array[i]
    otvet = 0
    while chislo > 0:
        if chislo % 10 == 3 or chislo % 10 == 5: 
            otvet = 1
            break
        chislo //= 10
        
    if otvet == 1:
        ans += 1

if ans == len(array):
    print(True)
else:
    print(False)