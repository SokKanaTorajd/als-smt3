data  = [72,42,35,12,101,5]
n =len(data)
looping = 0

def worse(data,n,looping):
    for i in range(n-1):
        for j in range(n-1):
            looping += 1
            if data[j] > data [j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                y,x = data[j], data[j+1]
                print(data)
    print(data, "total looping %i kali"%(looping))

worse(data,n,looping)

def average(data,n,looping):
    for i in range(n):
        for j in range(n-i-1):
            looping += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    print(data, "total looping %i kali"%(looping))

average(data,n,looping)

def best(data,n,looping):
    ditukar = True
    i = -1
    while ditukar:
        i+=1
        ditukar = False
        looping += 1
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                ditukar = True
                data[j], data[j+1] = data[j+1], data[j]
                            
    print(data, "total looping %i kali"%(looping))

best(data,n,looping)

"""
tugas insertion sort dikumpulkan hari jumat
kisi2 uts
definisi
selection array
bubble sort
membuat program dengan algoritma bubble sort

"""

