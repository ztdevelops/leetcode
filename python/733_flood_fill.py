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

            if not self.__should_amend(r, c):
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

        self.__dfs(sr, sc)
        return image
    

    def __dfs(self, r: int, c: int) -> None:
        if not self.__should_amend(r, c):
            return
        
        self.__dfs(r+1, c)
        self.__dfs(r-1, c)
        self.__dfs(r, c+1)
        self.__dfs(r, c-1)


    def __should_amend(self, r: int, c: int) -> bool:
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
