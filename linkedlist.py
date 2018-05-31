class List(object):
    """Linked list."""
    def __init__(self, head):
        self.head = head

    def print_list(self):
        """Print the contents of a Linked List"""

        current = self.head

        while current:
            print current.data
            current = current.next_node


class Node(object):
    """Node of a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_node = None

