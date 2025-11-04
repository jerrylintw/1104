def count_vowels(s):
    # 定義母音字符集（小寫字母）
    vowels = 'aeiou'
    
    # 計數母音數量
    count = 0
    
    # 遍歷字串中的每個字符
    for char in s:
        # 將字符轉小寫並檢查是否為母音
        if char.lower() in vowels:
            count += 1
    
    # 返回母音總數
    return count

# 主程序
s = input()  # 輸入字串
print(count_vowels(s))  # 輸出母音的數量