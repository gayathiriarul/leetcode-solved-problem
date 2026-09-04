class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        def possible(day):
            flowers = 0
            bouquets = 0

            for x in bloomDay:
                if x <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        while left < right:
            mid = (left + right) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left