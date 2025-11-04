def factorial(n):
    # 基底條件
    if n == 0:
        return 1
    # 遞迴步驟
    else:
        return n * factorial(n - 1)

# 主程序
n = int(input())  # 輸入一個非負整數
print(factorial(n))  # 輸出 n 的階乘
