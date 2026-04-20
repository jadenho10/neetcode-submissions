class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        hashmap = {}
        l = 0

        maxChar = float("-inf")
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxChar = max(maxChar, hashmap[s[r]])

            while (r - l + 1) - maxChar > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

                