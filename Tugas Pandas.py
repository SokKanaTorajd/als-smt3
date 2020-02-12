import pandas as pd

nama_data = []
nim_data = []
jurusan_data = []
usia_data = []
data_mahasiswa = {"Nama": nama_data, "NIM": nim_data,
                "Jurusan": jurusan_data, "Usia": usia_data}

"""fungsi inputan"""
def input_data_mhs():
    nama = input("\n masukkan nama mahasiswa: ")
    nim = input("masukkan nim: ")
    jurusan = input("masukkan jurusan: ")
    usia = input("masukkan usia: ")

    nama_data.append(nama)
    nim_data.append(nim)
    jurusan_data.append(jurusan)
    usia_data.append(usia)

    return nama,nim,jurusan,usia

if __name__ == "__main__":

    """memasukkan jumlah data berdasarkan inputan"""
    x = int(input("masukkan jumlah mahasiswa: "))
    for i in range(x):
        input_data_mhs()

    """merubah dataset ke Data Frame, lalu di export menjadi file csv"""
    dfm = pd.DataFrame(data_mahasiswa)
    print(dfm)
    print()
    dfm.to_csv('data-mahasiswa.csv')

    """menyeleksi data yang jurusannya sistem informasi, lalu di export menjadi file csv baru"""
    new_dfm = dfm[dfm.Jurusan=="sistem informasi"]
    print(new_dfm)
    new_dfm.to_csv('data-mhs-sistem-informasi.csv')