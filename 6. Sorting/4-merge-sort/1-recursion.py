def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Storing elements in temp in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # If elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    # If elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Transferring all elements back to arr
    for i in range(low, high + 1): # here +1 bc python normally do -1
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid) # left half
    merge_sort(arr, mid + 1, high) # right half
    merge(arr, low, mid, high) # merge both halves

arr = [9, 4, 7, 6, 3, 1, 5]
merge_sort(arr, 0, len(arr) - 1) # len - 1 bc of how arr work in python eg., here 0 to 6 if there is no -1 it will be 0 to 7 which makes the length 8
print("Sorted array:", arr) # Sorted array: [1, 3, 4, 5, 6, 7, 9]