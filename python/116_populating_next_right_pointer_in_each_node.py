from collections import deque

# Definition for a node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return

        queue = deque()
        root.next = None
        queue.append(root.left)
        queue.append(root.right)

        while queue and queue[0]:
            level_size = len(queue)
            queue.append(None)

            for _ in range(level_size):
                current_node = queue.popleft()
                current_node.next = queue[0]
                queue.append(current_node.left)
                queue.append(current_node.right)
            queue.popleft()
        return root

