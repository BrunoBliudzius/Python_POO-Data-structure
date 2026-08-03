class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head

        while current:
            yield current.data
            current = current.next

    def __str__(self):
        result = []
        for value in self.__iter__():
            result.append(str(value))
        return " -> ".join(result)

    def __len__(self):
        return self.size

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def append(self, data, index=None):
        if index is None:
            index = len(self)

        if index < 0 or index > len(self):
            raise IndexError("Index out of bounds")

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == len(self):
            self.tail.next = node
            self.tail = node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

        self.size += 1
        return

    def remove(self, data):
        if self.head is None:
            return

        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next

                    if self.head is None:
                        self.tail = None

                elif current == self.tail:
                    self.tail = previous
                    previous.next = None
                else:
                    previous.next = current.next

                self.size -= 1
                return

            previous = current
            current = current.next

        raise ValueError(f"{data} not found in the list")


def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(linked_list)  # Output: ['1', '2', '3']

    linked_list.remove(2)
    print(linked_list)  # Output: ['1', '3']

    print(1 in linked_list)  # Output: True
    print(2 in linked_list)  # Output: False


if __name__ == "__main__":
    main()
