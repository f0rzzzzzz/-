def heapify(arr, n, i):
    largest = i     #наибольшей размер как корень
    l = 2 * i + 1   #left
    r = 2 * i + 2   #right

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest)

def heapSort(arr):
    lenth = len(arr)

    for i in range(lenth, -1, -1):
        heapify(arr, lenth, i)

    for i in range(lenth-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [5, 16, 8, 14, 20, 1, 26]
print(f'Начальный список: {arr}')
heapSort(arr)
print(f'Отсортированный список: {arr}')