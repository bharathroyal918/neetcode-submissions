class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h={}
        res=[]

        for i in nums:
            if i not in h:
                h[i]=1
        
        for i in range(1,len(nums)+1):
            if i not in h:
                res.append(i)
        return res