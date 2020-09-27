from Heap import HeapMaxHanyu
class PriorityQueueWithHeap():
    def __init__(self):
        self.pq = HeapMaxHanyu()

    def enqueue(self, val):
        self.pq.push(val)
        return
    def dequeue(self):
        return self.pq.pop()

    def isempty(self):
        return len(self.pq) == 0


if __name__ =="__main__":
    instance = PriorityQueueWithHeap()
    instance.enqueue(3)
    instance.enqueue(13)
    instance.enqueue(2)
    instance.enqueue(9)
    print(instance.dequeue())
