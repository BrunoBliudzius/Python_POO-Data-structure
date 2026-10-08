from hash_tableLinked_list import hash_tableLinked_list


class Hash_table:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def __str__(self):
        result = []
        for i, linkedList in enumerate(self.table):
            try:
                for key, value in linkedList:
                    result.append(f"Index {i}: \n('{key}', '{value}')\n")
            except TypeError:
                result.append(f"Index {i}: \n\n")
        return "".join(result)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return False

        for current in self.table[index]:
            k, v = current
            if k == key:
                return True
        return False

    def resize(self):
        load_factor = self.count / self.size

        if load_factor > 0.7:
            new_table = Hash_table(self.size * 2)

            for index in range(self.size):
                if self.table[index] is not None:
                    for current in self.table[index]:
                        k, v = current
                        new_table.put(k, v)

            self.size = new_table.size
            self.table = new_table.table
        return

    def _hash(self, key):
        return hash(key) % self.size

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None

        for current in self.table[index]:
            k, v = current
            if k == key:
                return v
        return None

    def keys(self):
        keys_list = []
        for index in range(self.size):
            if self.table[index] is not None:
                for current in self.table[index]:
                    k, v = current
                    keys_list.append(k)
        return keys_list

    def values(self):
        values_list = []
        for index in range(self.size):
            if self.table[index] is not None:
                for current in self.table[index]:
                    k, v = current
                    values_list.append(v)
        return values_list

    def put(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = LinkedList()

        if key in self.table[index]:
            for current in self.table[index]:
                k, v = current
                if k == key and v != value:
                    current.data = (key, value)
        else:
            self.table[index].append((key, value))
            self.count += 1

        self.resize()
        return

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        try:
            self.table[index].remove((key, self.get(key)))
            self.count -= 1
            return
        except ValueError:
            return None


def main():
    hash_table = Hash_table(10)
    hash_table.put("name", "John")
    hash_table.put("age", 30)
    hash_table.put("city", "New York")

    hash_table.remove("age")

    print(hash_table)


if __name__ == "__main__":
    main()
