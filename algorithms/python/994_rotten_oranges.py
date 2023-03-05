from collections import deque

class Solution:
    grid = None
    m = None
    n = None
    fresh = None
    queue = None


    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.fresh = 0
        self.queue = deque()
        self.__update_fresh_count_and_queue()

        if self.fresh == 0:
            return 0
        if len(self.queue) == 0:
            return -1

        return self.__bfs()
    

    def __update_fresh_count_and_queue(self) -> None:
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.fresh += 1
                elif self.grid[i][j] == 2:
                    self.queue.append((i, j, 0))


    def __bfs(self) -> None:
        time_taken = 0
        num_affected = 0
        
        while self.queue:
            r, c, time_so_far = self.queue.popleft()
            if time_so_far > 0 and not self.__should_amend(r, c):
                continue
            
            self.grid[r][c] = 2
            time_taken = time_so_far
            num_affected += 1 if time_so_far > 0 else 0
            for offset in range(-1, 2, 2):
                self.queue.append((r+offset, c, time_so_far + 1))
                self.queue.append((r, c+offset, time_so_far + 1))
        
        return time_taken if num_affected == self.fresh else -1


    def __should_amend(self, r: int, c: int) -> bool:
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return False
        
        return self.grid[r][c] == 1

