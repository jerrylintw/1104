def is_palindrome(s):
    # 判斷字串是否等於其反轉字串
    return s == s[::-1]

# 主程序
s = input()  # 輸入字串
if is_palindrome(s):
    print("Yes")
else:
    print("No")
