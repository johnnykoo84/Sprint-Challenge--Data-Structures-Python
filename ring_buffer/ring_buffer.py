class RingBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity

    def is_full(self):
        return self.tail > (self.head-1) % self.capacity

    def append(self, item):

        if self.is_full():
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
        else:
            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity

    def get(self):
        Not_none_values = filter(None.__ne__, self.buffer)

        list_of_values = list(Not_none_values)
        return list_of_values
