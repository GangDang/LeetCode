#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '':
            return ""    

        strlen = len(s)
        listStr = []
        newStr = ""

        if numRows>strlen :
            numRows=strlen;

        for tier in range(numRows):
            flag = True
            index = tier
            times = 0
            strRang = numRows-1
            listStr.append(s[tier])
            while flag:                
                if strRang == index:
                    if numRows==1 :
                        index=index+1;
                    else :
                        index=index+(numRows-1)*2;

                    strRang = index
                else:
                    if index > strRang:
                        index = (strRang+(numRows-1)*2)-(index-strRang)
                        strRang = index+(index-strRang)
                    else:
                        index = strRang+(strRang-index)
                        strRang = strRang+(numRows-1)

                if index > strlen-1 :
                    flag = False
                else:
                    if strlen-1==index :
                        flag=False;
                    if strlen-1==0 :
                        break;
                    listStr.append(s[index])

        newStr = newStr.join(listStr)
        return newStr


foo = Solution()
print(foo.convert('ABC', 1))

# @lc code=end
