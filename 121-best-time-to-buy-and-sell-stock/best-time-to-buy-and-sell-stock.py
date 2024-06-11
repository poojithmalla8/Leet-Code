class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0

        l=0 #Buy
        r=1 #Sell

            
        while r<len(prices):
            
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,profit)
                
            else:
                l=r
            r+=1
        return maxprofit
            
