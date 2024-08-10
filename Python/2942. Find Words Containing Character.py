class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, val in enumerate(words):
            if x in val:
                res.append(idx)
        return res
