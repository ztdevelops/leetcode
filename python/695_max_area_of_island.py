from collections import deque

class Solution:
    grid = None
    m = None
    n = None


    def maxAreaOfIsland_BFS(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    result = max(result, self.__bfs(i, j))
        return result


    def __bfs(self, r: int, c: int) -> int:
        queue = deque()
        queue.append((r, c))
        area = 0
        while queue:
            r, c = queue.popleft()
            if not self.__should_amend(r, c):
                continue

            self.grid[r][c] = -1
            area += 1
            for offset in range(-1, 2, 2): # accounts for -1, 1
                queue.append((r+offset, c))
                queue.append((r, c+offset))
        return area


    def maxAreaOfIsland_DFS(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        result = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    result = max(result, self.__dfs(i, j))
        return result


    def __dfs(self, r: int, c: int) -> int:
        if not self.__should_amend(r, c):
            return 0
        
        self.grid[r][c] = -1
        count = 1
        for offset in range(-1, 2, 2): # accounts for -1, 1
            count += self.__dfs(r+offset, c)
            count += self.__dfs(r, c+offset)
        return count


    def __should_amend(self, r: int, c: int) -> bool:
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return False
        
        return self.grid[r][c] == 1


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

solution = Solution()