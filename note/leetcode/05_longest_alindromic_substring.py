'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindrome_dp(s)
	  
    def longestPalindrome_dp(self, s:str)->str:
        if not s or len(s) < 2:return s

        maxStr = s[0]
        slen, maxLen = len(s), 1

        # dp[i][j] 第i个到第j个字符是否为回文，是否存在回文
        dp = [ [False] * slen for _ in range(slen)]
        # for i in range(slen):
        #     dp[i][i] = True

        for i in range(slen):
            # # 单字符可构成回文
            dp[i][i] = True
            for j in range(i):
                # j ... i
                # s[j] == s[i] 相等，再判断 j+1 到 i-1 是否为回文
                # i-j in [0,1,2] aa/aba 只需要判断 s[j]==s[i] 且 i-j<=2时,j+1会>i-1
                if s[j] == s[i] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > maxLen:
                        maxLen = i-j+1
                        maxStr = s[j:i+1]
        
        return maxStr

    def longestPalindrome_recursion(self, s: str) -> str:

        if s==s[::-1]: 
            return s
        left = self.longestPalindrome(s[1:])
        right = self.longestPalindrome(s[:-1])

        if len(left)>len(right):
            return left
        else:
            return right

    
    def longestPalindrome_slice(self, s:str) -> str:
        if not s: return s

        slen = len(s)
        maxLen = 1
        maxStr = s[0]

        for i in range(slen):
            for j in range(slen-1, i-1,-1):
                if j-i+1 > maxLen and s[i:j+1] == s[i:j+1][::-1]:
                    maxLen = j-i+1
                    maxStr = s[i:j+1]
                    break
        return maxStr
        
    def longestPalindrome_bs(self, s:str) ->str:
        if not s: return s

        maxStr = s[0]

        for i in range(len(s)-1):
            subMax = self.longestPalindrome_bs_from_center(s, i,i) # bab 奇数
            if len(subMax) > len(maxStr):
                maxStr = subMax

            subMax = self.longestPalindrome_bs_from_center(s, i, i+1) # baab 偶数
            if len(subMax) > len(maxStr):
                maxStr = subMax

        return maxStr

    def longestPalindrome_bs_from_center(self, s:str, left:int, right:int):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left, right = left-1, right+1
        return s[left+1:right] # 最后一轮不符合条件前， left-1了，所以这里left+1进行归位








