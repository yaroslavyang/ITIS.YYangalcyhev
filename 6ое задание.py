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


def list_len(first):
    len = 0

    current = first

    while current is not None:
        len += 1
        current = current.next

    return len


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

print(list_len(first))

print_list(first)
