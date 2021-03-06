class MinHeap(object):
    """Heap data structure."""

    def __init__(self):
        self.min_heap = [0]
        self.current_size = 0


    def perc_up(self, i):
        """Move a val up to the correct position in a binary heap."""

        while i // 2 > 0:

            if self.min_heap[i] < self.min_heap[i // 2]:

                parent = self.min_heap[i // 2]
                self.min_heap[i // 2] = self.min_heap[i]
                self.min_heap[i] = parent

            i = i // 2


    def insert(self, val):
        """Insert a value into a binary heap."""

        self.min_heap.append(val)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

        return self.min_heap

    def perc_down(self, i):
        """Move a value down so the correct position"""

        while (i * 2) < self.current_size:

            min_child = self.min_child(i)
            if self.min_heap[i] > self.min_heap[min_child]:

                parent = self.min_heap[i]
                self.min_heap[i] = self.min_heap[min_child]
                self.min_heap[min_child] = parent

            i = min_child

    def min_child(self, i):
        """gets the current min child."""
        if i * 2 > self.current_size:
            return i * 2
            
        else:
            if self.min_heap[i * 2] > self.min_heap[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def del_min(self):
        """Dequeue the minimium node."""

        min = self.min_heap[1]
        self.min_heap[1] = self.min_heap[self.current_size]
        self.current_size = self.current_size - 1
        self.min_heap.pop()
        self.perc_down(1)

        return self.min_heap
