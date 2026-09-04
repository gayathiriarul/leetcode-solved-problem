class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count

        for num in nums:
            index = (num - mn) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            used[index] = True

        ans = 0
        prev_max = mn

        for i in range(bucket_count):
            if not used[i]:
                continue

            ans = max(ans, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return ans