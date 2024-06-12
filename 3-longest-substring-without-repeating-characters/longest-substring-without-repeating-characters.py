class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()

        l=0
        res=0

        for r in range (len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1
            temp.add(s[r])
            res=max(res,r-l+1)
        return res
        