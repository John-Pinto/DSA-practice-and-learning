from data_structure.heaps.heap import Heap


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self, new_data):
        self.heap.append(new_data)

        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self.parent(index)],
            )

            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None

        minimum = self.heap[0]

        self.heap[0] = self.heap[-1]

        self.heap.pop()

        self.heapify_down(0)

        return minimum

    def heapify_down(self, index):
        size = len(self.heap)
        smallest = index

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break

    def build_heap(self, array):
        self.heap = array[:]

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None


if __name__ == "__main__":
    min_heap = MinHeap()
    array = [-1, 1, 10, 20, 50, 0, 0, 8, 60, 100]
    min_heap.build_heap(array=array)

    print(min_heap)
    min_heap.insert(new_data=1000)
    print(min_heap)

    max_data = min_heap.extract_min()
    print(min_heap, max_data)

    # A min priority queue
    queue = MinHeap()

    queue.insert(new_data=10)
    queue.insert(new_data=1)
    queue.insert(new_data=22)
    queue.insert(new_data=145)
    queue.insert(new_data=65)
    queue.insert(new_data=2)
    print(queue)

    while len(queue) != 0:
        queue.extract_min()
        print(queue)
