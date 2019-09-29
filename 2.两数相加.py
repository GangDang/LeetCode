#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lsResult=ListNode(0);
        r=lsResult;
        carry=0;
        while l1 or l2 or carry==1 :
            l1Item =l1.val if l1 != None else 0;
            l2Item =l2.val if l2 != None else 0;
            itemResult=(l1Item+l2Item+carry)%10;
            carry=(l1Item+l2Item+carry)//10;
            node=ListNode(itemResult);
            r.next=node;
            if l1 != None : l1=l1.next;
            if l2 != None : l2=l2.next;
            r=r.next;

        return lsResult.next;
