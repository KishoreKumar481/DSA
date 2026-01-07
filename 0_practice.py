class queue_array:
    def __init__(self):
        self.arr = [0] * 10
        self.start = -1
        self.end = -1
        self.curr_size = 0
        self.max_size = 10

    def push(self, x):
        if self.curr_size == self.max_size:
            print('Queue is full')
            exit(1)

        if self.curr_size == 0:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.max_size
        self.arr[self.end] = x
        self.curr_size += 1

    def pop(self):
        if self.start == -1:
            print('Queue is empty')
            exit(1)
        popped = self.arr[self.start]
        if self.curr_size == -1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start + 1) % self.max_size
        self.curr_size -= 1
        return popped

    def peek(self):
        if self.start == -1:
            print('Queue is empty')
            exit(1)
        return self.arr[self.start]

    def size(self):
        return self.curr_size


if __name__ == "__main__":
    queue = queue_array()
    queue.push(5)
    queue.push(6)
    queue.push(7)
    queue.push(8)
    queue.push(9)
    queue.push(10)

    print(queue.arr)

    print(queue.pop())

    print(queue.peek())

    print(queue.size())
