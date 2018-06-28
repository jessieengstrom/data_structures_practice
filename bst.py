
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

def print_tree_levels_depth(root):

    to_visit = [root]

    while to_visit:
        current = to_visit.pop()
        print current.data

        if current.left != None and current.right != None:
            to_visit.extend([current.left, current.right])

        elif current.right != None:
            to_visit.append(current.right)

        elif current.left != None:
            to_visit.append(current.left)


def is_bst(root, min, max):
    """Check if it's a bst."""

    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    right = is_bst(root.right, root.data, max)
    left = is_bst(root.left, min, root.data)

    return left and right

# def is_balanced(root):
#     """Checks if a bst is balanced"""

#     return bal(root) >= 0

# def bal(root):
#     """Get balance number."""
#     if root is None:
#         return 0

#     right = bal(root.right)
#     left = bal(root.left)

#     if left < 0 or right < 0 or abs(left - right) > 1:
#         return -1

#     return max(left, right) + 1

def is_balanced(root):
    """Check for a balanced tree."""

    depths = []
    nodes = []
    nodes.append((root, 0))

    while nodes:
        node, depth = nodes.pop()
        print node.data, depth

        if not node.right and not node.left:
            if depth not in depths:
                depths.append(depth)
            print depths

            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):

                return False

        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True


def cal_height(root):
    """Calculate the height of a binary search tree."""

    if root is None:
        return 0

    return 1 + max(cal_height(root.right), cal_height(root.left))

def is_there(root, value):
    """Find a value in a bst."""
    if root is None:
        return False
    if value == root.data:
        return True
    if value < root.data:
        return is_there(root.left, value)
    if value > root.data:
        return is_there(root.right, value)

def find_largest(root):
    """find the largest number in a bst."""

    if root.right is None:
        return root.data

    return find_largest(root.right)

def find_second_largest(root):
    """Find the second largest number."""

    # check if you are at the parent of the largest node
    # and the largest node has no left subtree
    if root.right and (not root.right.right and not root.right.left):
        return root.data

    # check if the largest element has a left subtree
    # and find the largest in that tree 
    if root.left and not root.right:
        return find_largest(root.right.left)

    return find_second_largest(root.right)



four = Node(4)
root = four

insert(root, 2)
insert(root, 6)
insert(root, 3)
insert(root, 1)
insert(root, 7)
insert(root, 5)
insert(root, 8)
insert(root, 9)
insert(root, 10)

create_bst([1, 2, 3, 4, 5, 6, 7])
print_tree_levels(root)
print_tree_levels_depth(root)
print is_bst(root, float('-inf'), float('inf'))
print is_balanced(root)
print cal_height(root)
print is_there(root, 2)
print find_second_largest(root)
