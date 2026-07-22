class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                p = (ord(num1[i])-48) * (ord(num2[j])-48)
                p += res[i+j+1]
                res[i+j+1] = p % 10
                res[i+j] += p // 10

        return ''.join(map(str, res)).lstrip('0')