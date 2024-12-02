# 元素无重复, 不可复选
# (子集)
res, trace = [], []
def dfs(nums, start):
    res.append(list(trace))
    for i in range(start, len(nums)):
        trace.append(nums[i])
        dfs(nums, i + 1)
        trace.pop()
# (组合)(和子集代码基本一样)
res, trace = [], []
def dfs(nums, start, k):
    if len(trace) == k:
        res.append(list(trace))
        return 
    for i in range(start, len(nums)):
        trace.append(nums[i])
        dfs(nums, i + 1)
        trace.pop()
# (排序)
nums = [1, 2,]
res, trace = [], []
used = [False] * len(nums)
def dfs(nums):
    if len(trace) == len(nums):
        res.append(list(trace))
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        trace.append(nums[i])
        used[i] = True
        dfs(nums[i])
        trace.pop()
        used[i] = False
        
        
        
# 元素可重复, 不可复选
# (子集和组合)
nums = [1, 2,]
res, trace = [], []
nums.sort() # [重点!!!!!!!!!!!!!!]
def dfs(nums, start):
    res.append(list(trace))
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:  # [重点!!!!!!!!!!!!!!]
            continue
        trace.append(nums[i])
        dfs(nums, i + 1)
        trace.pop()
# 组合时候可以减枝,详细见leetcode 40

# (排序)
nums = [1, 2,]
res, trace = [], []
used = [False] * len(nums)
def dfs(nums):
    if len(trace) == len(nums):
        res.append(list(trace))
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1] and not used[i- 1]:
            continue
        trace.append(nums[i])
        used[i] = True
        dfs(nums[i])
        trace.pop()
        used[i] = False




        
# 元素无重复, 可复选
# (子集和组合) 这里使用组合的例子, targetSum
res, trace = [], []
global curSum
curSum = 0
def dfs(nums, targetSum, start):
    if curSum == targetSum:
        res.append(list(trace))
        return
    if curSum > targetSum:
        return
    for i in range(start, len(nums)):
        trace.append(nums[i])
        curSum += nums[i]
        dfs(nums, targetSum, i)
        trace.pop()
        curSum -= nums[i]
        
# 思考排序的代码怎么写?