#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# 解题思路:
# 1. 使用回溯算法(DFS)解决,通过递归不断选择数字组合
# 2. 因为每个数字可以重复使用,所以每次递归时从当前数字开始遍历
# 3. 使用一个临时数组path记录当前路径,一个结果数组res记录所有有效组合
# 4. 递归终止条件:
#    - 当目标值等于0时,说明找到一个有效组合
#    - 当目标值小于0时,说明当前组合无效,返回
#
# 数据结构:
# - 列表(List): 存储candidates数组、路径path和结果res
#
# 算法:
# - 回溯算法(DFS)
#
# 时间复杂度: O(n^(target/min)), 其中n是candidates数组长度,min是数组中最小值
# 空间复杂度: O(target/min), 递归调用栈的深度

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 定义结果数组
        res = []
        # 定义当前路径数组
        path = []
        
        def backtrack(start: int, target: int):
            # 找到一个有效组合
            if target == 0:
                res.append(path[:])
                return
            # 当前组合无效
            if target < 0:
                return
            
            # 从start开始遍历,保证不重复选择之前的数字
            for i in range(start, len(candidates)):
                # 选择当前数字
                path.append(candidates[i])
                # 递归,目标值减去当前数字
                backtrack(i, target - candidates[i])
                # 回溯,移除当前数字
                path.pop()
        
        # 调用回溯函数
        backtrack(0, target)
        return res
        
# @lc code=end
