import re

class Solution:
     
    # Optimized
    # Bruteforce
    def longestPalindrome1(self, s: str) -> str:
        def isPalidrome(sub:str)-> bool:
            return sub == sub[::-1]

        longest = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                subString = s[i:j+1]
                if isPalidrome(subString):
                    if len(subString) > len(longest):
                        longest = subString

        return longest
    
    



    
    

        





