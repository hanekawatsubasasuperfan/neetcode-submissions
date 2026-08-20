class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c]+=1
        print(hashmap)
        for c in t:
            if c not in hashmap:
                return False
            elif c in hashmap:
                if hashmap[c] == 0:
                    return False
                else:
                    hashmap[c]-=1
        return True