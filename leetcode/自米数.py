class Solution:
    def is_flower(self, num):
        num_string = str(num)
        length = len(num_string)
        num_sum = 0
        for i in num_string:
            num_sum += int(i) ** length
        if num_sum == num:
            return True
        else:
            return False

    def find_flowers(self, max_numbers):
        result = []
        for i in range(1, max_numbers+1):
            if self.is_flower(i) is True:
                result.append(i)
        return result

a = Solution()
print(a.find_flowers(1000))



