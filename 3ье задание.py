# Класс Ноды, для элементов списка
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_into_end_of_the_list(first, value):
    node = Node(value)
    if first is None:
        return node
    current = first
    while current.next is not None:
        current = current.next
    current.next = node
    return first


def insert_first(first, value):
    node = Node(value)
    node.next = first
    return node


def merge(first, second):
    new_list = None
    current = first

    while current is not None:
        new_list = insert_into_end_of_the_list(new_list, current.value)
        current = current.next

    current = second

    while current is not None:
        new_list = insert_into_end_of_the_list(new_list, current.value)
        current = current.next

    return new_list


def print_list(first):
    # Выводим список
    print("!!!!!")
    current = first
    while current is not None:
        print(current.value)
        current = current.next
    print(current)  # None


# Первый элемент списка, важно не потерять его
first = Node(0)
current = first
# Генерируем список
for i in range(1, 10):
    node = Node(i)
    current.next = node
    current = current.next

second = Node(10)
current = second

for i in range(10, 20):
    node = Node(i)
    current.next = node
    current = current.next

first = merge(first, second)

print_list(first)
