class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # track set of chars in our window
        l = 0
        res = 0
        for r in range(len(s)):
            # remove s[l] iff s[r] in charset
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
