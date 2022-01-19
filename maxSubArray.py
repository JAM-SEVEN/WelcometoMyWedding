# -*- coding: utf-8 -*-
# @Time    : 19/1/2022 下午3:28
# @Author  : Jam
# @File    : maxSubArray.py
# @Software: PyCharm

class Solution:
    def maxSubArray(self, nums) -> int:
        # res = nums[0]
        # sum = 0
        # for i in nums:
        #     if sum > 0:
        #         sum += i
        #     else:
        #         sum = i
        #     res = max(res, sum)
        # return res

        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    maxSubArray = solution.maxSubArray(nums)
    print(maxSubArray)
