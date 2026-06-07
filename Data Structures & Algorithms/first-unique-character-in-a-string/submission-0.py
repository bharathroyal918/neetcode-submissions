class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}

        for i in range(len(s)):
            if s[i] in h.keys():
                h[s[i]]+=1
            else:
                h[s[i]]=1
        
        for x,y in h.items():
            if y==1:
                return s.index(x)
        return -1