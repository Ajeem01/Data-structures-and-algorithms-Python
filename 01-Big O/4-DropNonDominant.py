def print_items(n):
    for i in range(n):
        for j in range(n): #O(n^2)
            print(i,j)
    
    for k in range(n):    #O(n)
        print(k)
    
print_items(10) #O(n^2) + O(n), where O(n) is less dominant. 
                #for example if n=10 then O(n^2) is 100 and O(n) is 10. therefore O(n) is less dominant and dropped. 