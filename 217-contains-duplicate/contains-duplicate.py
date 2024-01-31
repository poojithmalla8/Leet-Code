# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums_dict={}
#         for item in nums:
#             key= item
#             nums_dict[key]= None
        
#         if len(nums_dict)==len(nums):
#             return False
#         else:
#             return True


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset =set()
#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False
   
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else: return False