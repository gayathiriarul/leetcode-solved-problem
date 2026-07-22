class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:

            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total = total + digit * digit
                n = n // 10

            n = total

        if n == 1:
            return True
        else:
            return False        