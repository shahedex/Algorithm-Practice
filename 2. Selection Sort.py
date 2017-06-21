def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1,len(arr)):
        if(arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print("Enter the numbers to sort : ")
alist = [int(num) for num in input().strip().split(' ')]
new_list = selectionSort(alist)
print("Sorted list : ")
print(new_list)
