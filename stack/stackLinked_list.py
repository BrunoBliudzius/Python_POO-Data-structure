class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


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

    def push(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1
        return

    def pop(self):
        if self.tail is None:
            return

        self.tail = self.tail.previous
        self.size -= 1

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return


def main():
    stack = LinkedList()

    print("Empty stack:")
    print("Size:", stack.size)
    print()

    print("Pushing elements...")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack)
    print("Size:", stack.size)
    print("Bottom (head):", stack.head.data)
    print("Top (tail):", stack.tail.data)
    print()

    print("Testing contains:")
    print("20 in stack:", 20 in stack)
    print("50 in stack:", 50 in stack)
    print()

    print("Popping element...")
    stack.pop()

    print("Stack:", stack)
    print("Size:", stack.size)
    print("Bottom (head):", stack.head.data)
    print("Top (tail):", stack.tail.data)
    print()

    print("Popping remaining elements...")
    stack.pop()
    stack.pop()

    print("Stack:", stack)
    print("Size:", stack.size)
    print("Head:", stack.head)
    print("Tail:", stack.tail)
    print()

    print("Trying to pop from empty stack...")
    stack.pop()

    print("Stack:", stack)
    print("Size:", stack.size)

if __name__ == "__main__":
    main()