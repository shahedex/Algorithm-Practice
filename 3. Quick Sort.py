def quickSort(array):
    if(len(array) < 2):
        return array
    else:
        pivot = array[0]
        less_array = [i for i in array[1:] if i <= pivot]
        large_array = [i for i in array[1:] if i > pivot]

        return quickSort(less_array) + [pivot] + quickSort(large_array)

print("Enter the list to be sorted : ")
input_list = [int(i) for i in input().strip().split(' ')]
print("Sorted list : ")
print(quickSort(input_list))
