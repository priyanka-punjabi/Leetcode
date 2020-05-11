class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    def flattenList(currentNode, childNode, nextNode):
        head = childNode
        currentNode.next = childNode
        childNode.prev = currentNode
        currentNode.child = None

        while head is not None:
            if head.next is None:
                head.next = nextNode
                if nextNode is None:
                    return head
                nextNode.prev = head
                return nextNode
            elif head.child is None:
                head = head.next
            else:
                head = flattenList(head, head.child, head.next)
        return nextNode

    start = head
    head = head
    while head is not None:
        if head.child is None:
            head = head.next
        else:
            head = flattenList(head, head.child, head.next)

    return start

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node1.child = node3
    node2.prev = node1
    node3.prev = node1
    return flatten(node1)
if __name__ == '__main__':
    main()