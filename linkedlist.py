class List(object):
    """Linked list."""
    def __init__(self):
        self.head = None

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
        while current.next_node:
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

    def make_copy(self):
        """Make a copy of the list."""

        new_list = List()

        old_list_dictionary = {}
        current = self.head

        while current:
             old_list_dictionary[current] = Node(current.data)

             current = current.next_node

        for key, value in old_list_dictionary.iteritems():
            if key == self.head:
                new_list.head = value

            if key.next_node is None:
                pass

            else:
                value.next_node = old_list_dictionary[key.next_node]

        return new_list



class Node(object):
    """Node of a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_node = None

def merge_two_lists(lst1, lst2):
    """Merge two sorted linked lists."""

    merged = List()
    curr1 = lst1.head
    curr2 = lst2.head

    while curr1 or curr2:
        if merged.head is None:
            if curr1.data <= curr2.data:
                new_node = Node(curr1.data)
                merged.head = new_node
                prev = new_node
                curr1 = curr1.next_node
            else:
                new_node = Node(curr2.data)
                merged.head = new_node
                prev = new_node
                curr2 = curr2.next_node
        elif curr1 is None:
            new_node = Node(curr2.data)
            prev.next_node = new_node
            prev = new_node
            curr2 = curr2.next_node

        elif curr2 is None:
            new_node = Node(curr1.data)
            prev.next_node = new_node
            prev = new_node
            curr1 = curr1.next_node

        else:
            if curr1.data <= curr2.data:
                new_node = Node(curr1.data)
                prev.next_node = new_node
                prev = new_node
                curr1 = curr1.next_node
            else:
                new_node = Node(curr2.data)
                prev.next_node = new_node
                prev = new_node
                curr2 = curr2.next_node

    return merged


one = Node(1)
lst = List()
lst.head = one

lst.insert_end(2)
lst.insert_end(3)
lst.insert_end(3)
lst.insert_end(4)

one2 = Node(1)
lst2 = List()
lst2.head = one2

lst2.insert_end(4)
lst2.insert_end(5)
lst2.insert_end(6)






