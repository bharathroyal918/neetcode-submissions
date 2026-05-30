class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans=nums[0]
        idx=0

        for i in range(len(nums)):
            if nums[i] > ans:
                ans=nums[i]
                idx=i
        return idx
