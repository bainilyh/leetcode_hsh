#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 解题思路：迭代法两两交换相邻节点
        # 数据结构：链表
        # 算法：迭代

        # 创建哑节点，简化头节点的处理
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 当有两个节点可以交换时，继续迭代
        while head and head.next:
            # 保存要交换的两个节点
            first = head
            second = head.next

            # 交换节点
            prev.next = second
            first.next = second.next
            second.next = first

            # 移动指针，准备下一次交换
            prev = first
            head = first.next

        # 返回新的头节点
        return dummy.next

# @lc code=end

# 时间复杂度：O(n)，其中n是链表的节点数。我们需要遍历每个节点一次。
# 空间复杂度：O(1)。我们只使用了常数级的额外空间。
