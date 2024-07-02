def get_result(heights):
    count = 0
    n = len(heights)

    # 遍历高度列表，检查每个位置是否为山峰
    for i in range(n):
        # 获取当前高度左侧和右侧的高度，边界情况设置为0
        left_height = heights[i - 1] if i > 0 else 0
        right_height = heights[i + 1] if i < n - 1 else 0

        # 判断当前高度是否比左右两侧高度都高，如果是则计数加一
        if heights[i] > left_height and heights[i] > right_height:
            count += 1

    return count

# 从输入中获取高度列表，输入以逗号分隔的字符串转换为整型列表
heights = list(map(int, input().split(',')))

# 调用函数并输出结果，打印出山峰的数量
print(get_result(heights))
