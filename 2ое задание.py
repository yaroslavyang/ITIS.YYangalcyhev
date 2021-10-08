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


def reverse_list_value(first):
    buf = None
    buf = insert_first(buf, first.value)
    current = first.next

    while current is not None:
        buf = insert_first(buf, current.value)
        current = current.next

    return buf


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

#print_list(first)

first = reverse_list_value(first)

print_list(first)
