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


def get_by_index(first, position):
    i = 0
    current = first

    while current is not None:
        if i == position:
            return current
        else:
            current = current.next
            i += 1

    return None


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

element = get_by_index(first, 3)
print(element.value)

print_list(first)
