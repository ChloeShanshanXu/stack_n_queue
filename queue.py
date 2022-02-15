class Queue:
    MINIMUM_SIZE = 10

    def __init__(self):
        self._data = [None] * Queue.MINIMUM_SIZE
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

    def __len__(self):
        if self._back_index < self._front_index:
            return len(self._data) - self._front_index + self._back_index
        return self._back_index - self._front_index

    def _resize(self):
        new_data = [None] * len(self._data) * 2
        new_index = 0
        for index in range(self._front_index, len(self._data)):
            new_data[new_index] = self._data[index]
            new_index += 1
        for index in range(0, self._front_index):
            new_data[new_index] = self._data[index]
            new_index += 1
        self._data = new_data
        self._front_index = 0
        self._back_index = new_index

    def resize_smaller(self):
        new_data = [None] * (len(self._data) // 2)
        # new_index = 0
        # if self._back_index > self._front_index:
        #     for index in range(self._front_index, self._back_index):
        #         new_data[new_index] =[index]
        #         new_index += 1
        # else:
        #     for index in range(self._front_index, len(self._data)):
        #         new_data[new_index] = self._data[index]
        #         new_index += 1
        #     for index in range(0, self._back_index):
        #         new_data[new_index] = self._data[index]
        #         new_index += 1
        for index in range(len(self)):
            new_data[index] = self._data[(self._front_index + index) % len(self._data)]

        number_of_items = len(self)
        self._data = new_data
        self._front_index = 0
        self._back_index = number_of_items


class Deque:
    _MINIMUM_SIZE = 10

    def __init__(self):
        self._data = [None] * Deque._MINIMUM_SIZE
        self._front_index = 0
        self._back_index = 0

    def add_back(self, item):
        self._data[self._back_index] = item
        self._back_index += 1
        if self._back_index == len(self._data):
            self._back_index = 0
        if self._back_index == self._front_index:
            self._resize()

    def add_front(self, item):
        self._front_index -= 1
        self._data[self._front_index] = item
        if self._front_index == -1:
            self._front_index = len(self._data) - 1
        if self._back_index == self._front_index:
            self._resize()

    def remove_front(self):
        if self.is_empty():
            raise IndexError
        item = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index += 1
        if self._front_index == len(self._data):
            self._front_index = 0
        if Deque._MINIMUM_SIZE < len(self) * 4 < len(self._data):
            self._resize_smaller()
        return item

    def remove_back(self):
        if self.is_empty():
            raise IndexError
        self._back_index -= 1
        item = self._data[self._back_index]
        self._data[self._back_index] = None
        if self._back_index == -1:
            self._back_index = len(self._data) - 1
        if Deque._MINIMUM_SIZE < len(self) * 4 < len(self._data):
            self._resize_smaller()

        return item
    def front(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._front_index]

    def back(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._back_index - 1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        if self._back_index < self._front_index:
            return len(self._data) + self._back_index - self._front_index
        return self._back_index - self._front_index

    def _resize(self):
        new_data = [None] * len(self._data) * 2
        new_index = 0
        for index in range(len(self)):
            new_data[index] = self._data[(self._front_index + index) % len(self._data)]

        number_of_items = len(self)
        self._data = new_data
        self._front_index = 0
        self._back_index = index

    def _resize_smaller(self):
        new_data = [None] * (len(self._data) // 2)
        for index in range(len(self)):
            new_data[index] = self._data[(self._front_index + index) % len(self._data)]

        number_of_items = len(self)
        self._data = new_data
        self._front_index = 0
        self._back_index = number_of_items


if __name__ == "__main__":
    q = Deque()
    for num in range(1, 7):
        q.add_back(num)

    for num in range(4):
        print(q.remove_front())

    for num in range(7, 12):
        q.add_back(num)

    while not q.is_empty():

        print(q.remove_back())

