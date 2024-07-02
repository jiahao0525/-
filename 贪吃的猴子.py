def max_bananas(length, bananas, times):
    # 初始化左边获取的香蕉数为0
    left_sum = 0
    # 初始化右边获取的香蕉数为最后N个元素的和
    right_sum = sum(bananas[-times:])
    
    # 初始情况下的最大值为右边获取的香蕉数
    max_bananas = right_sum

    # 逐步从左边获取香蕉并减少右边的香蕉数
    for i in range(times):
        # 左边多取一个，右边少取一个
        left_sum += bananas[i]
        right_sum -= bananas[-times + i]
        # 更新最大值
        max_bananas = max(max_bananas, left_sum + right_sum)

    return max_bananas

# 主函数，处理输入和输出
def main():
    length = int(input().strip())
    bananas = list(map(int, input().strip().split()))
    times = int(input().strip())
    result = max_bananas(length, bananas, times)
    print(result)

if __name__ == "__main__":
    main()
