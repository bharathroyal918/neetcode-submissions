class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        
        pow=1
        while (True):
            pow *= 2
            if pow==n:
                return True
            elif pow > n:
                return False