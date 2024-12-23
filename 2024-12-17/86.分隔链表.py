#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# 解题思路:
# 1. 使用两个链表分别存储小于x和大于等于x的节点
# 2. 遍历原链表,根据节点值的大小将节点分配到对应的链表
# 3. 最后将两个链表连接起来
#
# 数据结构: 链表
# 算法: 双指针
#
# 时间复杂度: O(n) - 只需遍历一次链表
# 空间复杂度: O(1) - 只使用了常数个额外空间

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 创建两个虚拟头节点
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)
        # 创建两个指针分别指向两个链表的当前节点
        small = small_dummy
        large = large_dummy
        
        # 遍历原链表
        while head:
            if head.val < x:
                # 将小于x的节点连接到small链表
                small.next = head
                small = small.next
            else:
                # 将大于等于x的节点连接到large链表
                large.next = head
                large = large.next
            head = head.next
        
        # 将large链表的末尾置为None
        large.next = None
        # 将small链表与large链表连接
        small.next = large_dummy.next
        
        return small_dummy.next
        
# @lc code=end
