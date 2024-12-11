#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# 解题思路:
# 1. 使用回溯法解决,需要先对数组排序以便去重和剪枝
# 2. 递归函数中记录当前和、当前选择的数字、开始位置
# 3. 通过排序后的剪枝和同层去重避免重复组合
# 
# 数据结构: 
# - 列表存储结果集和当前路径
# - 递归调用栈
#
# 算法:
# - 回溯法(DFS)
# - 排序
# - 剪枝优化

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 定义结果列表和当前路径列表
        res = []
        path = []
        
        # 对候选数组排序,用于去重
        candidates.sort()
        
        def backtrack(start: int, target: int):
            # 找到目标和,将当前路径加入结果集
            if target == 0:
                res.append(path[:])
                return
            
            # 遍历候选数字
            for i in range(start, len(candidates)):
                # 剪枝:如果当前数字大于目标值,后面更大的数字都不需要遍历
                if candidates[i] > target:
                    break
                    
                # 同一层级的数字要去重
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                # 选择当前数字
                path.append(candidates[i])
                # 递归下一层,注意是i+1避免重复使用
                backtrack(i + 1, target - candidates[i])
                # 撤销选择
                path.pop()
        
        backtrack(0, target)
        return res

# @lc code=end

# 时间复杂度: O(2^n), n为candidates长度,每个数字都有选和不选两种状态
# 空间复杂度: O(n), n为递归调用栈的深度
