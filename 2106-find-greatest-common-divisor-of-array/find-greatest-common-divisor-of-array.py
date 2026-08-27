class Solution:
    def findGCD(self, nums):
        small = min(nums)
        large = max(nums)

        while small != 0:
            small, large = large % small, small

        return large