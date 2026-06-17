class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s[::-1]
        a=a.strip()
        c=0

        for i in range(len(a)-1+1):
            if a[i] != ' ':
                c+=1
            else:
                break
        return c