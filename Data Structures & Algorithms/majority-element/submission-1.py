class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return nums[0]

        count = 1
        res = nums[0]
        for i in nums:
            if i == res:
                count +=1
            else:
                count-=1
                if count == 0:
                    res = i
                    count = 1
                    
        return res