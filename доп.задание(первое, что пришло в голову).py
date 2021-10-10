array = [1, 2, 3, 5, 5]
maxim = 0

for i in range(len(array)):
    j = i
    for j in range(len(array)):
        sum = min(array[i], array[j]) * ( j - i )
        if sum > maxim:
            maxim = sum

print(maxim)