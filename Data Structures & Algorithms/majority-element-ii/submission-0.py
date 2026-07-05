class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        for i in nums:
            if i in h.keys():
                h[i]+=1
            else:
                h[i]=1

        x=[]
        for i in h.keys():
            if h[i] > len(nums)//3:
                x.append(i)
        return x