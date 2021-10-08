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

def swap(first, node1, node2):
    buf = node1.next
    node1.next = node2.next
    node2.next = buf

    if first == node1:
        current = node2

        while current.next != node2:
            current = current.next

        current.next = node1

        return node2
    else:
        current = first

        while current is not None:
            if current.next == node1:
                current.next = node2
            elif current.next == node2:
                current.next = node1

            current = current.next

        return first


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

left = get_by_index(first, 0)
right = get_by_index(first, 9)

first = swap(first, left, right)

print_list(first)
