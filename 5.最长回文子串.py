#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #判断字符串长度是否为零
        if len(s)==0 :
            return "";
        #字符串长度
        strLen=len(s);
        #回文字符串，默认字符串第一个
        palindromeStr=s[0];
        #回文字符串长度，默认1
        longestPalindromeLen=1;
        #布尔型二维数组，用于记录字符串存在的回文字符串地址
        db=[[False for _ in range(strLen)]  for _ in range(strLen)];

        #字符串右边索引一定大于1
        for rightIndex in range(1,strLen) :
            for leftIndex in range(rightIndex) :
                if s[leftIndex]==s[rightIndex] and (rightIndex-leftIndex <= 2 or db[leftIndex+1][rightIndex-1]) :
                    db[leftIndex][rightIndex]=True;
                    #当回文字符串
                    currentPalindrome=s[leftIndex:rightIndex+1];
                    #当回文字符串长度
                    currentPalindromeLen=rightIndex-leftIndex + 1;
                    if currentPalindromeLen>longestPalindromeLen :
                        longestPalindromeLen=currentPalindromeLen;
                        palindromeStr=currentPalindrome;
        for item in db :
            print(item);

        return palindromeStr;
# @lc code=end

