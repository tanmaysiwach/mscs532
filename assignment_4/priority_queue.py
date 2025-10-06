class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):  # For min-heap use; reverse for max-heap
        return self.priority < other.priority

    def __repr__(self):
        return f"(ID: {self.task_id}, Priority: {self.priority})"


class PriorityQueue:
    def __init__(self, max_heap=False):
        self.heap = []
        self.max_heap = max_heap

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_top(self):
        if self.is_empty():
            return None
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify(0)
        return top

    def increase_key(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                if (self.max_heap and new_priority < self.heap[i].priority) or \
                   (not self.max_heap and new_priority > self.heap[i].priority):
                    raise ValueError("New priority is not valid for heap type")
                self.heap[i].priority = new_priority
                self._sift_up(i)
                return
        raise KeyError("Task not found")

    def _compare(self, a, b):
        return a > b if self.max_heap else a < b

    def _sift_up(self, i):
        while i > 0 and self._compare(self.heap[i].priority, self.heap[self._parent(i)].priority):
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify(self, i):
        size = len(self.heap)
        left = self._left(i)
        right = self._right(i)
        best = i

        if left < size and self._compare(self.heap[left].priority, self.heap[best].priority):
            best = left
        if right < size and self._compare(self.heap[right].priority, self.heap[best].priority):
            best = right
        if best != i:
            self.heap[i], self.heap[best] = self.heap[best], self.heap[i]
            self._heapify(best)


def run_priority_queue_test():
    pq = PriorityQueue(max_heap=True)
    pq.insert(Task("A", 3))
    pq.insert(Task("B", 5))
    pq.insert(Task("C", 1))

    print("Priority Queue Contents (Max-Heap):")
    while not pq.is_empty():
        print(pq.extract_top())

if __name__ == "__main__":
    run_priority_queue_test()
