def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while first <= last and not found:
        # mencari nilai tengah
        mid = (first+last)//2
        if item_list [mid] == item:
        #found
            found = True
            print("Found on index %s"%mid)
        else:
            #kalau tidak ditemukan index pertama dan terakhirnya.
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binary_search([1,2,4,6,7,9],6))
print(binary_search([1,2,4,6,7,9],3))

