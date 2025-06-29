def insertion_sort(n):
    newlist=[]
    for i in range(len(n)):
        # Last i elements are already in place
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:
                # Swap if the element found is greater than the next element

                newlist.append(n[j], n[j+1] = n[j+1], n[j]) #swaping both element same time
    print(n)

insertion_sort([2,1])