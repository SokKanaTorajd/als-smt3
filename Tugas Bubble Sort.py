data  = [72,42,35,12,101,5]
n =len(data)  #banyaknya data
looping = 0

def worse_case(data,n,looping):
    """ Worst Case = (n-1)**2 """
    for i in range(n-1):
        for j in range(n-1):
            looping += 1
            if data[j] < data [j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    print(data, "\ntotal looping %i kali"%(looping))

worse_case(data,n,looping)    

def average_case(data,n,looping):
    """ Average Case = (n*(n-1))/2 """
    for i in range(n):
        for j in range(n-i-1):
            looping += 1
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    print(data, "\ntotal looping %i kali"%(looping))

average_case(data,n,looping)

def best_case(data,n,looping):
    """ Best Case = n """
    ditukar = True
    i = -1
    while ditukar:
        i+=1
        ditukar = False
        looping += 1
        for j in range(n-i-1):
            if data[j] < data[j+1]:
                ditukar = True
                data[j], data[j+1] = data[j+1], data[j]

    print(data, "\ntotal looping %i kali"%(looping))

best_case(data,n,looping)