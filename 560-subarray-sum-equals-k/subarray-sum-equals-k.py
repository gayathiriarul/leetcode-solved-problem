class Solution:
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num

            if total - k in prefix:
                count += prefix[total - k]

            prefix[total] = prefix.get(total, 0) + 1

        return count