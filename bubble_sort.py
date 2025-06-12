def bubble_sort(n):
    for i in range(len(n)):
        # Last i elements are already in place
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:
                # Swap if the element found is greater than the next element
                n[j], n[j+1] = n[j+1], n[j] #swaping both element same time
    print(n)

bubble_sort([2,1,7,0])