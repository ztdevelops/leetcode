from collections import deque

class Solution:
    image = None
    m = None
    n = None
    original_colour = None
    color = None


    def floodFill_BFS(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.image = image
        self.m = len(image)
        self.n = len(image[0])
        self.original_colour = image[sr][sc]
        self.color = color

        queue = deque()
        queue.append((sr, sc))
        while queue:
            r, c = queue.popleft()

            if not self.should_amend(r, c):
                continue

            image[r][c] = color
            queue.append((r+1, c))
            queue.append((r-1, c))
            queue.append((r, c+1))
            queue.append((r, c-1))

        return image


    def floodFill_DFS(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.image = image
        self.m = len(image)
        self.n = len(image[0])
        self.original_colour = image[sr][sc]
        self.color = color

        self.dfs(sr, sc)
        return image
    

    def dfs(self, r, c):
        if not self.should_amend(r, c):
            return
        
        self.dfs(r+1, c)
        self.dfs(r-1, c)
        self.dfs(r, c+1)
        self.dfs(r, c-1)


    def should_amend(self, r, c):
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return False
        
        if self.image[r][c] == self.color or self.image[r][c] != self.original_colour:
            return False
        
        return True


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

solution = Solution()
