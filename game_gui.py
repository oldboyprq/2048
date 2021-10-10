# /usr/bin/python3
# coding:utf-8
# @Author:prq
# @Time:2021/10/10 21:47


import random


class Game:
    def __init__(self, size):
        # N*N的矩阵
        self.size = size
        self.matrix = [[0] * self.size for _ in range(self.size)]

    def calculate(self, nums):
        """
        [0,2,2,2,0,4]
        <-----
        [2,2,2,4]
        <------
        [4,0,2,4]
         <------
        [4,2,4],然后根据size补0
        """

        '''
        去0
        '''
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i = i + 1
        '''
        合并
        '''
        if len(nums) != 0:
            for i in range(len(nums) - 1):
                if (nums[i] == nums[i + 1]) and (nums[i] != 0):
                    nums[i] = nums[i] * 2
                    nums[i + 1] = 0
        '''
        去0
        '''
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i = i + 1
        '''
        补0
        '''
        while len(nums) < self.size:
            nums.append(0)
        return nums

    def random_num(self):
        """
        在为0的位置随机生成数
        """
        value_list = [2, 2, 2, 2, 4]  # 概率2 80% 4 20%
        position = list()
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] == 0:
                    position.append([i, j])
        if len(position) == 0:
            print("无空白区域，游戏结束")
            return 0
        '''随机选取位置'''
        point = position[random.randint(0, len(position) - 1)]
        i, j = point
        self.matrix[i][j] = random.choice(value_list)
        return 1

    def up(self):
        """
        0204      4 2 2 8
        2024 ---> 0 0 8 2
        2082      0 0 0 0
        """
        for i in range(self.size):
            # 上下按列拆分
            nums = list()
            for j in range(self.size):
                nums.append(self.matrix[j][i])
            nums = self.calculate(nums)
            for j in range(self.size):
                self.matrix[j][i] = nums[j]

    def down(self):
        for i in range(self.size):
            nums = list()
            for j in range(self.size - 1, -1, -1):
                nums.append(self.matrix[j][i])
            nums = self.calculate(nums)
            for j in range(self.size - 1, -1, -1):
                self.matrix[j][i] = nums[self.size - 1 - j]

    def left(self):
        # 左右按行拆分
        for i in range(self.size):
            nums = list()
            for j in range(self.size):
                nums.append(self.matrix[i][j])
            nums = self.calculate(nums)
            for j in range(self.size):
                self.matrix[i][j] = nums[j]

    def right(self):
        for i in range(self.size):
            nums = list()
            for j in range(self.size - 1, -1, -1):
                nums.append(self.matrix[i][j])
            nums = self.calculate(nums)
            for j in range(self.size - 1, -1, -1):
                self.matrix[i][j] = nums[self.size - 1 - j]

    def score(self):
        score = 0
        for i in range(self.size):
            if score < max(self.matrix[i]):
                score = max(self.matrix[i])
        return score
