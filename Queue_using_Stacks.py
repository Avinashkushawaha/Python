class MyQueue:
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.out_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()                