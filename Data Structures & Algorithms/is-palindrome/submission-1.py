class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        # reverse = ""
        # for i in range(len(cleaned)-1,-1,-1):
        #     reverse += cleaned[i]
        # for i in range(len(reverse)):
        #     if cleaned[i] != reverse[i]:
        #         return False
        # return True
        l = 0
        r = len(cleaned)-1
        while l<r:
            if cleaned[l] != cleaned[r]:
                print(l)
                print(r)
                return False
            l+=1
            r-=1
        return True

        