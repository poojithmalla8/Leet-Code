class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        diffmap={}

        for i,n in enumerate(nums):
            diff=target-n
            # print(diffmap)
            if diff in diffmap:
                return [diffmap[diff],i]
            diffmap[n]=i
        

        