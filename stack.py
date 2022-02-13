
class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop() # Always pop last item, if not specifically say which one

    def peek(self):
        return self._data[len(self._data)-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    stack = Stack()
    for i in range (10):
        stack.push(i)
    while not stack.is_empty():
        print(stack.pop())

        


