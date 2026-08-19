class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            v = ord(c)
            if 48<=v<=57:
                return True
            if 65<=v<=90:
                return True
            if 97<=v<=122:
                return True
            return False
        l = 0
        r = len(s)-1
        while l<r:
            while not isAlphaNum(s[l]) and l < r:
                l+=1
            while not isAlphaNum(s[r]) and r > l:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

        