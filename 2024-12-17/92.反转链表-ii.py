#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# 解题思路:
# 1. 找到要反转部分的前一个节点(pre_left)和起始节点(curr)
# 2. 使用头插法将left到right之间的节点逐个插入到pre_left之后
# 3. 需要特殊处理left=1的情况(使用dummy节点)
#
# 数据结构:
# - 链表(LinkedList): 存储和操作数据
# - 虚拟头节点(Dummy Node): 统一处理头节点的情况
#
# 算法:
# - 迭代法: 使用头插法实现局部反转

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 创建虚拟头节点,统一处理逻辑
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # 找到要反转部分的前一个节点
        for _ in range(left - 1):
            pre = pre.next
            
        # curr指向要反转部分的起始节点
        curr = pre.next
        # 进行right-left次头插操作
        for _ in range(right - left):
            # 保存下一个要插入的节点
            next_node = curr.next
            # 将next_node从链表中断开
            curr.next = next_node.next
            # 将next_node插入到pre后面
            next_node.next = pre.next
            pre.next = next_node
            
        return dummy.next

# 时间复杂度: O(n) - 需要遍历链表找到反转起点,然后进行反转操作
# 空间复杂度: O(1) - 只使用常数额外空间
# @lc code=end
