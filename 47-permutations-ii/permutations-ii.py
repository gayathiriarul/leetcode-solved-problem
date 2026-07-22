class Solution:
    def permuteUnique(self, nums):
        from itertools import permutations
        return [list(i) for i in set(permutations(nums))]