from linked_list import Linked_list


class Hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_define(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_define(key)
        if self.table[index] is None:
            self.table[index] = Linked_list()
        self.table[index].append({key: value})

    def get(self, key):
        index = self.hash_define(key)
        if self.table[index] is None:
            return None

        current = self.table[index].head
        while current:
            if key in current.data:
                return current.data[key]
            current = current.next
        return None

    def remove(self, key):
        index = self.hash_define(key)
        if self.table[index] is None:
            return None

        self.table[index].remove({key: self.get(key)})

    def __str__(self):
        result = []
        for i, linked_list in enumerate(self.table):
            if linked_list is not None:
                current = linked_list.head
                while current:
                    result.append(f"Index {i}: {current.data}")
                    current = current.next
        return "\n".join(result)


def main():
    hash_table = Hash_table(10)
    hash_table.put("name", "John")
    hash_table.put("age", 30)
    hash_table.put("city", "New York")

    print(hash_table.get("name"))  # Output: John
    print(hash_table.get("age"))  # Output: 30
    print(hash_table.get("city"))  # Output: New York

    print(hash_table)

    hash_table.remove("age")
    print(hash_table.get("age"))

    print(hash_table)  # Output: None


if __name__ == "__main__":
    main()
