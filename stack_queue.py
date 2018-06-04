class Stack(object):
    """Create a stack data structure."""

    def __init__(self):
        self.stack = []


    def peek(self):
        """Return the item on top of the stack."""

        print self.stack[-1]

    def add_item(self, item):
        """Add an item to the stack."""
        
        self.stack.append(item)

    def pop(self):
        """Remove an item in a stack."""

        self.stack.pop()

    def is_empty(self):

        print len(self.stack) < 0

stack = Stack()
stack.add_item(1)
stack.add_item(2)
stack.add_item(3)

stack.peek()
stack.is_empty()
stack.pop()
stack.peek()


class Queue(object):
    """Create a Queue data structure."""

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """Add an item to out queue."""

        self.stack1.append(item)

    def dequeue(self):
        """Remove something from our queue."""

        if len(self.stack2) == 0:

            while len(self.stack1) > 1:

                self.stack2.append(self.stack1.pop())

            first_out = self.stack1.pop()

            while len(self.stack2) > 0:

                self.stack1.append(self.stack2.pop())

            return first_out


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
    