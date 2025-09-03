class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def clear(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)
