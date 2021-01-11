'''Ищет с начала массива наименьший элемент, если найден меньше - делает его активным
В конце массива делает наименьший элемент текущим
Т.к. сокращает область слева - от i+1 до n'''


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index_of_min_element = i
        for j in range(i+1, n):
            if arr[j] < arr[index_of_min_element]:
                index_of_min_element = j
        arr[i], arr[index_of_min_element] = arr[index_of_min_element], arr[i]
    return arr


def main():
    arr = [64, 34, 2, 2, 5, 7, 5]
    sorted_array = selection_sort(arr)
    print("Sorted array is:")
    for element in sorted_array:
        print("%d" % element)


if __name__ == "__main__":
    main()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         index_of_min_element = i
#         for j in range(i+1, n):
#             if arr[j] < arr[index_of_min_element]:
#                 index_of_min_element = j
#         arr[i], arr[index_of_min_element] = arr[index_of_min_element], arr[i]
#     return arr
