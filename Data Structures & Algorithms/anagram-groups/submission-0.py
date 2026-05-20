class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in h:
                h[key].append(word)
            else:
                h[key] = [word]
        return list(h.values())