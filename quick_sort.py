def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(array,start,end):
    left = start + 1
    pivot = array[start]["nilai"]["uts"]
    for right in range(start+1,end):
        if pivot > array[right]:
            swap(array,left,right)
            left = left + 1
    swap(array,start,left-1)
    return left-1

def quickSortHelper(array,start,end):
    if start < end:
        splitPoint = partition(array,start,end)
        quickSortHelper(array,start,splitPoint)
        quickSortHelper(array,splitPoint+1,end)

def quickSort(array):
    quickSortHelper(array,0,len(array))

# array = [
#   {"nama":"Siti Aminah","nilai":{"uts":100,"uas":95}},
#   {"nama":"Siti Azizah","nilai":{"uts":90,"uas":80}},
#   {"nama":"Siti Fatimah","nilai":{"uts":99,"uas":87}},
#   {"nama":"Siti Aminah","nilai":{"uts":80,"uas":81}},
#   {"nama":"Siti Aminah","nilai":{"uts":95,"uas":98}},
#   ]

#bukan begini caranya, bambank....

array = [100,95,90,80,99,87,80,81,95,98]
quickSort(array)
print(array)