class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[int]:
            hashmaps = {}
            res = set()
            for i in range(len(nums)):
                val = target - nums[i]
                if val in hashmaps:
                    res.add(tuple(sorted([val, nums[i]])))
                hashmaps[nums[i]] = i
            return res
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            temp = twoSum(nums[i+1:], -nums[i])
            if temp:
                for j in temp:
                    res.append([nums[i],j[0],j[1]])
        return res