from collections import deque

def maximum_candies(N, matrix):
    # 初始化糖果矩阵
    candy = [[-1] * N for _ in range(N)]  # 初始化一个 N*N 的二维数组，用于记录到达每个格子时可以获得的最大糖果数

    # 定义偏移量，用于上下左右移动
    offsets = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    # 初始化妈妈的位置并加入队列
    for i in range(N):  # 遍历每一行
        if -3 in matrix[i]:  # 如果 -3（代表妈妈）在当前行中
            start_pos = (i, matrix[i].index(-3))  # 记录妈妈的位置
            candy[start_pos[0]][start_pos[1]] = 0  # 妈妈的位置糖果数为0，因为刚开始还没移动
            queue = deque([start_pos])  # 将妈妈的位置加入队列
            break  # 找到妈妈后就退出循环

    # 记录最大糖果数
    max_candies = -1  # 初始化最大糖果数为-1，用于记录最终结果

    # bfs 按层扩散
    while queue:  # 队列不为空时循环
        new_queue = deque()  # 用于存储下一层的点
        flag = False  # 用于标记是否找到宝宝的位置

        for pos in queue:  # 遍历当前层的点
            x, y = pos  # 获取当前点的坐标

            for offset in offsets:  # 遍历四个方向的偏移量
                new_x = x + offset[0]  # 计算新点的横坐标
                new_y = y + offset[1]  # 计算新点的纵坐标

                # 检查新点是否越界或者是障碍物
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or matrix[new_x][new_y] == -1:
                    continue  # 如果越界或者是障碍物，跳过当前点，继续下一个点

                if candy[new_x][new_y] == -1:  # 如果新点还未被访问过
                    new_queue.append((new_x, new_y))  # 将新点加入下一层队列

                # 更新新点的糖果数，取当前点的糖果数加上新点的糖果数与0的较大值
                candy[new_x][new_y] = max(candy[new_x][new_y], candy[x][y] + max(0, matrix[new_x][new_y]))

                if matrix[new_x][new_y] == -2:  # 如果新点是宝宝的位置
                    max_candies = candy[new_x][new_y]  # 更新最大糖果数
                    flag = True  # 标记找到宝宝的位置

        if flag:  # 如果找到了宝宝的位置
            break  # 退出循环，不再继续搜索

        queue = new_queue  # 将下一层的队列赋值给当前层队列，进行下一轮搜索

    return max_candies  # 返回最大糖果数

# 输入处理
N = int(input())  # 输入矩阵的大小
matrix = []  # 初始化矩阵
for _ in range(N):
    row = list(map(int, input().split()))  # 输入每一行的数据，并转换成整数列表
    matrix.append(row)  # 将每一行加入矩阵

# 计算结果并输出
result = maximum_candies(N, matrix)  # 调用函数计算结果
print(result)  # 输出结果
