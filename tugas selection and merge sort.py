import sys

nilai_uts = [
    {"nama" : "Siti Azizah","nilai" : 85},
    {"nama" : "Siti Aminah","nilai" : 95},
    {"nama" : "Siti Fatimah","nilai" : 75},
    {"nama" : "Siti Maimunah","nilai" : 70},
    {"nama" : "Siti Komariah","nilai" : 90},
]

def selection(nilai_uts):
    for i in range(0,len(nilai_uts)):
        min_idx = i
        for j in range(i+1, len(nilai_uts)):
            if nilai_uts[min_idx]["nilai"] > nilai_uts[j]["nilai"]:
               min_idx=j
        nilai_uts[i],nilai_uts[min_idx] = nilai_uts[min_idx], nilai_uts[i]
    return nilai_uts

nilai_uts = selection(nilai_uts)
for i in range(len(nilai_uts)):
    print("%s"%nilai_uts[i])

def merge(nilai_uts):
    print("Splitting", nilai_uts)
    if len(nilai_uts)>1:
            mid = len(nilai_uts)//2
            lefthalf = nilai_uts[:mid]
            righthalf = nilai_uts[mid:]

            lefthalf = merge(lefthalf)
            righthalf = merge(righthalf)

            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i]["nilai"] <= righthalf[j]["nilai"]:
                    nilai_uts[k]=lefthalf[i]
                    i+=1
                else:
                    nilai_uts[k]=righthalf[j]
                    j+=1
                k+=1

            while i<len(lefthalf):
                nilai_uts[k]=lefthalf[i]
                i+=1
                k+=1

            while j<len(righthalf):
                nilai_uts[k] = righthalf[j]
                j+=1
                k+=1
    print("Merging", nilai_uts)
    return nilai_uts

merge(nilai_uts)
print()
for i in range(len(nilai_uts)):
    print("%s"%nilai_uts[i])