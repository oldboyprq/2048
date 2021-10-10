# /usr/bin/python3
# coding:utf-8
# @Author:prq
# @Time:2021/10/10 14:03


nums = [4, 0, 4, 4]
i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
    else:
        i = i + 1
if len(nums) != 0:
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i + 1]) and (nums[i] != 0):
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
    else:
        i = i + 1
while len(nums) < 4:
    nums.append(0)

print(nums)

