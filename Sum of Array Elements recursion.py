def sum_array(n):

    if len(n)==1:
        return n[0]
    else:
        return n[0]+sum_array(n[1:])
        # n[0] is first index element + sum of n[1:](meaning 2 to last element of array)




a=[1,2,3,4,5]
print(sum_array(a))
