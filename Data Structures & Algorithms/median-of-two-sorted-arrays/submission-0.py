class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        i=0
        j=len(num)-1
        while i<j:
            i+=1
            j-=1
        if i==j:
            return num[i]*1.0
        else:
            x=num[i]+num[j]
            x=x*1.0
            return x/2