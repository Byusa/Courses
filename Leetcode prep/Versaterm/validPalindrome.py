import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric
        cleaned_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return cleaned_s == cleaned_s[::-1]

