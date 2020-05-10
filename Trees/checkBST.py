import math
prev = -math.inf

class Node:
    """
    A binary tree node has data, pointer to left child and a pointer to right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def checkBST(root):
    """
    Function to check if Binary Tree is a Binary Search Tree
    :param root: current root node
    :return: Boolean value
    """
    # traverse the tree in inorder fashion and update the prev node
    global prev

    if root:
        if not checkBST(root.left):
            return False

        # Handles same valued nodes
        if root.data < prev:
            return False

        # Set value of prev to current node
        prev = root.data

        return checkBST(root.right)
    return True

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(4)

    if checkBST(root):
        print("Is BST")
    else:
        print("Not a BST")

if __name__ == '__main__':
    main()