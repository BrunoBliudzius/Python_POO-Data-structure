class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def append(self, data, index=0):
        if index < 0 or index > self.size():
            raise IndexError("Index out of bounds")

        node = Node(data)

        if index == 0:
            node.next = self.head
            self.head = node
            self.tail = node
        elif index == self.size():
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

        return node.data

    def remove(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = None
                else:
                    prev = self.head
                    while prev.next != current:
                        prev = prev.next
                    prev.next = current.next
                return current.data
            current = current.next
        return None


def main():
    linked_list = Linked_list()
    print(f"add: {linked_list.append(0, 1)}")
    print(f"add: {linked_list.append(1, 2)}")
    print(f"add: {linked_list.append(2, 3)}")
    print(f"add: {linked_list.append(3, 4)}")
    print()

    print(f"size: {linked_list.size()}")
    print(f"search 2: {linked_list.search(2)}")
    print()

    print(f"remove: {linked_list.remove(1)}")
    print(f"size: {linked_list.size()}")
    print(f"search 2: {linked_list.search(2)}")


if __name__ == "__main__":
    main()
