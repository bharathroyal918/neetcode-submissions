class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for c1, c2 in zip(s, t):
            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2

            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1

        return True