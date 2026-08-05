class MaxHeap:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def clear(self):
        self.elements.clear()

    def peek(self):
        return self.elements[0] if self.elements else None

    def insert(self, value):
        if value is None:
            raise ValueError("Cannot insert None into the heap.")

        self.elements.append(value)
        self._heapify_up(len(self) - 1)

    def extract(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            return self.elements.pop()

        max_value = self.elements[0]
        self.elements[0] = self.elements[len(self) - 1]
        self.elements.pop()
        self._heapify_down(0)
        return max_value

    def _swap(self, a, b):
        self.elements[a], self.elements[b] = self.elements[b], self.elements[a]

    def _heapify_down(self, index):
        largest = index
        left = self._get_left(index)
        right = self._get_right(index)
        size = len(self)

        if left < size and self.elements[largest] < self.elements[left]:
            largest = left

        if right < size and self.elements[largest] < self.elements[right]:
            largest = right

        if index != largest:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _heapify_up(self, index):
        parent_index = self._get_parent_index(index)
        current_index = index

        while (
            current_index > 0
            and self.elements[parent_index] < self.elements[current_index]
        ):
            self._swap(parent_index, current_index)
            current_index = parent_index
            parent_index = self._get_parent_index(current_index)

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _get_left(self, index):
        return 2 * index + 1

    def _get_right(self, index):
        return 2 * index + 2


def main():
    heap = MaxHeap()

    values = [50, 20, 80, 10, 90, 60, 30, 100, 40, 70]

    print("Inserting values:")
    for value in values:
        heap.insert(value)
        print(f"Inserted: {value:<3} | Heap: {heap.elements}")

    print("\nCurrent maximum:")
    print(heap.peek())

    print("\nExtracting values:")

    while len(heap) > 0:
        maximum = heap.extract()
        print(f"Extracted: {maximum:<3} | Heap: {heap.elements}")

    print("\nHeap is empty.")
    print("Peek:", heap.peek())


if __name__ == "__main__":
    main()
