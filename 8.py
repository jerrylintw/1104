def gcd(a, b):
    # 基底條件
    if b == 0:
        return a
    # 遞迴條件
    else:
        return gcd(b, a % b)

# 主程序
a, b = map(int, input().split())  # 輸入兩個非負整數 a 和 b
print(gcd(a, b))  # 輸出 a 和 b 的最大公因數
