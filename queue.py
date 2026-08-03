class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self) > 0

    def __contains__(self, value):
        return value in self.items

    def __str__(self):
        return str(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self) == 0:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if len(self) == 0:
            raise IndexError("Queue is empty")
        return self.items[0]

    def back(self):
        if len(self) == 0:
            raise IndexError("Queue is empty.")
        return self.items[-1]

    def clear(self):
        self.items.clear()


def main():
    q = Queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print()

    print(q)
    print(q.peek())
    print(q.back())
    print()

    print(q.dequeue())
    print(q)
    print(q.peek())
    print(q.back())

    print()
    print(q.dequeue())
    print(q.dequeue())

    print()
    print(q)


if __name__ == "__main__":
    main()
