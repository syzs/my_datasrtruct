'''
72. Edit Distance
Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''

class Solution:
    # https://leetcode.cn/problems/edit-distance/solutions/6455/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j]: word1 的第 i 个字符 => word2 的第j个字符，所需的最少的步数
        dp = [ [0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i # w1的第i个字符=> w2的第0个字符，需要操作i次
        
        for j in range(n+1):
            dp[0][j] = j # w1的第0个字符=> w2的第j个字符，需要操作j次
        '''
        if w1[i]==w2[j]: 不需要进行操作
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1             
       
        以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，因此有：

(1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）

(2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作

(3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符
        '''
        for i in range(1,m+1): 
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1             
        
        return dp[m][n]
        