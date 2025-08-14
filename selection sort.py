def selection_sort(elements):

    for i in range(len(elements)):
            min_idx = i
            for j in range(i + 1, len(elements)):
                if elements[j] < elements[min_idx]:
                    min_idx = j
            elements[i], elements[min_idx] = elements[min_idx], elements[i]
    return elements     







print(selection_sort([2,9,1,5,6]))