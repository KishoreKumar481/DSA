def frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_freq = 0
    min_freq = len(arr)
    max_ele = None
    min_ele = None

    for element, count in freq.items():
        if count > max_freq:
            max_freq = count
            max_ele = element
        if count < min_freq:
            min_freq = count
            min_ele = element
        
    print("The highest frequency element is:", max_ele) # 10
    print("The lowest frequency element is:", min_ele) # 15

arr = [10, 5, 10, 15, 10, 5]
frequency(arr)
