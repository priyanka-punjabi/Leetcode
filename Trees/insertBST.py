class Node:
    """
    A binary tree node has data, pointer to left child and a pointer to right child
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertBST(arr):
    """
    Method to insert elements from array into a BST
    :param arr: array of elements to be inserted
    :return: root node of the tree
    """
    if not arr:
        return None

    # find middle
    mid = (len(arr)) // 2

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = insertBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = insertBST(arr[mid + 1:])

    return root

def partition(arr, low, high):
    """
    Helper method for quick sort
    :param arr: array of elements to be inserted
    :param low: lower limit
    :param high: upper limit
    :return: Position of sorted element
    """
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def qsort_arr(arr, low, high):
    """
    Sorted the given array in ascending order using quick sort. O(n log n)
    :param arr: array of elements to be inserted
    :param low: lower limit
    :param high: upper limit
    :return: None
    """
    if low < high:
        pi = partition(arr, low, high)
        qsort_arr(arr, low, pi - 1)
        qsort_arr(arr, pi + 1, high)

def printBST(root):
    """
    Utility method to print inorder traversal
    :param root: current root node
    :return: None
    """
    if root:
        printBST(root.left)
        print(root.data, end=' ')
        printBST(root.right)

def main():
    arr = [10, 5, 15, 3, 7, 8, 20, 25]
    qsort_arr(arr, 0, len(arr) - 1)
    root = insertBST(arr)
    printBST(root)

if __name__ == '__main__':
    main()