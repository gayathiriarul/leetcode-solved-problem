class Solution:
    def checkSubarraySum(self, nums, k):
        rem = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k

            if r in rem:
                if i - rem[r] >= 2:
                    return True
            else:
                rem[r] = i

        return False