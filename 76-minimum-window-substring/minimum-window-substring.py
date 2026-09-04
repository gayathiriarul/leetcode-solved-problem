from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        window = {}

        left = 0
        formed = 0
        required = len(need)

        ans = ""
        ans_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < ans_len:
                    ans = s[left:right + 1]
                    ans_len = right - left + 1

                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in need and window[leftChar] < need[leftChar]:
                    formed -= 1

                left += 1

        return ans