class Set:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
            return element

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            return element

    def contains(self, element):
        if element in self.elements:
            return True
        return False

    def clear(self):
        self.elements = []

    def union(self, other_set: Set):
        result_set = Set()

        for element in self.elements:
            result_set.add(element)

        for element in other_set.elements:
            result_set.add(element)

        return result_set

    def intersection(self, other_set: Set):
        if self.size() >= other_set.size():
            larger_set = self
            smaller_set = other_set
        else:
            larger_set = other_set
            smaller_set = self

        intersection_set = Set()

        for _ in smaller_set.elements:
            if larger_set.contains(_):
                intersection_set.add(_)

        return intersection_set

    def difference(self, other_set: Set):
        if self.size() >= other_set.size():
            larger_set = self
            smaller_set = other_set
        else:
            larger_set = other_set
            smaller_set = self

        difference_set = Set()

        for _ in larger_set.elements:
            if not smaller_set.contains(_):
                difference_set.add(_)

        return difference_set


def main():
    set1 = Set()
    set2 = Set()

    print(f"add: {set1.add(1)}")
    print(f"add: {set1.add(2)}")
    print(f"add: {set1.add(3)}")
    print(f"add: {set2.add(3)}")
    print(f"add: {set2.add(4)}")
    print(f"add: {set2.add(5)}")

    union_set = set1.union(set2)
    difference_set = set1.difference(set2)
    intersection_set = set1.intersection(set2)

    print(f"union: {union_set.elements}")
    print(f"intersection: {intersection_set.elements}")
    print(f"difference: {difference_set.elements}")


if __name__ == "__main__":
    main()
