# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_list=[]
#         t_list=[]
#         for i in s:
#             s_list.append(i)
        
#         for j in t:
#             t_list.append(j)
        
#         s_list.sort()
#         t_list.sort()

#         if s_list==t_list:
#             return True
#         else:
#             return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # return Counter(s) == Counter (t)

#         print (Counter(s))
#         print(Counter(t))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)