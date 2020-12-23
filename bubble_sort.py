def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    arr = [64, 34, 2, 2, 2, 5]
    sorted_array = bubble_sort(arr)
    print("Sorted array is:")
    for element in sorted_array:
        print("%d" % element)


if __name__ == "__main__":
    main()
