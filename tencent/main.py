class Solution:
    def func(self, list_inter):
        length = len(list_inter)
        res = []
        for i in range(length-2):
            for j in range(i+1, length-1):
                for r in range(j+1, length):
                    if list_inter[i] + list_inter[j] + list_inter[r] == 0:
                        res.append([list_inter[i], list_inter[j], list_inter[r]])
        return res


test = Solution()
print(test.func([1, -1, 2, 0, -2, 3, -3]))

