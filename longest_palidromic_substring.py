class Solution:
    def longestPalindrome(self, s: str) -> str:
        lgst_str_idx = 0
        start = 0
        for i in range(len(s)):
            # odd length string
            left, right = i, i
            while s[left] == s[right] and left >= 0 and right < len(s):
                if right - left + 1 > lgst_str_idx:
                    start = left
                    lgst_str_idx = right - left + 1
                left -= 1
                right += 1
            # even length string
            left, right = i, i + 1
            while s[left] == s[right] and left >= 0 and right < len(s):
                if right - left + 1 > lgst_str_idx:
                    start = left
                    lgst_str_idx = right - left + 1
                left -= 1
                right += 1
        return s[start : start + lgst_str_idx]
