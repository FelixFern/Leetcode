class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_hash = {}
        magazine_hash = {}

        for i in ransomNote:
            ransom_hash[i] = ransom_hash.get(i, 0) + 1

        for i in magazine:
            magazine_hash[i] = magazine_hash.get(i, 0) + 1

        for i in ransom_hash:
            if (ransom_hash.get(i) > magazine_hash.get(i, 0)):
                return False

        return True
