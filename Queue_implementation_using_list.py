class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.pop(0) if self.queue else None 
    def peek(self): return self.queue[0] if self.queue else None 
    def is_empty(self): return len(self.queue) == 0

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())    