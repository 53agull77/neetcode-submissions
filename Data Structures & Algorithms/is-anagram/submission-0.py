class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for letter in s:
            table[letter] = table.get(letter, 0) + 1
        for letter in t:
            table[letter] = table.get(letter, 0) - 1
        for count in table.values():
            if count != 0:
                return False
        return True
