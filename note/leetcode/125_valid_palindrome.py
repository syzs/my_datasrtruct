'''
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True

        start, end = 0, len(s)-1
        while start < end:
            h,t = s[start], s[end]
            if not h.isalnum():
                start+=1
                continue
            if not t.isalnum():
                end-=1
                continue
            if h.lower() != t.lower():
                return False
            start, end = start+1, end-1
        
        return True

    def isPalindrome_better(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b: return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True