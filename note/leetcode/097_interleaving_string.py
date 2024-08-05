'''
97. Interleaving String

Medium

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.


Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave_recursion(s1, s2, s3)

    def isInterleave_recursion(self, s1, s2, s3)-> bool:
        self.ls1, self.ls2, self.ls3 = len(s1), len(s2), len(s3)
        if self.ls1 + self.ls2 != self.ls3: return False

        self.cache = {}
        return self._recursion(s1, s2, s3,0,0,0)

    def _recursion(self,s1, s2, s3, i,j,k) -> bool:
        if k == self.ls3:return True

        if (i,j) in self.cache:
            return self.cache[(i,j)]
        
        ans = False
        if i < self.ls1 and s1[i] == s3[k]:
            ans = ans or self._recursion(s1, s2, s3,i+1, j, k+1)
        
        if j < self.ls2 and s2[j] == s3[k]:
            ans = ans or self._recursion(s1, s2, s3,i, j+1, k+1)

        self.cache[(i,j)] = ans
        return ans


    def isInterleave_dp(self, s1, s2, s3) -> bool:
        ls1, ls2, ls3 = len(s1), len(s2), len(s3)
        if ls1 + ls2 != ls3: return False

        # dp[i][j]: s1[i] s2[j] 是否和 s[i+j] 匹配
        dp = [ [False]*(ls2+1) for _ in range(ls1+1) ]

        dp[0][0] = True

        for i in range(1,ls1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        for j in range(1,ls2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, ls1+1):
            for j in range(1, ls2+1):
                # dp[i][j] = dp[i-1][j] + s1[i] or dp[i][j-1] + s2[j]
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[ls1][ls2]
 