from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = []
        k = len(p)

        pc = Counter(p)
        wc = Counter(s[:k])

        if pc == wc:
            ans.append(0)

        for i in range(k, len(s)):
            wc[s[i]] += 1
            wc[s[i-k]] -= 1

            if wc[s[i-k]] == 0:
                del wc[s[i-k]]

            if wc == pc:
                ans.append(i-k+1)

        return ans