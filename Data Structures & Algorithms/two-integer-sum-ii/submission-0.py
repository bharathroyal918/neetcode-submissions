class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j]==target:
                ans=[i+1,j+1]
                return ans
            elif num[i]+num[j]>target:
                j-=1
            else:
                i+=1
        return ans