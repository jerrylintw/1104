def filter_by_threshold(numbers, limit):
    # 使用 list comprehension 進行篩選
    return [num for num in numbers if num > limit]
#這裡是篩選函數，會回傳大於 limit 的數字列表 

# 主程序
numbers = list(map(int, input().split()))  # 輸入並轉換為整數串列
limit = int(input())  # 輸入 limit 整數

# 呼叫篩選函數並輸出結果
result = filter_by_threshold(numbers, limit)
print(result)
