def find_longest_substring_length(s):
    n = len(s)
    max_length = 0

    # 用于存储特定状态首次出现的位置
    state_to_index = {0: -1}
    # 初始化字符计数状态
    state = 0

    # 遍历字符串的两倍长度，以考虑环形结构
    for i in range(2 * n):
        # 计算当前字符在原字符串中的索引
        index = i % n
        ch = s[index]

        # 更新字符计数状态
        if ch == 'l':
            state ^= 1
        elif ch == 'o':
            state ^= 2
        elif ch == 'x':
            state ^= 4

        # 检查当前状态是否已存在
        if state in state_to_index:
            # 计算子字符串长度
            length = i - state_to_index[state]
            # 确保子字符串长度不超过原字符串长度
            if length <= n:
                max_length = max(max_length, length)
        else:
            # 存储首次出现的状态及其索引
            state_to_index[state] = i

    return max_length

def main():
    # 从标准输入读取字符串
    s = input()
    # 调用函数计算并返回结果
    result = find_longest_substring_length(s)
    # 打印结果
    print(result)

if __name__ == "__main__":
    main()
