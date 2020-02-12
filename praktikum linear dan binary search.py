"""Nomor 1"""

def linear_search(arr,n):
    print(arr)
    for i in range(len(arr)):
        if arr[i] == n:
            print("Data ditemukan, berada pada indeks ke-%s"%i)
            return True
    return False

arr = [1,2,3,4,5,6,7,8,9,19]
n = 8

if linear_search(arr,n):
    print("Found")
else:
    print("Not Found")

"""Nomor 2"""

def insertion_sort(arr):
    for i in range(len(arr)):
        nim = arr[i]["nim"]
        j=i
        while j>0 and nim < arr[j-1]["nim"]:
            arr[j]["nim"] = arr[j-1]["nim"]
            j-=1
        arr[j]["nim"]= nim
    return arr
        
def binary_search(arr,n):
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        # mencari nilai tengah
        mid = (first+last)//2
        if arr [mid]["nim"] == n:
        #found
            found = True
            print("Found on index %s"%mid)
        else:
            #kalau tidak ditemukan index pertama dan terakhirnya.
            if n < arr[mid]["nim"]:
                last = mid - 1
            else:
                first = mid + 1
    return found

arr = [
    {"nim": 18012, "nama":"Fulan"},
    {"nim": 18002, "nama":"Fulana"},
    {"nim": 18008, "nama":"Fulani"},
    {"nim": 18005, "nama":"Anton Antoni"},
    {"nim": 18010, "nama":"Ricky Rich"},
]

arr = insertion_sort(arr)
for i in range(len(arr)):
    print("%s"%arr[i])

print(binary_search(arr,18012))