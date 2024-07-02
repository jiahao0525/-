# 获取输入字符串
s = input()

# 对字符串进行排序，得到按字典序排序后的字符串
sorted_str = ''.join(sorted(s))

# 如果排序后的字符串与原字符串相同，则说明已经是最小字符串，直接输出
if sorted_str == s:
    print(s)
else:
    # 将原字符串转换为列表，便于后续交换操作
    sb = list(s)
    
    # 遍历原字符串
    for i in range(len(s)):
        # 如果当前字符与排序后的字符不相同，则进行交换
        if s[i] != sorted_str[i]:
            # 找到排序后的字符在原字符串中从当前位置开始的第一个出现位置
            for j in range(i + 1, len(s)):
                if s[j] == sorted_str[i]:
                    swap_index = j
                    break
            
            # 将原字符与排序后的字符交换
            sb[i], sb[swap_index] = sb[swap_index], sb[i]
            break

    # 输出变换后的最小字符串
    print(''.join(sb))
