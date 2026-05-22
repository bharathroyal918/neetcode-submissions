class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        arr = sorted(h, key=h.get, reverse=True)

        return arr[:k]