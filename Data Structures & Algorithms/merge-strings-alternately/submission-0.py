class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        i=0
        j=0

        ans=""

        x=min(len(a),len(b))
        for i in range(x-1+1):
            ans=ans+a[i]+b[i]
        
        ans+=a[x:]
        ans+=b[x:]

        return ans