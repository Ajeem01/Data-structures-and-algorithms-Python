def print_items(n):
    for i in range(n):
        for j in range(n):         # it is n*n therefore it is O(n^2), it is not efficient from time complexity stand point.
            for k in range(n):
                print(i,j,k)

print_items(10)