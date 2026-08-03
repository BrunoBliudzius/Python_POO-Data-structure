class Set:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def __iter__(self):
        return iter(self.elements)

    def __str__(self):
        return f'{{{",".join(str(e) for e in self.elements)}}}'

    def __or__(self, other_set):
        return self.union(other_set)

    def __and__(self, other_set):
        return self.intersection(other_set)

    def __sub__(self, other_set):
        return self.difference(other_set)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
            return
        return

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            return
        raise ValueError(f"{element} not found in the set.")

    def clear(self):
        self.elements.clear()

    def union(self, other_set: Set):
        union_set = Set()

        for element in self.elements:
            union_set.add(element)

        for element in other_set.elements:
            union_set.add(element)

        return union_set

    def intersection(self, other_set: Set):
        if len(self) >= len(other_set):
            larger_set = self
            smaller_set = other_set
        else:
            larger_set = other_set
            smaller_set = self

        intersection_set = Set()

        for element in smaller_set:
            if element in larger_set:
                intersection_set.add(element)

        return intersection_set

    def difference(self, other_set: Set):
        difference_set = Set()

        for element in self.elements:
            if element not in other_set.elements:
                difference_set.add(element)

        return difference_set


def main():
    set1 = Set()
    set2 = Set()

    {set1.add(1)}
    {set1.add(2)}
    {set1.add(3)}
    {set2.add(3)}
    {set2.add(4)}
    {set2.add(5)}

    union_set = set2 | set1
    difference_set = set2 - set1
    intersection_set = set2 & set1

    print(f"union: {union_set}")
    print(f"intersection: {intersection_set}")
    print(f"difference: {difference_set}")


if __name__ == "__main__":
    main()
