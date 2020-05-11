tilt = 0
sumL = 0
sumR = 0
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def getTilt(root):
    global tilt
    if root:
        sumL, sumR = 0, 0
        sumL = getTilt(root.left)
        sumR = getTilt(root.right)
        tilt += abs(sumL - sumR)
        return sumL + sumR + root.data
    else:
        return 0

def main():
    global tilt
    root = Node(10)
    root.left = Node(7)
    root.right = Node(15)
    root.left.left = Node(5)
    root.left.right = Node(8)
    root.right.left = Node(12)
    root.right.right = Node(18)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.left.right.left = Node(8)
    root.left.right.left = Node(9)

    tilt = 0
    getTilt(root)
    return tilt

if __name__ == '__main__':
    print(main())