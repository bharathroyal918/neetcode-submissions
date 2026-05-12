class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        ans=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if x in d:
                ans.append(d.get(x))
                ans.append(i)
                return ans
            d[nums[i]]=i