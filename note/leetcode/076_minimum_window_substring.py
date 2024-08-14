'''
76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

'''
class Solution:
    '''
    t = 'adasd'
    tm = collections.Counter(t)
    print(tm) # Counter({'a': 2, 'd': 2, 's': 1})
    print(tm['1']) # 0
    tm['p'] -=1
    print(tm) # Counter({'a': 2, 'd': 2, 's': 1, 'p': -1})
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        needstr = collections.Counter(t)
        needcnt,start = len(t), 0
        res = (0, len(s))

        for end, ch in enumerate(s):
            # 不存在的字符为负值，needstr[s[start]]==0 避免不存在的字符命中这行
            if needstr[ch] > 0: 
                needcnt -= 1 
            # 重复的字符需要累计计算，不能只在 needstr[ch]>0时-1
            needstr[ch] -= 1             
            if needcnt > 0:
                continue

            # needcnt == 0时，从start开始找，找到第一个在 t 中存在的字符
            while True:
                # 不存在于t, -1 后再 +1，就会存在在 needstr 中？？-> 先判==0再+1
                if needstr[s[start]] == 0: break
                needstr[s[start]] += 1
                start += 1

            if end-start < res[1]-res[0]: res = (start, end)

            # 把 start 的 去掉后重新往后计算
            needstr[s[start]] += 1
            needcnt += 1
            start += 1
        
        return '' if res[1] >= len(s) else s[res[0]: res[1]+1]

