class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        while i <= len(nums)-1:
            if target > nums[i]:
                i+=1
            else:
                return i
        return i