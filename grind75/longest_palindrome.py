from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = defaultdict(int)
        for char in s:
            char_map[char] += 1
        longest_palindrome = 0
        found_odd = False
        for key, value in char_map.items():
            if value % 2 == 1:
                if found_odd:
                    longest_palindrome += value - 1
                else:
                    longest_palindrome += value
                    found_odd = True
            elif value % 2 == 0:
                longest_palindrome += value
        return longest_palindrome
