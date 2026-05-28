class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suf=1
        ans=float('-inf')

        for i in range(len(nums)):
            if pre==0:
                pre=1

            if suf==0:
                suf=1
            
            pre*=nums[i]

            suf*=nums[len(nums)-i-1]

            ans=max(pre,suf,ans)
        return ans