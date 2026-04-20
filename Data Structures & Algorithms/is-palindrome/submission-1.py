class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1
        while front < back:
            if not s[front].isalnum():
                front += 1
            elif not s[back].isalnum():
                back -= 1
            else:
                if s[front].lower() != s[back].lower():
                    return False
                front += 1
                back -= 1
        return True
        
        