'''
Для понимания лучше стартовать не с первого элемента - а с 3-4
Берем сразу второй элемент (поэтому с единицы), и предыдущий, значение текущего запоминаем в переменную
Дальше перезаписываем в цикле следующий элемент (без замены, а именно дублируя), если наткнулись на элемент меньше
запомненного - выходим и запихиваем на его место сохраненный
'''


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_value

    return arr


def main():
    arr = [64, 34, 2, 2, 2, 5]
    sorted_array = insertion_sort(arr)
    print("Sorted array is:")
    for element in sorted_array:
        print("%d" % element)


if __name__ == "__main__":
    main()
