class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    pass
                else:
                    temp = prices[j]-prices[i]
                    print(temp)
                    if temp>cur_max:
                        cur_max=temp
        return cur_max