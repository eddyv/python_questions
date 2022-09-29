from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(lambda x: 0)
        for char in magazine:
            letters[char] += 1
        for char in ransomNote:
            letters[char] -= 1
        return all(value > 0 for value in letters.values())
