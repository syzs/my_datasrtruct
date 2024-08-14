'''
3. Longest Substring Without Repeating Characters

Medium

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0

        maxLen = -1
        window = []

        for c in s:
            while window and c in window:
                window.pop(0)
            
            window.append(c)
            maxLen = max(maxLen, len(window))
        return maxLen




        