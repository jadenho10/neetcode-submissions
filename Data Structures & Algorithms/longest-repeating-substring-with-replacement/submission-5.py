class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) # char : count
        res = 0
        maxFreq = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(count[s[r]], maxFreq)

            window = r - l + 1
            if window - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
