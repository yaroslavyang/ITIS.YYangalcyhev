#я мог неправильно понять
array = [1,2,3,4,5,6,7,8,9]
array1 = [0,1,2,3,4,5,6,7,8]

for i in range(len(array))
    array[i] *= array[array1[i]]
for i in range(len(array)):
    print(array[i])