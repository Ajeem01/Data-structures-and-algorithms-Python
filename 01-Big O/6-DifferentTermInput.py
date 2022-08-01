def print_items(a,b):
    for i in range(a):  #O(a)
        print(i)
    for j in range(b):  #O(b)
        print(j)

print_items(10,20)  #O(a+b)

def print_items2(a,b):
    for i in range(a):  #O(a)
        for j in range(b):  #O(b)
            print(i,j)
print_items2(10,20) #O(a*b)