from typing import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.arr = []

    def pre_order(self, root):
        # print(root.value)
        try:
            self.arr.append(root.value)
            if root.left != None:
                self.pre_order(root.left)

            if root.right != None:
                self.pre_order(root.right)
            return self.arr
        except:
            raise Exception("pre order accept valid ")

    def post_order(self, root):
        try:
            if root.left:
                self.post_order(root.left)

            if root.right:
                self.post_order(root.right)

            self.arr.append(root.value)
            return self.arr
        except:
            raise Exception("something went wrong")

    def in_order(self, root):
        try:
            if root.left:
                self.in_order(root.left)

            self.arr.append(root.value)

            if root.right:
                self.in_order(root.right)

            return self.arr
        except:
            raise Exception("something went wrong")

    def test(self):
        self.arr = []


class BinarySearch(BinaryTree):

    def add(self, value):

        if not self.root:
            self.root = Node(value)
            # print(self.root.value)
            return

        current = self.root

        while current:
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)

                    return

            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return

    def Contains(self, value):

        if not self.root:
            raise Exception("empty is tree")
        elif value == self.root.value:
            return True
        else:
            current = self.root
            while current:

                if current.value < value:

                    if current.right:
                        current = current.right
                        if value == current.value:
                            return True
                    else:
                        return False

                else:

                    if current.left:
                        current = current.left
                        if value == current.value:
                            return True
                    else:
                        return False