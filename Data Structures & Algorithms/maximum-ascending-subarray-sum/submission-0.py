class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int: 
        maxsum=0
        
        for i in range(len(nums)):
            psum=nums[i]
            maxsum=max(maxsum,psum)

            for j in range(i+1,len(nums)):
                if nums[j]>nums[j-1]:
                    psum+=nums[j]
                    maxsum=max(psum,maxsum)
                else:
                    break
        return maxsum
        
        
        
        
        # maxsum=nums[0]
        # tsum=0

        # for i in range(len(nums)):
        #     tsum+=nums[i]
        #     if tsum > maxsum:
        #         maxsum=tsum
        #     maxsum=max(tsum,maxsum)
        # return maxsum
