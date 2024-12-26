#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# 解题思路:
# 1. 如果总油量小于总消耗,则无法完成一圈
# 2. 如果总油量大于等于总消耗,则一定存在解
# 3. 从起点开始,如果当前累计剩余油量小于0,说明起点不对,需要将起点设为下一个点
#
# 使用的数据结构和算法:
# - 贪心算法
# - 一次遍历
#
# 时间复杂度: O(n) - 遍历一次数组
# 空间复杂度: O(1) - 只使用常数额外空间

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 计算总油量和总消耗
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 如果总油量小于总消耗,无法完成一圈
        if total_gas < total_cost:
            return -1
            
        # start为起点,curr_gas为当前累计剩余油量
        start = 0
        curr_gas = 0
        
        # 遍历所有加油站
        for i in range(len(gas)):
            # 计算当前位置剩余油量
            curr_gas += gas[i] - cost[i]
            
            # 如果累计剩余油量小于0
            if curr_gas < 0:
                # 将起点设为下一个位置
                start = i + 1
                # 重置累计剩余油量
                curr_gas = 0
                
        return start
        
# @lc code=end
