def get_higher_index(arr):
    stack = []  # 初始化一个栈，用于存储待比较的元素及其索引
    res = [0] * len(arr)  # 初始化一个结果列表，用于存储每个元素第一次遇到比它高的人的索引

    for i, ele in enumerate(arr):  # 遍历输入的数组
        while stack and ele > stack[-1][0]:  # 当栈不为空且当前元素比栈顶元素高
            _, peek_index = stack.pop()  # 弹出栈顶元素，并获取其索引
            res[peek_index] = i  # 更新栈顶元素对应的结果为当前元素的索引

        stack.append((ele, i))  # 将当前元素及其索引入栈

    return res  # 返回结果列表

if __name__ == "__main__":
    n = int(input())  # 输入数组的长度
    arr = list(map(int, input().split()[:n]))  # 输入数组

    result = get_higher_index(arr)  # 调用函数获取结果
    print(" ".join(map(str, result)))  # 将结果列表转换为字符串并输出
