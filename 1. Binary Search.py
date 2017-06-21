def binary_search(list, search_item):
    low = 0
    high = len(list)-1

    while(low<=high):
        mid = round((low+high)/2)
        #print(mid)
        guess = list[mid]

        if(guess == search_item):
            return mid
        elif(guess > search_item):
            high = mid-1
        else:
            low = mid+1
    return None

search_range_lower, search_range_upper = map(int,input("Enter search range(?-?):").split())
search_item = int(input("Enter search item: "))

list = [i for i in range(search_range_lower,search_range_upper)]
index_found = binary_search(list,search_item)
print(list)
if index_found != None : print("Search item found in index : %d" %index_found)
else : print("No result found")
