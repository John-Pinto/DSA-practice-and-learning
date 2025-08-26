class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_data):
        if self.root is None:
            self.root = Node(data=new_data)
            return

        current_root = self.root

        while True:
            if new_data < current_root.data:
                if current_root.left is None:
                    current_root.left = Node(data=new_data)
                    break
                else:
                    current_root = current_root.left
            elif new_data > current_root.data:
                if current_root.right is None:
                    current_root.right = Node(data=new_data)
                    break
                else:
                    current_root = current_root.right
            else:
                break

    def search(self, data):
        current_root = self.root

        while current_root is not None:
            if data == current_root.data:
                return True
            elif data < current_root.data:
                current_root = current_root.left
            else:
                current_root = current_root.right

        return False

    def __min_value_node(self, node: Node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def delete(self, data):
        current_root = self.root
        parent = None

        while current_root and current_root.data != data:
            parent = current_root

            if data < current_root.data:
                current_root = current_root.left
            else:
                current_root = current_root.right

        if current_root is None:
            return

        if current_root.left is None and current_root.right is None:
            if current_root == self.root:
                self.root = None
            elif current_root == parent.left:
                parent.left = None
            else:
                parent.right = None

        elif current_root.left is None:
            if current_root == self.root:
                self.root = current_root.right
            elif current_root == parent.left:
                parent.left = current_root.right
            else:
                parent.right = current_root.right

        elif current_root.right is None:
            if current_root == self.root:
                self.root = current_root.left
            elif current_root == parent.left:
                parent.left = current_root.left
            else:
                parent.right = current_root.left

        else:
            successor = self.__min_value_node(node=current_root.right)
            successor_data = successor.data
            self.delete(successor.data)
            current_root.data = successor_data

    def print_preorder(self):
        print("BST Preorder: ", end="")
        self.__preorder(node=self.root)
        print()

    def __preorder(self, node: Node):
        if node:
            print(node.data, end=", ")
            self.__preorder(node=node.left)
            self.__preorder(node=node.right)

    def print_inorder(self):
        print("BST Inorder: ", end="")
        self.__inorder(node=self.root)
        print()

    def __inorder(self, node: Node):
        if node:
            self.__inorder(node=node.left)
            print(node.data, end=", ")
            self.__inorder(node=node.right)

    def print_postorder(self):
        print("BST Postorder: ", end="")
        self.__postorder(node=self.root)
        print()

    def __postorder(self, node: Node):
        if node:
            self.__postorder(node=node.left)
            self.__postorder(node=node.right)
            print(node.data, end=", ")

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, node: Node):
        if node is None:
            return 0

        left_height = self.__get_height(node=node.left)
        right_height = self.__get_height(node=node.right)
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    import random

    array = random.sample(population=range(1, 50), k=10)

    binary_tree = BST()

    for data in array:
        binary_tree.insert(new_data=data)

    print(f"Binary tree height: {binary_tree.get_height()}")
    print(f"Random numbers list: {array}")
    binary_tree.print_preorder()
    binary_tree.print_inorder()
    binary_tree.print_postorder()

    print(binary_tree.search(array[0]))
    print(binary_tree.search(array[-1]))
    print(binary_tree.search(array[5]))
    print(binary_tree.search(51))

    print(f"Deleting {array[0]}, {array[3]}, {array[8]}, {array[-1]}:")
    binary_tree.delete(data=array[0])
    binary_tree.delete(data=array[3])
    binary_tree.delete(data=array[8])
    binary_tree.delete(data=array[-1])
    print(f"Binary tree height: {binary_tree.get_height()}")

    binary_tree.print_preorder()
    binary_tree.print_inorder()
    binary_tree.print_postorder()
