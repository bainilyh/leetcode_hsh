#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 解题思路：双指针（快慢指针）
        # 数据结构：链表
        # 算法：快慢指针

        # 创建一个虚拟头节点，用于处理删除头节点的情况
        dummy = ListNode(0)
        dummy.next = head
        
        # 初始化快慢指针，都指向虚拟头节点
        fast = slow = dummy
        
        # 快指针先移动n步
        for _ in range(n):
            fast = fast.next
        
        # 同时移动快慢指针，直到快指针到达链表末尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 删除倒数第n个节点
        slow.next = slow.next.next
        
        return dummy.next

# @lc code=end

# 时间复杂度：O(L)，其中L是链表的长度。我们只遍历了链表一次。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间。
