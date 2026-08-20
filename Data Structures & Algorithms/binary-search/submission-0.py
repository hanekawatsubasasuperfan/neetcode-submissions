class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        
        0, 1 ,2, 3, 4, 5
        [-1,0,3,5,9,12]
        
        """
        l = 0
        r = len(nums)-1
        mid = len(nums)//2
        while l<=r:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                mid = (l+r) // 2 
            else:
                r = mid - 1
                mid = (r+l)//2
        return -1
            