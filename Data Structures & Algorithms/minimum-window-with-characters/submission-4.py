class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float('inf')
        t_count, win_count = defaultdict(int), defaultdict(int)

        for c in t:
            t_count[c] += 1

        l = 0
        have, req = 0, len(t_count)
        # increment "have" if t_count[c] == win_count[c]
        for r in range(len(s)):
            c = s[r]
            win_count[c] += 1
            if c in t_count and t_count[c] == win_count[c]:
                have += 1
            while have == req:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                win_count[s[l]] -= 1
                if s[l] in t_count and win_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""
                

             

