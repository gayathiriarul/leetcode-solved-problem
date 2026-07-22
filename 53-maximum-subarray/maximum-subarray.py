class Solution:
    def maxSubArray(self, nums):
        cur = ans = nums[0]
        for i in nums[1:]:
            cur = max(i, cur + i)
            ans = max(ans, cur)
        return ans