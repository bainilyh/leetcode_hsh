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
        # 解题思路：迭代法合并两个有序链表
        # 数据结构：链表
        # 算法：双指针遍历

        # 创建哑节点作为合并后链表的头部
        dummy = ListNode(0)
        current = dummy

        # 同时遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                # 如果list1的值小于等于list2的值，将list1的节点接入结果链表
                current.next = list1
                list1 = list1.next
            else:
                # 否则，将list2的节点接入结果链表
                current.next = list2
                list2 = list2.next
            # 移动结果链表的指针
            current = current.next

        # 将剩余的节点接入结果链表
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # 返回合并后的链表，去掉哑节点
        return dummy.next

# @lc code=end

# 时间复杂度：O(m+n)，其中m和n分别是两个链表的长度。
# 我们需要遍历两个链表各一次。

# 空间复杂度：O(1)。我们只需要常数级的额外空间。
