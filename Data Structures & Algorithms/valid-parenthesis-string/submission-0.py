class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount, closedCount = 0, 0
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                openCount += 1
            else:
                openCount -= 1
            
            if s[len(s) - 1 - i] == ")" or s[len(s) - 1 - i] == "*":
                closedCount += 1
            else:
                closedCount -= 1
            if closedCount < 0 or openCount < 0:
                return False
        return True