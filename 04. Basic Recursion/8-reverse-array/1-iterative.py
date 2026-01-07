# function to print array
def printArray(arr):
    n = len(arr)
    print("The reversed array is: ")
    for i in range(n):
        print(arr[i], end=' ')
    print()

def reverseArray(i, arr):
    n = len(arr)
    while i <= n // 2:
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        i += 1
    printArray(arr)

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    reverseArray(0, arr)
    