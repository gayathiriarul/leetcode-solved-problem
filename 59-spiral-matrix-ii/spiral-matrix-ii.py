class Solution:
    def generateMatrix(self, n):
        a = [[0] * n for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        num = 1
        while l <= r and t <= b:
            for i in range(l, r + 1):
                a[t][i] = num; num += 1
            t += 1
            for i in range(t, b + 1):
                a[i][r] = num; num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                a[b][i] = num; num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                a[i][l] = num; num += 1
            l += 1
        return a