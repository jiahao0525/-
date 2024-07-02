def count_climbable_peaks(map_arr, stamina):
    """
    计算在给定体力下可以安全攀登的山峰数量。

    参数：
        map_arr: 表示地图高度的一维数组。
        stamina: 登山者的体力值。

    返回：
        可以安全攀登的山峰数量。
    """

    peaks = []  # 存储山峰信息（位置，高度）
    n = len(map_arr)

    # 识别山峰
    for i in range(n):
        # 判断当前位置是否为山峰：高于两侧或位于边界且高于相邻位置
        if (i == 0 or map_arr[i] > map_arr[i - 1]) and (i == n - 1 or map_arr[i] > map_arr[i + 1]):
            peaks.append((i, map_arr[i]))

    climbable_peaks = 0  # 可攀登的山峰数量

    # 计算体力消耗并判断是否可攀登
    for peak_pos, peak_height in peaks:
        climb_cost_left = climb_cost_right = descend_cost_left = descend_cost_right = 0

        # 计算从左侧攀登和下山的体力消耗
        for i in range(peak_pos - 1, -1, -1):  # 从峰顶向左遍历到地面
            climb_cost_left += 2 * max(0, map_arr[i + 1] - map_arr[i])  # 上山消耗体力为高度差的两倍
            descend_cost_left += max(0, map_arr[i + 1] - map_arr[i])  # 下山消耗体力为高度差

        # 计算从右侧攀登和下山的体力消耗
        for i in range(peak_pos + 1, n):  # 从峰顶向右遍历到地面
            climb_cost_right += 2 * max(0, map_arr[i] - map_arr[i - 1])
            descend_cost_right += max(0, map_arr[i] - map_arr[i - 1])

        # 判断是否可以安全攀登：
        # 选择左右两侧消耗体力较小的路径，判断总消耗是否小于等于体力值
        if min(climb_cost_left, climb_cost_right) + min(descend_cost_left, descend_cost_right) <= stamina:
            climbable_peaks += 1

    return climbable_peaks


# 获取用户输入
map_str = input()
map_arr = [int(x) for x in map_str.split(",")]
stamina = int(input())

# 计算并输出结果
result = count_climbable_peaks(map_arr, stamina)
print(result)
