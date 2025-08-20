class Node:
    def __init__(self, data):
        self.data = data  # Assign the data to the node
        self.next = None  # Initializing the next data to the node


class LinkedList:
    def __init__(self):
        # Initializing the head and tail as None
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        temp_head = self.head
        output = "["

        while temp_head:
            output += f"{temp_head.data} -> "
            temp_head = temp_head.next

        output = output[:-4] + "]"

        return output

    def __getitem__(self, key):
        if key > self.size - 1 or key < 0:
            raise IndexError("Index out of range.")

        temp_head = self.head

        for i in range(key):
            temp_head = temp_head.next

        return temp_head.data

    def __setitem__(self, key, new_data):
        if key > self.size - 1 or key < 0:
            raise IndexError("Index out of range.")

        temp_head = self.head

        for i in range(key):
            temp_head = temp_head.next

        temp_head.data = new_data

    def __iter__(self):
        self.iter_head = self.head
        return self

    def __next__(self):
        if self.iter_head is None:
            raise StopIteration
        else:
            element = self.iter_head.data
            self.iter_head = self.iter_head.next
            return element

    def prepend(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def append(self, new_data):
        new_node = Node(new_data)

        if self.tail is None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def insert(self, new_data, index):
        if index < 0:
            raise IndexError("Index out of range.")

        new_node = Node(data=new_data)

        if index == 0:
            self.prepend(new_data=new_data)
            return

        current_head = self.head
        for i in range(index - 1):
            if current_head is None:
                raise IndexError("Index out of range.")
            current_head = current_head.next

        new_node.next = current_head.next
        current_head.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Pop from empty linked list.")
        output_data = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return output_data

    def delete(self, index):
        if self.head is None:
            raise IndexError("Delete from empty linked list.")

        if index < 0:
            raise IndexError("Index out of range.")

        if index == 0:
            self.pop()
            return

        current_head = self.head
        for i in range(index - 1):
            if current_head is None or current_head.next is None:
                raise IndexError("Index out of range.")
            current_head = current_head.next

        if current_head.next == self.tail:
            self.tail = current_head
        current_head.next = current_head.next.next

    def reverse(self):
        previous = None
        current_head = self.head
        self.tail = self.head

        while current_head:
            next_node = current_head.next
            current_head.next = previous
            previous = current_head
            current_head = next_node

        self.head = previous


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.prepend("increased")
    linked_list.append("by")
    linked_list.append(15)
    linked_list.prepend("sales")
    linked_list.prepend("The")
    linked_list.append("%")

    print(linked_list)
    print(f"Length of linked list: {len(linked_list)}")

    print("Iterating all the elements:")
    for elem in linked_list:
        print(elem)

    print(f"Element at 0 Index: {linked_list[0]}")

    try:
        print(linked_list[-1])
        print(linked_list[6])
    except Exception as e:
        print(e)

    print(f"Element at 5 Index: {linked_list[5]}")

    linked_list[4] = 50
    print(f"It is increased again: {linked_list}")

    linked_list.insert(new_data="Hello", index=0)
    linked_list.insert(new_data=":", index=4)
    linked_list.insert(new_data=".", index=8)
    print(linked_list)

    pop_left = linked_list.pop()
    print(f"After poping left: Data: {pop_left} and {linked_list}")

    linked_list.delete(index=3)
    linked_list.delete(index=6)
    print(f"After Deleting at index 3 and 6: {linked_list}")

    linked_list.reverse()
    print(f"After Reversing: {linked_list}")
