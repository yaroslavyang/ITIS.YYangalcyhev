n = 3
array_arreev = [[7,8,9],[10,11,12],[7,8,9]]
ans = [0]*14

for i in range(0, n):
    for j in range(0, n):
        ans[array_arreev[i][j] - 7] += 1
        
for i in range(len(ans)):
    print(i+7,": 00:", ans[i], "workers")