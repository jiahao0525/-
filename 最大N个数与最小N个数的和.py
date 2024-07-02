def calculate_sum_of_extremes(array, N):
    # 检查N是否有效
    if N <= 0:
        return -1
    
    unique_numbers = set()
    
    # 检查数组中的每个数并去重
    for num in array:
        if num < 0 or num > 1000:
            return -1
        unique_numbers.add(num)
    
    # 如果去重后的数字数量不足2N个，则返回-1
    if len(unique_numbers) < N * 2:
        return -1
    
    # 将去重后的数字排序
    sorted_numbers = sorted(unique_numbers)
    
    smallest_sum = sum(sorted_numbers[:N])
    largest_sum = sum(sorted_numbers[-N:])
    
    # 检查最小N个数和最大N个数是否重叠
    if sorted_numbers[N-1] >= sorted_numbers[-N]:
        return -1
    
    # 返回最大N个数与最小N个数的和
    return smallest_sum + largest_sum

if __name__ == "__main__":
    M = int(input())  # 读取数组大小
    array = list(map(int, input().split()))  # 读取数组内容
    N = int(input())  # 读取N的值
    
    result = calculate_sum_of_extremes(array, N)  # 计算结果
    print(result)  # 打印结果
