class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        i, j = 0, len(new_string) - 1
        while i < j:
            if new_string[i] != new_string[j]:
                return False
            i += 1
            j -= 1
        return True