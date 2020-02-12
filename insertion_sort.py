"""Taufaldisatya W.D/182103010/Sistem Informasi"""

nilai_uts = [
    {"nama" : "Siti Azizah","nilai" : 85},
    {"nama" : "Siti Aminah","nilai" : 95},
    {"nama" : "Siti Fatimah","nilai" : 75},
    {"nama" : "Siti Maimunah","nilai" : 70},
    {"nama" : "Siti Komariah","nilai" : 90},
]

def insertionsort(nilai_uts):
    for i in range(len(nilai_uts)):
        nilai = nilai_uts[i]["nilai"]
        nama = nilai_uts[i]["nama"]
        j = i
        while j > 0 and nilai < nilai_uts[j-1]["nilai"]:
            nilai_uts[j]["nilai"] = nilai_uts[j-1]["nilai"]
            nilai_uts[j]["nama"] = nilai_uts[j-1]["nama"]
            j-=1
        nilai_uts[j]["nilai"] = nilai
        nilai_uts[j]["nama"] = nama
    return nilai_uts

nilai_uts = insertionsort(nilai_uts)

for i in range(len(nilai_uts)):
    print("%s"%nilai_uts[i])
