import itertools

def optimal_arrangements(a, b):
    # 对a和b进行排序
    a.sort()
    b.sort()
    
    max_bigger_count = 0
    optimal_count = 0
    
    # 生成a的所有排列
    for perm in itertools.permutations(a):
        bigger_count = sum(1 for i in range(len(a)) if perm[i] > b[i])
        
        if bigger_count > max_bigger_count:
            max_bigger_count = bigger_count
            optimal_count = 1
        elif bigger_count == max_bigger_count:
            optimal_count += 1
    
    return optimal_count

if __name__ == "__main__":
    # 输入a和b的数组
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
  
    # 获取最优排列的数量
    result = optimal_arrangements(a, b)
    
    print(result)
