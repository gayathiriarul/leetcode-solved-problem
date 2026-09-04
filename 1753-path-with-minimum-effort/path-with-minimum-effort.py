from collections import deque

class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])

        def canReach(limit):
            q = deque([(0, 0)])
            visited = set()
            visited.add((0, 0))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()

                if r == m - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        diff = abs(heights[r][c] - heights[nr][nc])

                        if diff <= limit and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))

            return False

        left = 0
        right = 1000000

        while left < right:
            mid = (left + right) // 2

            if canReach(mid):
                right = mid
            else:
                left = mid + 1

        return left