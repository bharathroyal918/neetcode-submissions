class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        repeated = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                else:
                    seen.add(num)

        total = len(grid) * len(grid)

        for num in range(1, total + 1):
            if num not in seen:
                return [repeated, num]