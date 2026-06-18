class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}

        cap= len(nums)//2

        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
            
        for i in h:
            if h[i] >cap:
                return i
        
        return -1