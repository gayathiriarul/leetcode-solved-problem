class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(n - 1):
            t, c = "", 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    c += 1
                else:
                    t += str(c) + s[i-1]
                    c = 1
            s = t + str(c) + s[-1]
        return s