#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# 解题思路:
# 1. 使用单指针遍历链表
# 2. 比较当前节点和下一个节点的值:
#    - 如果相等,跳过下一个节点
#    - 如果不等,移动指针到下一个节点
# 3. 由于链表已排序,相同元素一定相邻
#
# 数据结构: 链表
# 算法: 单指针遍历
#
# 时间复杂度: O(n), 其中n为链表长度,需要遍历一遍链表
# 空间复杂度: O(1), 只使用常数额外空间

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 处理空链表和单节点链表
        if not head or not head.next:
            return head
            
        # 初始化当前节点指针
        curr = head
        
        # 遍历链表
        while curr.next:
            # 如果当前节点值等于下一节点值
            if curr.val == curr.next.val:
                # 跳过下一个节点
                curr.next = curr.next.next
            else:
                # 移动到下一个节点
                curr = curr.next
                
        return head
        
# @lc code=end
