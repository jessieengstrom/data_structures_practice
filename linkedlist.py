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

    def reverse_in_place(self):
        """Reverse a linked list in place"""

        current = self.head
        cn = current.next_node
        current.next_node = None

        while cn:
            prev = current
            current = cn
            cn = current.next_node
            current.next_node = prev

        self.head = current

    def has_cycles(self):
        """Checks if a linked list has cycles."""

        slow = self.head
        fast = self.head

        while fast != None:
            slow = slow.next_node

            if fast.next_node != None:
                fast = fast.next_node.next_node
            else:
                return False

            if slow is fast:
                return True

        return False


class Node(object):
    """Node of a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_node = None

