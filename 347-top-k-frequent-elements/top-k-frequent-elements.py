class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort={}
        # for item in nums:
        #     sort[item]=nums.count(item)
        
        sort=Counter(nums)
        dict_sort=dict(sorted(sort.items(), key=lambda x:x[1], reverse=True))

        ans=list(dict_sort.keys())

        return ans[0:k]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = Counter(nums)
#         print(res)
#         res2 = [i for i in res.items()]
#         res2.sort(key=lambda x: x[1], reverse=True)
#         return [i[0] for i in res2[:k]]