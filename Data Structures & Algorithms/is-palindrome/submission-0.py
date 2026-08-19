class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        reverse = ""
        for i in range(len(cleaned)-1,-1,-1):
            reverse += cleaned[i]
        for i in range(len(reverse)):
            if cleaned[i] != reverse[i]:
                return False
        return True