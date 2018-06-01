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

    def insert_end(self, data):
        """Insert a node at the end of the list."""

        current = self.head
        while current.next:
            current = current.next_node

        current.next_node = Node(data)

    def insert_begin(self, data):
        """Insert a node at the begining."""

        current = self.head
        new_node = Node(data)
        new_node.next_node = current
        self.head = new_node

    def delete_dups(self):
        """Remove duplicates in a linked list."""

        slow = self.head
        fast = slow.next_node

        while fast:

            if slow.data == fast.data:
                slow.next_node = fast.next_node

            if fast.next_node != None:
                slow = slow.next_node
                fast = slow.next_node
            else:
                break



class Node(object):
    """Node of a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_node = None


one = Node(1)
two = Node(2)
three = Node(3)
three2 = Node(3)

one.next_node = three
three.next_node = three2
three2.next_node = two

lst = List(one)





