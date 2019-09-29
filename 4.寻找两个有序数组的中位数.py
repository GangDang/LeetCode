#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: [], nums2: []) -> float:
        nums1Len=nums1.__len__();
        nums2Len=nums2.__len__();

        if nums1Len>nums2Len:
            nums1, nums2, nums1Len,nums2Len=nums2,nums1,nums2Len,nums1Len;
        if nums1Len<0 :
            raise ValueError;

        iMin,iMax,haftNum=0, nums1Len, (nums1Len+nums2Len+1)//2;
        
        while iMin <= iMax:
            i=(iMin+iMax)//2;
            j=haftNum-i;
            if i<nums1Len and nums2[j-1]>nums1[i]:
                iMin+=1;
            elif i>0 and nums1[i-1]>nums2[j]:
                iMax-=1;
            else :
                if i==0 : left_max_num=nums2[j-1]
                elif j==0 : left_max_num=nums1[i-1]
                else: left_max_num=max(nums1[i-1],nums2[j-1]);

                if (nums1Len+nums2Len)%2 ==1 : return left_max_num;

                if i==nums1Len : right_mini_num=nums2[j]
                elif j==nums2Len : right_mini_num=nums1[i]
                else: right_mini_num=min(nums2[j],nums1[i]);

                return (left_max_num+right_mini_num)/2.0;            
