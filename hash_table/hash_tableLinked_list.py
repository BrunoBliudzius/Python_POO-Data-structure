class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class hash_tableLinked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        text = ""

        while current:
            text += f"{current.data} -> "
            current = current.next

        text += " None"

        return text

    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        return

    def remove(self,data):
        if self.head is None:
            return False

        current = self.head

        while current:
            if current.data == data:
                if current is self.head:
                    if self.head.next == None:
                        self.tail = None
                        self.head = None
                    else:
                        self.head.next.previous = None
                        self.head = self.head.next
                elif current is self.tail:
                    self.tail.previous.next = None
                    self.tail = self.tail.previous
                else:
                    current.next.previous = current.previous
                    current.previous.next = current.next
                
                return True
            
            current = current.next
        
        return False


def main():
    linked_list = hash_tableLinked_list()

    print("Initial list:")
    print(linked_list)

    # Adding elements
    for value in [10, 20, 30, 40]:
        linked_list.add(value)

    print("\nAfter adding elements:")
    print(linked_list)

    # Removing the first element
    print("\nRemoving 10:", linked_list.remove(10))
    print(linked_list)

    # Removing a middle element
    print("\nRemoving 30:", linked_list.remove(30))
    print(linked_list)

    # Removing the last element
    print("\nRemoving 40:", linked_list.remove(40))
    print(linked_list)

    # Removing the only remaining element
    print("\nRemoving 20:", linked_list.remove(20))
    print(linked_list)

    # Attempting to remove an element from an empty list
    print("\nRemoving 50:", linked_list.remove(50))
    print(linked_list)

    # Testing an element that does not exist
    linked_list.add(100)
    print("\nAttempting to remove 200:", linked_list.remove(200))
    print(linked_list)


if __name__ == "__main__":
    main()