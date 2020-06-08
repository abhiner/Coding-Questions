
"""Write a Python program to check whether a given a binary tree is a valid binary search
tree (BST) or not. """
arr = []
class Node:
    def __init__(self, root_val):
        self.left = None
        self.right = None
        self.val = root_val

def isSorted():
    global arr
    if (all(arr[i] < arr[i+1] for i in range(len(arr)-1))):
        return True
    else:
        return False

def Inorder(root):
    global arr
    if root:
        Inorder(root.left)
        arr.append(root.val)
        Inorder(root.right)

def isBST(root):
    if root is None:
        return True
    Inorder(root)
    if isSorted():
        return True
    else:
        return False
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
if isBST(root):
    print("is BST")
else:
    print("not a BST")
