class Queue:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit
        self.size = 0

    def enqueue(self, item):
        if self.limit is not None and self.size >= self.limit:
            raise Exception("QueueOverflow: Queue has reached its limit.")

        self.items.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("QueueUnderflow: Queue is empty.")

        self.size -= 1
        return self.items.pop(0)

    def peek(self):
        if self.size == 0:
            raise Exception("QueueUnderflow: Queue is empty.")

        return self.items[0]


if __name__ == "__main__":
    # Static Queue
    queue = Queue(limit=5)

    for i in range(1, 11):
        try:
            queue.enqueue(item=i)
            print(f"Entering in queue: {i}, peek: {queue.peek()}")
        except Exception as e:
            print(e)

    for i in range(1, 11):
        try:
            print(f"Exiting from queue: {i}, peek: {queue.peek()}")
            queue.dequeue()
        except Exception as e:
            print(e)

    # Dynamic Queue
    queue = Queue()

    for i in range(1, 6):
        try:
            queue.enqueue(item=i)
            print(f"Entering in queue: {i}, peek: {queue.peek()}")
        except Exception as e:
            print(e)

    for i in range(1, 11):
        try:
            print(f"Exiting from queue: {i}, peek: {queue.peek()}")
            queue.dequeue()
        except Exception as e:
            print(e)
