class Solution:
    def func(self, x):
        if x < 0 or (x != 0 and x%10 != 0):
            return False
        reves = 0
        while x > reves:
            reves = x%10 + 10* reves
            x = int(x / 10)
        # print(x, reves)
        reves2 = int(reves / 10)
        return (reves == x) or  reves2 == x

a = Solution()
print(a.func(12321))


"""pay attention to the int type"""