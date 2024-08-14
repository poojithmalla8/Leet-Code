class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1 
        curr_min = nums[0]
        
        while l  <  r :
            mid = l + (r - l ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[r]:
                l = mid + 1
                
            # left has the  min 
            else:
                r = mid - 1 
                
        return min(curr_min,nums[l])