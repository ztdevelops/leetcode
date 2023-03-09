class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complements:
                return complements[comp], i
            
            complements[nums[i]] = i