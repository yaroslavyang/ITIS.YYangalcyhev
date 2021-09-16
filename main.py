#Задача 4
s = 'тыгыдык'
s1 = 'кыдыгыт'

def string(s):
    return s[::-1]

if string(s1) == s:
    print('YES')
else:
    print('NO')

#Задача 5
array = [1, 2, 3, 4]
summ = 0

for i in range(len(array)):
    summ = (summ * 10 + array[i])

print(summ + 1)

#Задача 6
array = [1, 2, 4, 5]
x = 5
i = 0

for i in range (len(array)):
    j = i + 1
    for j in range (len(array)):
        if array[i] + array[j] == x:
            print(array[i], array[j])
            raise SystemExit

#Задача 7
def string(s):
    return s[::-1]

print(string('тыгыдык'))

#Задача 8
с = 'тыгыдык'
l = len(с) // 2

for i in range(l):
    if с[i] != с[-1-i]:
        print("NO")
        raise SystemExit

print("YES")