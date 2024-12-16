#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# 解题思路:
# 1. 使用虚拟头节点dummy简化边界情况处理
# 2. 使用双指针遍历链表:
#    - curr指向当前处理的节点
#    - next指向下一个节点
# 3. 比较相邻节点值,跳过所有重复节点
# 4. 使用prev指针维护最后一个不重复的节点
#
# 数据结构: 链表
# 算法: 双指针遍历
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
            
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next:
            # 初始化当前节点
            curr = prev.next
            # 计数当前值出现次数
            count = 1
            
            # 统计当前值出现的次数
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
                count += 1
                
            # 如果当前值只出现一次,移动prev指针
            if count == 1:
                prev = prev.next
            # 如果出现多次,跳过所有重复节点
            else:
                prev.next = curr.next
                
        return dummy.next

# @lc code=end
