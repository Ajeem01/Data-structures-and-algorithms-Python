def print_items(n):
    for i in range(n):     # n+n=(2n) so it is O(2n), we are dropping the constants so it is O(n).
        print(i)
    for j in range(n):
        print(j)

print_items(10)