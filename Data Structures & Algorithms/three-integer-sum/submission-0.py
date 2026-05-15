class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        h=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    t=nums[i],nums[j],nums[k]
                    h.add(t)
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return list(h)

        