def sum_to_n(n):
    if n==0 :
        return 0
    else:
        n += sum_to_n(n-1)
    return n 

c = int(input())
print(sum_to_n(c))