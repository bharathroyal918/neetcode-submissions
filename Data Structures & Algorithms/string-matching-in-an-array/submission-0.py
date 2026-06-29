class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [word for i, word in enumerate(words)
                if any(i != j and word in words[j] for j in range(len(words)))]