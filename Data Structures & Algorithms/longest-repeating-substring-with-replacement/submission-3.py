class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {} # char : freq
        length = 0

        l = 0
        maxFreq = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxFreq = max(maxFreq, hashmap[s[r]]) 

            while (r - l + 1) - maxFreq > k:
                hashmap[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length