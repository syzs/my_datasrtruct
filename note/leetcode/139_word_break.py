'''
139. Word Break

Medium

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

'''

class Solution:
    def wordBreak(self, s:str, wordDict:List[str])->bool:
        return self.wordBreak_dp(s, wordDict)
    
    def wordBreak_recursion(self, s:str, wordDict:List[str]) -> bool:
        if not s or s in wordDict: return True

        for w in wordDict:
            if s.startswith(w):
                return self.wordBreak_recursion(s[len(w):], wordDict)
        
        return False
            

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # dp[i][j]:  是否可由 w[j] 组成
        dp = [False] * (n+1)
        dp[0] = True
        maxLen = max(map(len, wordDict))

        # 前i个字符是否可匹配
        for i in range(1, n+1):
            # max(i-maxLen-1, -1): 以最长的word为准找匹配的单词，索引最小不能<-1
            for j in range(i-1, max(i-maxLen-1, -1),-1):
                # j 前面的字符是匹配成功的 and s[j:i] 可以在字典里找到
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]