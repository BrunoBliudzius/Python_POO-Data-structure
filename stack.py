class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items} <- Top"

    def __bool__(self):
        return len(self) > 0

    def push(self, value):
        self.items.append(value)
        return

    def pop(self):
        if len(self) == 0:
            raise IndexError("Stack is empty.")

        return self.items.pop()

    def peek(self):
        if len(self) == 0:
            raise IndexError("Stack is empty. Cannot peek from an empty stack.")
        return self.items[-1]

    def clear(self):
        self.items.clear()
        return


def main():
    stack = Stack()
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack)
    print(stack.pop())
    print(stack)
    print(f"Peek: {stack.peek()}")
    print(f"Size: {len(stack)}")


if __name__ == "__main__":
    main()
