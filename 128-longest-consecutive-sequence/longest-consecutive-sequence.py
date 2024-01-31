class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        longest=0
        
        for element in numset:
            if element-1 not in numset:
                length=1
                while element+length in numset:
                    length += 1
                longest=max(longest,length)
        return longest