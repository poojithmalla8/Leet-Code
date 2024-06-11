class Solution:
    def maxArea(self, height: List[int]) -> int:

        area=[]

        l=0
        r=len(height)-1

        for i,a in enumerate(height):

            
            h=min(height[l],height[r])
            b=r-l
                    
            area.append(h*b)
            
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max(area)