class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=-1
        right=-1
        for i in range(len(nums)):
            if nums[i]==target:
                if left ==-1:
                    left =i
                right=i
        return [left, right]