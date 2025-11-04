def fib(n):
    # 基底條件
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 遞迴條件
    else:
        return fib(n - 1) + fib(n - 2)

# 主程序
n = int(input())  # 輸入一個非負整數 N
print(fib(n))  # 輸出第 N 項費波那契數列
