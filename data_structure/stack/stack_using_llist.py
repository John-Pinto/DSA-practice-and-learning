from data_structure.linked_list.single_linked_list import LinkedList


class Stack:
    def __init__(self, limit=None):
        self.items = LinkedList()
        self.limit = limit
        self.size = 0

    def push(self, item):
        if self.limit is not None and self.size >= self.limit:
            raise Exception("StackOverflow: Stack has reached its limit.")

        self.items.prepend(new_data=item)
        self.size += 1

    def pop(self):
        if self.size == 0 and self.items.head is None:
            raise Exception("StackUnderflow: Stack is empty.")

        self.size -= 1
        return self.items.pop()

    def peek(self):
        if self.size == 0 and self.items.head is None:
            raise Exception("StackUnderflow: Stack is empty.")

        return self.items.head.data


if __name__ == "__main__":
    # Static stack
    stack = Stack(limit=5)

    for i in range(1, 11):
        try:
            stack.push(item=i)
            print(f"Pushing in stack: {stack.peek()}")
        except Exception as e:
            print(e)

    for i in range(1, 11):
        try:
            print(f"Poping from stack: {stack.peek()}")
            stack.pop()
        except Exception as e:
            print(e)

    # Dynamic stack
    stack = Stack()

    for i in range(1, 6):
        try:
            stack.push(item=i)
            print(f"Pushing in stack: {stack.peek()}")
        except Exception as e:
            print(e)

    for i in range(1, 11):
        try:
            print(f"Poping from stack: {stack.peek()}")
            stack.pop()
        except Exception as e:
            print(e)
