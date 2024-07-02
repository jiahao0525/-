# 计算一个数的二进制表示中1的个数
def count_ones(x):
    return bin(x).count('1')

# 找到比给定数字x大的下一个数字y，使得y和x对应的二进制中1的个数相同
def find_next_number(x):
    ones_count = count_ones(x)  # 统计x中1的个数
    y = x + 1  # 初始y为x加1
    while count_ones(y) != ones_count:  # 当y的二进制表示中1的个数不等于x的时候
        y += 1  # 继续增加y
    return y

x = int(input())  # 从标准输入中读取整数x
result = find_next_number(x)  # 调用函数找到满足条件的y
print(result)  # 打印结果y
