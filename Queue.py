class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append([new_element])

    def display_all(self):
        return self.storage

    def display_one(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


q = Queue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.display_all())
print(q.display_one())