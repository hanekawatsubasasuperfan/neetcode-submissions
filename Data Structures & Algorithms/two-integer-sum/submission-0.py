class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmaps = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmaps:
                return [hashmaps[val],i]
            hashmaps[nums[i]] = i