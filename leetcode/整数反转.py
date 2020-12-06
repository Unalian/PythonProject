class Solution:
    def func(self, x):
        res = 0
        k = 0
        intMax = pow(2,31) -1
        while x!= 0:
            if x < 0:
                k = 1
                x = -x
            pop = x%10
            x = int(x/10)
            if (res > intMax/10) or (res == intMax/10 and pop> 7) :
                return 0
            res = res*10 + pop
        if k == 1:
            res = -res
        return res

testA = Solution()
print(testA.func(-12345))

# 动态规划

class Solution:
    def func(self, nums):
        # 1. 状态定义
        dp = [0]* len(nums)
        # 2. 状态初始化
        dp[0] = nums[0]
        ans = nums[0]
        # 3.状态转移 dp[i] = max(dp[i-1],0)+nums(i) dp[i]指1 i+1位 的最大子序和
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1],0)+nums[i]
            ans = max(dp[i], ans)
        return ans
    # dp[i]只是一个状态值，所以可以不做成数组

    def func2(self, nums):
        # 1. 状态定义
        # 2. 状态初始化
        countSum = nums[0]
        ans = nums[0]
        # 3.状态转移 dp[i] = max(dp[i-1],0)+nums(i) dp[i]指1 i+1位 的最大子序和
        for i in range(1, len(nums)):
            countSum = max(countSum, 0) + nums[i]
            ans = max(countSum, ans)
        return ans
