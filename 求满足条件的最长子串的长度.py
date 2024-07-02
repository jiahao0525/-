def longest_valid_substring(s):
    max_length = -1
    n = len(s)
    
    # 遍历每一个字符，以它为起点进行子串搜索
    for i in range(n):
        num_count = 0
        letter_count = 0
        letter = ''
        
        # 从当前字符开始，向后检查每一个字符，形成子串
        for j in range(i, n):
            if s[j].isdigit():
                num_count += 1
            elif s[j].isalpha():
                if letter == '':
                    letter = s[j]
                    letter_count += 1
                elif letter == s[j]:
                    letter_count += 1
                else:
                    break  # 如果出现了不同的字母，结束当前子串的搜索
            
            # 检查当前子串是否满足条件
            if num_count > 0 and letter_count == 1:
                max_length = max(max_length, j - i + 1)
    
    return max_length

# 用户输入部分
input_string = input()
result = longest_valid_substring(input_string)
print(result)
