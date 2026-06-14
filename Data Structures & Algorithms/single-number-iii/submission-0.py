class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h={}
        res=[]
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        for i in h:
            if h[i]==1:
                res.append(i)
        return res