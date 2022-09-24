class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char.lower() for char in s if char.isalnum())
        new_string_length = len(new_string)
        left_pointer = (new_string_length - 1) // 2
        right_pointer = -((new_string_length - 1) // -2)  # trick for ceil division by making use of floor division
        while left_pointer >= 0 and right_pointer < new_string_length:
            if new_string[left_pointer] != new_string[right_pointer]:
                return False
            left_pointer -= 1
            right_pointer += 1

        if left_pointer >= 0 or right_pointer < new_string_length:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    answer = True
    assert (sol.isPalindrome(s) == answer)
    s = "race a car"
    answer = False
    assert (sol.isPalindrome(s) == answer)
    s = " "
    answer = True
    assert (sol.isPalindrome(s) == answer)
    s = "a"
    answer = True
    assert (sol.isPalindrome(s) == answer)
    s = "aA"
    answer = True
    assert (sol.isPalindrome(s) == answer)
    s = "Ana"
    answer = True
    assert (sol.isPalindrome(s) == answer)
    s = "ab"
    answer = False
    assert (sol.isPalindrome(s) == answer)