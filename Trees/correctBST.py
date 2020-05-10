node1 = None
node2 = None
temp = None

class Node:
    """
    A binary tree node has data, pointer to left child and a pointer to right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def getIncorrectNodes(root):
    global temp
    global node1
    global node2
    if root:
        getIncorrectNodes(root.left)
        if temp != None:
            if temp.data > root.data:
                if node1 == None:
                    node1 = temp
                else:
                    node2 = root
        temp = root
        getIncorrectNodes(root.right)

def swapNodes(root, n1, n2):
    global node1
    global node2
    if root:
        swapNodes(root.left, n1, n2)
        if root == node1:
            root.data = n2
        elif root == node2:
            root.data = n1
        swapNodes(root.right, n1, n2)

def printBST(root):
    if root:
        printBST(root.left)
        print(root.data, end=' ')
        printBST(root.right)

def main():
    global node1
    global node2
    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)

    print('Inorder Traversal of Original Tree:')
    printBST(root)
    print()
    print()
    getIncorrectNodes(root)
    swapNodes(root, node1.data, node2.data)
    print('Inorder Traversal of Corrected Tree:')
    printBST(root)

if __name__ == '__main__':
    main()
