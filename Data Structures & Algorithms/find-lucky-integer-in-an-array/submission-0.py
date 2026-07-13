class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h={}

        for i in arr:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        maxx=-1

        for i in h.keys():
            if i == h[i]:
                maxx=max(maxx,i)
        return maxx
