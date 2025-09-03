from data_structure.heaps.heap import Heap


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self, new_data):
        self.heap.append(new_data)

        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self.parent(index)],
            )

            index = self.parent(index)

    def extract_max(self):
        if not self.heap:
            return None
        
        maximum = self.heap[0]

        self.heap[0] = self.heap[-1]

        self.heap.pop()

        self.heapify_down(0)

        return maximum
    
    def heapify_down(self, index):
        size = len(self.heap)
        largest = index

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def build_heap(self, array):
        self.heap = array[:]

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None
    

if __name__ == "__main__":
    max_heap = MaxHeap()
    array = [-1, 1, 10, 20, 50, 0, 0, 8, 60, 100]
    max_heap.build_heap(array=array)
    
    print(max_heap)
    max_heap.insert(new_data=1000)
    print(max_heap)
    
    max_data = max_heap.extract_max()
    print(max_heap, max_data)

    # A max priority queue
    queue = MaxHeap()

    queue.insert(new_data=10)
    queue.insert(new_data=1)
    queue.insert(new_data=22)
    queue.insert(new_data=145)
    queue.insert(new_data=65)
    queue.insert(new_data=2)
    print(queue)

    while len(queue) != 0:
        queue.extract_max()
        print(queue)

