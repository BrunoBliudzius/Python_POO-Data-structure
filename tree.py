class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, data, current_node=None):
        if self.root is None:
            return False

        current = self.root if current_node is None else current_node

        if data == current.data:
            return True
        elif data > current.data:
            if current.right is None:
                return False
            else:
                return self.__contains__(data, current.right)
        else:
            if current.left is None:
                return False
            else:
                return self.__contains__(data, current.left)

    def __iter__(self):
        yield from self._inorder(self.root)

    def __str__(self):
        DefaultTree = []
        for data in self:
            DefaultTree.append(str(data))
        return " ".join(DefaultTree)

    def _inorder(self, node):
        if node is not None:
            yield from self._inorder(node.left)
            yield node.data
            yield from self._inorder(node.right)

    def insert(self, data, current_node=None):

        if self.root is None:
            self.root = Node(data)
            self.size += 1
            return

        current = self.root if current_node is None else current_node

        if data >= current.data:
            if current.right is None:
                current.right = Node(data)
                self.size += 1
            else:
                return self.insert(data, current.right)
        else:
            if current.left is None:
                current.left = Node(data)
                self.size += 1
            else:
                return self.insert(data, current.left)

    def remove(self, data, current_node=None, previous_node=None):
        if self.root is None:
            return

        current = self.root if current_node is None else current_node

        if data == current.data:
            if current.left is None and current.right is None:
                if previous_node is None:
                    self.root = None
                elif previous_node.left is current:
                    previous_node.left = None
                else:
                    previous_node.right = None
                self.size -= 1
                return
            elif current.left is not None and current.right is not None:
                successor = current.right
                while successor.left is not None:
                    successor = successor.left
                current.data = successor.data
                self.remove(successor.data, current.right, current)
                return
            else:
                if previous_node is None:
                    if current.left is not None:
                        self.root = current.left
                        self.size -= 1
                        return
                    else:
                        self.root = current.right
                        self.size -= 1
                        return
                elif previous_node.left is current:

                    previous_node.left = (
                        current.left if current.left is not None else current.right
                    )
                    self.size -= 1
                    return
                else:
                    previous_node.right = (
                        current.left if current.left is not None else current.right
                    )
                    self.size -= 1
                    return
        elif data >= current.data:
            if current.right is None:
                return
            else:
                return self.remove(data, current.right, current)
        else:
            if current.left is None:
                return
            else:
                return self.remove(data, current.left, current)


def main():
    bst = Bst()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Inorder Traversal:", list(bst))
    print("Size of BST:", len(bst))

    bst.remove(3)
    print("Inorder Traversal after removing 3:", list(bst))
    print("Size of BST after removal:", len(bst))


if __name__ == "__main__":
    main()
