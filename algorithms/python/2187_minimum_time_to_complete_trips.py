class Solution:
    time = None

    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        self.time = time
        return self.__bsearch(totalTrips)

    def __calculate_trips(self, mid: int) -> int:
        return sum(mid // i for i in self.time)    

    def __bsearch(self, totalTrips: int) -> int:
        left = min(self.time)
        right = left * totalTrips

        while left <= right:
            mid = (left + right) // 2
            if self.__calculate_trips(mid) < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
        
        return right + 1
