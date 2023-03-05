from collections import deque

class Solution:
    arr = []
    adj_list = {}

    def minJumps(self, arr: list[int]) -> int:
        self.arr = arr
        self.__generate_adjacency_list()
        return self.__bfs()
    
    def __bfs(self):
        steps = 0
        n = len(self.arr)

        queue = deque()
        visited = set()
        queue.append(0)
        visited.add(0)

        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                current_idx = queue.popleft()
                if current_idx == n - 1:
                    return steps
                
                next_indexes = self.adj_list[self.arr[current_idx]]
                for idx in next_indexes:
                    if idx == current_idx:
                        continue
                    queue.append(idx)
                    visited.add(idx)
                
                if current_idx - 1 >= 0 and current_idx - 1 not in visited:
                    queue.append(current_idx - 1)
                    visited.add(current_idx - 1)

                if current_idx + 1 < n and current_idx + 1 not in visited:
                    queue.append(current_idx + 1)
                    visited.add(current_idx + 1)
                self.adj_list[self.arr[idx]] = set() # empty it, as we will not need to visit these values again.
            steps += 1

    def __generate_adjacency_list(self):
        self.adj_list = {}
        for i in range(len(self.arr)):
            val = self.arr[i]
            if val not in self.adj_list:
                self.adj_list[val] = set()
            self.adj_list[val].add(i)
