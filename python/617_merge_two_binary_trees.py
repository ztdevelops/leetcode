from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees_BFS(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not (root1 and root2):
            return root1 if not root2 else root2
        
        root1_pointer = root1
        root2_pointer = root2
        queue = deque()
        nodes = (root1_pointer, root2_pointer)
        queue.append(nodes)
        while queue: # use root1 as the tree to return
            root1_pointer, root2_pointer = queue.popleft()

            if not (root1_pointer or root2_pointer):
                continue

            if root1_pointer and root2_pointer:
                root1_pointer.val += root2_pointer.val
                if not root1_pointer.left and root2_pointer.left:
                    root1_pointer.left = root2_pointer.left
                else:
                    nodes = (root1_pointer.left, root2_pointer.left)
                    queue.append(nodes)
                
                if not root1_pointer.right and root2_pointer.right:
                    root1_pointer.right = root2_pointer.right
                else:
                    nodes = (root1_pointer.right, root2_pointer.right)
                    queue.append(nodes)

        return root1

    
    def mergeTrees_DFS(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not (root1 and root2):
            return root1 if not root2 else root2

        root1_pointer = root1
        root2_pointer = root2

        self.__dfs(root1_pointer, root2_pointer)
        return root1


    def __dfs(self, root1: TreeNode, root2: TreeNode) -> None:  # use root1 as the tree to return
        if not (root1 or root2):
            return

        if root1 and root2:
            root1.val += root2.val
            if not root1.left and root2.left:
                root1.left = root2.left
            else:
                self.__dfs(root1.left, root2.left)

            if not root1.right and root2.right:
                root1.right = root2.right
            else:
                self.__dfs(root1.right, root2.right)
        
