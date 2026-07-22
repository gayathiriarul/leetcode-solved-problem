class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2
        return ans