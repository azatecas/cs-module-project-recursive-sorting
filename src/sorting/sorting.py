# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)
        else:
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively 
def merge_sort(arr):
    # Your code here
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2

        arrA = merge_sort(arr[mid:])
        arrB = merge_sort(arr[:mid])

        sorted_arr = merge(arrA, arrB)

        return sorted_arr

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here



#text for commit
