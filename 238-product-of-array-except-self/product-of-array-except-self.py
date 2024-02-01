class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        answer=[1]*(len(nums))
        
        #Calculating Prefix
        for i in range(len(nums)):
            answer[i]=pre
            pre*=nums[i]

        #Calculating Postfix
        for i in range (len(nums)-1, -1, -1 ):
            answer[i]*=post
            post*=nums[i]
        return answer












        # answer=[]
        # copy=[]

        # def product(lst):
        #     result=1
        #     for i in range(len(lst)):
        #         result*=lst[i]
        #     return result

        # for i in range (len(nums)):
        #     copy=nums.copy()
        #     copy.pop(i)
        #     answer.append(product(copy))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           




        return answer

            