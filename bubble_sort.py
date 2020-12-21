def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    arr = [64, 34, 2, 5]
    bubble_sort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])


if __name__ == "__main__":
    main()
