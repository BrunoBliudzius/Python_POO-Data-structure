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

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def enqueue(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1
        return

    def dequeue(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None


def main():
    queue = LinkedList()

    print("Empty queue:")
    print("Size:", queue.size)
    print()

    print("Adding elements...")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:", queue)
    print("Size:", queue.size)
    print("Head:", queue.head.data)
    print("Tail:", queue.tail.data)
    print()

    print("Testing contains:")
    print(20 in queue)
    print(50 in queue)
    print()

    print("Removing element...")
    queue.dequeue()

    print("Queue:", queue)
    print("Size:", queue.size)
    print("Head:", queue.head.data)
    print("Tail:", queue.tail.data)
    print()

    print("Removing remaining elements...")
    queue.dequeue()
    queue.dequeue()

    print("Queue:", queue)
    print("Size:", queue.size)
    print("Head:", queue.head)
    print("Tail:", queue.tail)


if __name__ == "__main__":
    main()