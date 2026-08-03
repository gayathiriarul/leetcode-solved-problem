from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        k -= 1  # Convert to 0-based index
        result = []

        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            result.append(numbers.pop(index))
            k %= factorial[i - 1]

        return "".join(result)