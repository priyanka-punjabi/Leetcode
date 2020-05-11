store = set()
class Node:
    """
    A binary tree node has data, pointer to left child and a pointer to right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def checkUnvalued(root):
    global store
    if root:
        store.add(root.data)
        checkUnvalued(root.left)
        checkUnvalued(root.right)
    if len(store) <= 1:
        return True
    else:
        return False

def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)
    print(checkUnvalued(root))

if __name__ == '__main__':
    main()