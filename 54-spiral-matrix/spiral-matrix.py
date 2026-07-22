class Solution:
    def spiralOrder(self, matrix):
        ans = []

        while matrix:
            ans += matrix.pop(0)

            for row in matrix:
                if row:
                    ans.append(row.pop())

            if matrix:
                ans += matrix.pop()[::-1]

            for row in matrix[::-1]:
                if row:
                    ans.append(row.pop(0))

        return ans