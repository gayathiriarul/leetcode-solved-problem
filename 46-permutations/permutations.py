class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + p)
        return res