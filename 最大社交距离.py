def find_best_seat(occupied_seats, seat_num):
    """
    寻找最佳座位的函数
    :param occupied_seats: 已占用座位列表
    :param seat_num: 座位总数
    :return: 最佳座位编号
    """
    if not occupied_seats:
        return 0

    if len(occupied_seats) == 1:
        return seat_num - 1

    max_distance = 0
    best_seat = -1

    # 检查第一个座位
    if occupied_seats[0] > 0:
        max_distance = occupied_seats[0]
        best_seat = 0

    # 检查最后一个座位
    if seat_num - 1 - occupied_seats[-1] > max_distance:
        max_distance = seat_num - 1 - occupied_seats[-1]
        best_seat = seat_num - 1

    # 检查中间座位
    for i in range(1, len(occupied_seats)):
        distance = (occupied_seats[i] - occupied_seats[i - 1]) // 2
        if distance > max_distance:
            max_distance = distance
            best_seat = occupied_seats[i - 1] + distance

    return best_seat

def main():
    # 读取会议室座位总数
    seat_num = int(input())

    # 读取员工进出顺序，并转换为列表
    seat_or_leave = list(map(int, input().strip("[]").split(',')))

    occupied_seats = []  # 存储已占用座位的列表
    last_seat = -1  # 最后一个坐下的员工的座位号

    for action in seat_or_leave:
        if action == 1:
            # 找到最佳座位
            best_seat = find_best_seat(occupied_seats, seat_num)
            if best_seat != -1:
                occupied_seats.append(best_seat)  # 更新已占用座位列表
                occupied_seats.sort()  # 保持列表排序
                last_seat = best_seat  # 更新最后一个坐下的座位号
            else:
                last_seat = -1
        elif action < 0:
            # 出场操作
            leave_seat = -action  # 获取离开座位号
            if leave_seat in occupied_seats:
                occupied_seats.remove(leave_seat)  # 从已占用座位中移除

    print(last_seat)  # 输出最后一个进来员工的座位号

if __name__ == "__main__":
    main()
