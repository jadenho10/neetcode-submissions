class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        for i in range(len(s)):
            freq, maxCount = dict(), 0
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq.get(s[j], 0)
                maxCount = max(maxCount, freq[s[j]])
                window = j - i + 1
                if window - maxCount <= k:
                    res = max(res, window)
        return res



                