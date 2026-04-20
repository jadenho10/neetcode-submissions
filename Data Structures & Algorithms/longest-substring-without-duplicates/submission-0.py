class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set() #make sure we know when duplicates occur
        count = 0

        l = 0
        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            count = max(r - l + 1, count)
        return count

            
            