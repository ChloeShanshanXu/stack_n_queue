class Queue:

    MINIMUM_SIZE = 10

    def __init__(self):
        self._data = [None]*Queue.MINIMUM_SIZE
        self._front_index = 0
        self._back_index = 0

    def enqueue(self, item):
        self._data[self._back_index] = item
        self._back_index += 1
        if self._back_index == len(self._data):
            self._back_index = 0
        if self._back_index == self._front_index:
            self._resize()

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0
        if Queue.MINIMUM_SIZE < len(self) * 4 < len(self._data):
            self._resize_smaller()
        return item

    def front(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._front_index]

    def is_empty(self):
        return len(self) == 0


