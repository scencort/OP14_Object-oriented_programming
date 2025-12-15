from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()


    def enqueue(self, item):
        self.items.append(item)
        print(f"Добавлен в очередь: {item}")


    def dequeue(self):
        item = self.items.popleft()
        print(f"Удалён из очереди: {item}")
        return item

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.items)

q.dequeue()
print(q.items)
q.dequeue()
print(q.items)