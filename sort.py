array = list(map(int, input('Введите список числе через пробел ').split()))
element = int(input(f'Введите любое число: '))

for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

def BinarySearch(array, element):
    if element < array[0] or element > array[-1]: #невозможное событие
        return False
    first = 0
    last = len(array)
    while first < last - 1:
        mid = (first + last) // 2
        if element > array[mid]:
            first = mid
        else:
            last = mid
    return first


print(array)
print(BinarySearch(array, element))
