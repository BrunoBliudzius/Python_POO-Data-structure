class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)
        return f"Value {value} added to the stack"

    def pop(self):
        if self.size() > 0:
            value = self.items[-1]
            self.items.remove(self.items[-1])
            return f"Value {value} removed from the stack"
        return None

    def peek(self):
        if self.size() > 0:
            return self.items[-1]
        return None

    def __str__(self):
        return f"Stack: {self.items}"


def main():
    stack = Stack()
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack)
    print(stack.pop())
    print(stack)
    print(f"Peek: {stack.peek()}")
    print(f"Size: {stack.size()}")


if __name__ == "__main__":
    main()
