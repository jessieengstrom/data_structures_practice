
class Node(object):
    """Tree Nodes"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    """Insert Node at correct position."""

    if root is None:
        root = Node(data)

    if data > root.data:
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right, data)

    if data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            insert(root.left, data)

    return root

def create_bst(lst):
        """Create a bst from a sorted list."""

        if not lst:
            return None
        
        middle = len(lst) / 2

        node = Node(lst[middle])

        node.left = create_bst(lst[:middle])
        node.right = create_bst(lst[middle + 1:])

        print node.data
        

def print_tree_levels(root):
    """Print the breadth frist levels of a tree."""

    to_visit = [root]

    while to_visit:
        current = to_visit.pop(0)
        print current.data
        
        if current.left != None and current.right != None:
            to_visit.extend([current.left, current.right])

        elif current.left != None:
            to_visit.append(current.left)

        elif current.right != None:
            to_visit.append(current.right)


four = Node(4)
root = four

insert(root, 2)
insert(root, 6)
insert(root, 3)
insert(root, 1)
insert(root, 7)
insert(root, 5)

# create_bst([1, 2, 3, 4, 5, 6, 7])
print_tree_levels(root)
