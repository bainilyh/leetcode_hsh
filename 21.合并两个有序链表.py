#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummp = ListNode(-1)
        cur, p1, p2 = dummp, list1, list2
        while p1 and p2:
            p1_val = p1.val
            p2_val = p2.val
            if p1_val <= p2_val:
                node = ListNode(p1_val)
                cur.next = node
                cur = cur.next
                p1 = p1.next
            else:
                node = ListNode(p2_val)
                cur.next = node
                cur = cur.next
                p2 = p2.next
        while p1:
            p1_val = p1.val
            node = ListNode(p1_val)
            cur.next = node
            cur = cur.next
            p1 = p1.next
        while p2:
            p2_val = p2.val
            node = ListNode(p2_val)
            cur.next = node
            cur = cur.next
            p2 = p2.next
        return dummp.next
        
# @lc code=end

