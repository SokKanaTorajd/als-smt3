def konversi(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = " "
    if x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += konversi(x-10) + "belas"
    elif x < 100:
        hasil += konversi(int(x/10)) + " puluh" + konversi(x%10)
    elif x < 200 :
        hasil += "seratus" + konversi(x-100)
    elif x < 1000 :
        hasil += konversi(int(x/100)) + " ratus" + konversi(x%100)
    elif x < 2000 :
        hasil += "seribu" + konversi(x-1000)
    elif x < 1000000 :
        hasil += konversi(int(x/1000)) + "ribu" + konversi(x%1000)
    elif x < 1000000000 :
        hasil += konversi(int(x/1000000)) + " juta" + konversi(x%1000000)
    elif x >= 1000000000 :
        hasil += konversi(int(x/1000000000)) + " milyar" + konversi(x%1000000000)

    return hasil

print(konversi(1995))
