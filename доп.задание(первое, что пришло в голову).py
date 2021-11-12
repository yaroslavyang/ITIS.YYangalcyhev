array = [1, 2, 3, 5, 5]
maxim = 0

for i in range(len(array)):
    j = i
    for j in range(len(array)):
        sum = min(array[i], array[j]) * ( j - i )
        if sum > maxim:
            maxim = sum

print(maxim)
_____________________________
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(first):
    print()
    current = first
    while current is not None:
        print(current.value)
        current = current.next

def insert_first(first, value):
    node = Node(value)
    node.next = first
    return node

def insert_into_end_of_the_list(first, value):
    node = Node(value)
    if first is None:
        return node
    current = first
    while current.next is not None:
        current = current.next
    current.next = node
    return first

def reverse_list_value(first):
    print()
    current = first
    rev = None
    while current is not None:
        rev = insert_first(rev, current.value)
        current = current.next
    return rev

def len_list(first):
    if first is None:
        return None
    current = first
    c = 0
    while current is not None:
        c += 1
        current = current.next
    return c

def first_second(first, second):
    current_1 = reverse_list_value(first)
    current_2 = reverse_list_value(second)
    s = 0
    t = 0
    res = None
    for i in range(len_list(first)):
        t = s // 10
        s = (current_1.value + current_2.value + t)
        res = insert_first(res, s % 10)
        current_1 = current_1.next
        current_2 = current_2.next
    return res

first = Node(1)
current = first
for i in range(1, 10):
    node = Node(i)
    current.next = node
    current = current.next

second = Node(11)
current = second
for i in range(11, 20):
    node = Node(i)
    current.next = node
    current = current.next

print_list(first)
print_list(second)
first = first_second(first, second)
print_list(first)
