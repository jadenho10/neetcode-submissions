class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqList = defaultdict(int) # chars : freq
        res = 0
        l = 0
        maxFreq = 0
        for r in range(len(s)):
            freqList[s[r]] += 1
            maxFreq = max(maxFreq, freqList[s[r]])

            # check if we performed at most k replacements
            # if not we adjust left border by 1
            while (r - l + 1) - maxFreq > k:
                freqList[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res