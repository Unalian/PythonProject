class Solution:
    def func(self,s):
        print(s[1:2+1])
        hashmapNeed = {x:0 for x in s}
        print(hashmapNeed)
        for location, key in enumerate(hashmapNeed):
            print(location)
            print(key)





testA  = Solution()
testA.func("123")