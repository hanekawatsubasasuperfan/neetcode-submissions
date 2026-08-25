class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        
        count = 0
        mid = False
        for key in hashmap:
            cur = hashmap[key]
            if cur % 2 == 0:
                count += cur
            else:
                count += cur-1
                mid = True
        if mid:
            count+=1
        return count