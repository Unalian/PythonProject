import sys
from collections import deque
class Solution:
    def func(self,s):
        print(s[1:2+1])
        hashmapNeed = {x:0 for x in s}
        print(hashmapNeed)
        for location, key in enumerate(hashmapNeed):
            print(location)
            print(key)

    def func2 (self):
        # 队列
        dp = [1,2,3]
        que = deque(dp)
        que.popleft()
        dp2 = list(que)
        print(dp2)

    def func3(self):
        list = [1,2,3]
        print(list[:3])

# str = list(map(int,sys.stdin.readline().split()))
#print(str)
# print(type(str))

A = Solution()
A.func3()