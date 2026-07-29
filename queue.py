class queue:
    def __init__(self):
        self.items = []

    def queue_size(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)
        return f"Value: {value} added to the queue."

    def dequeue(self):
        if self.queue_size() == 0:
            return "Queue is empty."
        value = self.items[0]
        self.items.pop(0)
        return f"Value: {value} removed from the queue"

    def peek(self):
        if self.queue_size() == 0:
            return "Queue is empty."
        return f"Value: {self.items[0]} is at the front of the queue."

    def back(self):
        if self.queue_size() == 0:
            return "Queue is empty."
        return f"Value: {self.items[-1]} is at the back of the queue."

    def __str__(self):
        return f"Queue: {self.items}"


def main():
    q = queue()
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
