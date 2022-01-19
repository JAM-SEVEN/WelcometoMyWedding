# -*- coding: utf-8 -*-
# @Time    : 19/1/2022 下午3:38
# @Author  : Jam
# @File    : containsDuplicate.py
# @Software: PyCharm
# @Todo    : 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        # number = []
        # for i in range(len(nums)):
        #     if  nums[i] in number:
        #         return True
        #     else:
        #         number.append(nums[i])
        # return False

        # solution 2
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        else:
            return True


if __name__ == '__main__':
    Solution = Solution()
    Nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = Solution.containsDuplicate(Nums)
    print(result)
