class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.size
        self.count -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        index = (self.rear - 1) % self.size
        return self.queue[index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size