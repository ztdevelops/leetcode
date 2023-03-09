class Solution:
    cache = {}
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n not in self.cache:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]
