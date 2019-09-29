#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rightQueen=[];
        leftQueen=[];

        for item in s: 
            if rightQueen.__len__()>0:
                if item not in rightQueen:
                     rightQueen.append(item);
                else:                    
                    if leftQueen.__len__()<=rightQueen.__len__() :
                        leftQueen.clear();
                        leftQueen = combineArray(leftQueen,rightQueen);                       
                        
                        rightStartIndex=rightQueen.index(item)+1;
                        rightQueen=rightQueen[rightStartIndex:];
                        rightQueen.append(item);
                    else:
                        rightStartIndex=rightQueen.index(item)+1;
                        rightQueen=rightQueen[rightStartIndex:];
                        rightQueen.append(item);   
            else:
                if item in leftQueen :
                    rightStartIndex=leftQueen.index(item)+1;
                    rightQueen=leftQueen[rightStartIndex:];
                    rightQueen.append(item);
                    
                else:
                    leftQueen.append(item);
                    
        if leftQueen.__len__()<rightQueen.__len__() :
            return rightQueen.__len__() ;
        else :
            return leftQueen.__len__();

def combineArray(numbs1:[],numbs2:[])->[]:
        for item in numbs2:
            numbs1.append(item);
        return numbs1;