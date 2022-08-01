#chack whether the two list contains common item.

#approach 1:

def item_in_common(list1, list2):
    for i in list1:
        for j in list2: #nested loop was O(n^2) therefore it is less efficient 
            if i == j:
                return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

#approach 2

def item_in_common2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True   #these are not nested loop and it is O(2n). remove constants so it is O(n).
                            # more efficient than first approach.
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))