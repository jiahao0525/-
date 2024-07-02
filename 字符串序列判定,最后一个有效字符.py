def find_last_valid_char(stringS, stringL):
    """
    判断字符串S是否是字符串L的有效子串，并返回S最后一个有效字符在L中的位置。

    参数:
        stringS: 字符串S，只包含英文小写字母。
        stringL: 字符串L，只包含英文小写字母。

    返回:
        int: S最后一个有效字符在L中的位置（从0开始），如果S不是L的有效子串，则返回-1。
    """

    # 使用字典存储每个字符在L中最后出现的位置
    char_last_index = {}
    for i, char in enumerate(stringL):
        char_last_index[char] = i

    last_valid_index = -1  # 初始化最后一个有效字符的索引为-1
    for char in stringS:
        # 如果字符不在L中，或者字符在L中的最后出现位置小于等于上一个有效字符的位置，则不是有效子串
        if char not in char_last_index or char_last_index[char] <= last_valid_index:
            return -1
        last_valid_index = char_last_index[char]  # 更新最后一个有效字符的索引

    return last_valid_index  # 返回最后一个有效字符的索引

# 从标准输入读取两个字符串
stringS = input()
stringL = input()

# 调用函数查找最后一个有效字符的位置并打印结果
last_valid_index = find_last_valid_char(stringS, stringL)
print(last_valid_index)
