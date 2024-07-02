solutions = 0
MAX_DIFF = 3

# 递归函数：将月饼分配给员工
def distribute_mooncakes(employee_index, min_mooncakes, max_mooncakes, remaining_mooncakes, total_employees):
    global solutions

    # 如果是最后一个员工，将所有剩余月饼分配给他们
    if employee_index == total_employees - 1:
        # 确保分配给最后一个员工的月饼数量符合条件
        if remaining_mooncakes - min_mooncakes <= MAX_DIFF:
            solutions += 1  # 找到一个有效分配方案
        return

    # 遍历当前员工可能分到的月饼数量
    for mooncakes_for_current in range(min_mooncakes, max_mooncakes + 1):
        remaining_mooncakes -= mooncakes_for_current  # 更新剩余月饼数量

        # 计算下一个员工可分得的月饼范围
        next_min = mooncakes_for_current  # 下一个员工至少要分得这么多
        # 下一个员工最多分得：剩余月饼数 / 剩余员工数，但不能超过当前员工数量 + MAX_DIFF
        next_max = min(mooncakes_for_current + MAX_DIFF, remaining_mooncakes // (total_employees - employee_index - 1))

        # 递归分配给下一个员工
        distribute_mooncakes(employee_index + 1, next_min, next_max, remaining_mooncakes, total_employees)

        remaining_mooncakes += mooncakes_for_current  # 恢复剩余月饼数量，为下一次循环做准备

# 主函数
def main():
    global solutions
    total_employees, total_mooncakes = map(int, input().split())

    if total_employees == 1:
        print("1")  # 只有一个员工，只有一种分配方案
    else:
        # 开始分配月饼，第一个员工至少分 1 个，最多分平均数
        distribute_mooncakes(0, 1, total_mooncakes // total_employees, total_mooncakes, total_employees)
        print(solutions)  # 输出总分配方案数

if __name__ == "__main__":
    main()
