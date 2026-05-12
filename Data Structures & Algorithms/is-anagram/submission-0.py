class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        for i in s:
            if i in h1.keys():
                c1=h1[i]
                h1[i]=c1+1
            else:
                h1[i]=1

        for i in t:
            if i in h2.keys():
                c2=h2[i]
                h2[i]=c2+1
            else:
                h2[i]=1

        if (len(h1)!=len(h2)):
            return False

        for i in h1.keys():
            if i not in h2.keys():
                return False
            elif h1[i]!=h2[i]:
                return False
        return True  

        