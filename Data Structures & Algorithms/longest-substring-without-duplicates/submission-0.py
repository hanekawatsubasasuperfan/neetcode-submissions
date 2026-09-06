class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        cur_max = 0
        while r < len(s):
            if s[r] in seen:
                if r-l>cur_max:
                    cur_max = r-l
                l = max(l, seen[s[r]] + 1)
            seen[s[r]] = r
            r+=1
        return max(cur_max,r-l)