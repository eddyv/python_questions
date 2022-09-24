class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}  # {'char': count}
        for char in s:
            char_map[char] = char_map[char] + 1 if char in char_map else 1
        for char in t:
            char_map[char] = char_map[char] - 1 if char in char_map else -1
        result = all(char_count == 0 for char_count in char_map.values())
        return result
