class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float('inf')
        window, t_count = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        l = 0
        have, req = 0, len(t_count)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == req:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""

            
             