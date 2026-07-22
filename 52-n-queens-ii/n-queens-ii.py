class Solution:
    def totalNQueens(self, n):
        c, d1, d2 = set(), set(), set()

        def dfs(r):
            if r == n:
                return 1
            ans = 0
            for i in range(n):
                if i in c or r-i in d1 or r+i in d2:
                    continue
                c.add(i); d1.add(r-i); d2.add(r+i)
                ans += dfs(r+1)
                c.remove(i); d1.remove(r-i); d2.remove(r+i)
            return ans

        return dfs(0)