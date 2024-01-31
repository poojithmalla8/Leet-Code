class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansdict=defaultdict(list)
        
        for item in strs:
            k=sorted(item)
            # print(k)
            kkey="".join(k)
            # print(kkey)
            ansdict[kkey].append(item)
        # print(ansdict)
        # print(len(ansdict))

        ans=(ansdict.values())
        # print(ans)

        return (ans)

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = collections.defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()
