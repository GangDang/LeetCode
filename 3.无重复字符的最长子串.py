#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        flag=0;
        result=0;
        strlen=s.__len__();
        for i in range(0,strlen):
            for j in range(0,strlen):
                if s[i]==s[j] and i != j :
                    result= abs(i-j);
                    i=j;
                if result>flag :
                    flag=result;
                if flag==9:
                    print(i);
                    print(j);
        return flag;

test=Solution();
num = test.lengthOfLongestSubstring("adaddgghha");
print(num);
