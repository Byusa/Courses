
"""
"abcbbacde"

"abc" : left "a",0 right: "b",3 -> left: "b",1, right:"b",4

Given a string s, return the longest 
substring that doesn't contain repeating characters.

Example 1:

Input: s = "abcbacbb"
Output: "abc"
Explanation: The answer is "abc", with the length of 3. "cba" "bac" "acb"
Example 2:

Input: s = "bbbbb"
Output: "b"
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: "wke"
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = "pwWkew"
Output: "Wke"
Explanation: The answer is "Wke", with the length of 3. 
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = "abcbacdefca"
Output: "bacdef"
Explanation: The answer is "bacdef", with the length of 6.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 520
s consists of English letters only, no whitespace or punctuation, //[a-zA-Z], case doesnt' matter for repeating "W" = "w" but returned substring should have case preserved
"""


class Solution:
    def longestSubstring(self, s: str) -> str:
        char_index = {}
        left = 0
        max_length = 0
        start = 0
        
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            
            if right - left + 1 > max_length:
               max_length = right - left + 1
               start = left
               
        return s[start:start+ max_length]
        
    print(longestSubstring("abcbbacde"))