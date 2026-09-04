class Solution:
    def longestPrefix(self, s):
        lps = [0] * len(s)

        for i in range(1, len(s)):
            j = lps[i - 1]

            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j

        return s[:lps[-1]]