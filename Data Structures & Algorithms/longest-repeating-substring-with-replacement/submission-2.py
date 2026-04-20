class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = dict()
        length = 0
        maxChar = 0
        l = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxChar = max(hashmap[s[r]], maxChar)
            while (r - l + 1) - maxChar > k:
                hashmap[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length
                