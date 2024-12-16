#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# 解题思路:
# 1. 首先计算链表长度,并将链表首尾相连形成环
# 2. 找到新的头节点和尾节点的位置
# 3. 断开环形链表,返回新的头节点
#
# 使用的数据结构和算法:
# - 链表
# - 双指针
#
# 时间复杂度: O(n), n为链表长度
# 空间复杂度: O(1)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 处理特殊情况
        if not head or not head.next or k == 0:
            return head
        
        # 计算链表长度,并找到尾节点
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
            
        # 计算实际需要移动的步数
        k = k % length
        if k == 0:
            return head
            
        # 将链表首尾相连形成环
        tail.next = head
        
        # 找到新的尾节点位置
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 找到新的头节点
        new_head = new_tail.next
        
        # 断开环形链表
        new_tail.next = None
        
        return new_head
        
# @lc code=end
