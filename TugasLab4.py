from prettytable import PrettyTable



tabelMahasiswa = PrettyTable()

tabelMahasiswa.field_names = ['URUTAN', 'NAMA', 'TUGAS', 'UTS', 'UAS']

fitur = [
    {
        '1': 'TAMBAH DATA',
        '2': 'LIHAT DATA',
        '3': 'HAPUS DATA',
        '4': 'UBAH DATA\n',
        '0': 'keluar\n'
    }
]


urutan = 0
dataMahasiswa = []

def TambahData():
    global urutan
    
    urutan += 1
    name = str(input('Masukan Nama Mahasiswa :'))
    tugas = input('Masukan Nilai Tugas :')
    uts = input('Masukan Nilai UTS :')
    uas = input('Masukan Nilai UAS :')
    
    dataMahasiswa.append(
                {
                    'URUTAN':urutan,
                    'NAMA': name,
                    'TUGAS': tugas,
                    'UTS': uts,
                    'UAS': uas
                }
                )
    
    tabelMahasiswa.add_row(
        [
            urutan, name, tugas, uas, uts
        ]
    )
    #HAPUS DATA
def HapusData():
    print(tabelMahasiswa)
    urutan = input('\t[-] Urutan Yang Akan DiHapus?')
    tanya = input('Yakin Ingin Menghapus Data ? [Y / N] :')
    if tanya =='Y' or tanya =='y':
        tabelMahasiswa.del_row(int(urutan))
        print('\t[-] Data Berhasil DiHapus')
    elif tanya =='N' or tanya == 'n':
        main()
    else:
        print('\t[*] KEYWOARD TIDAK TESEDIA!')
    
    
    # LIHAT DATA
def LihatData():
    print(tabelMahasiswa)
    
def UbahData():
    print(tabelMahasiswa)
    urutan = input('\t[-] Urutan Yang Akan DiUbah?')
    tanya = input('Yakin Ingin Mengubah Data ? [Y / N] :')
    if tanya =='Y' or tanya =='y':
        tabelMahasiswa.del_row(int(urutan))
        print('\t[*] Data Berhasil DiHapus')
    elif tanya =='N' or tanya == 'n':
        main()
    else:
        print('\t[*] KEYWOARD TIDAK TESEDIA!')
        

    
def main():
    print('\t[*] Fitur Yang Tersedia')
    for key, value in fitur[0].items():
        print(f"\t{key}. {value.title()}")
    print()
    pilih_fitur = input('\t[*] Pilih Fitur: ')
    # PERULANGAN
    while pilih_fitur != '0':
        if pilih_fitur == '0':
            break
        elif pilih_fitur == '1':
            TambahData()
        elif pilih_fitur == '2':
            LihatData()
        elif pilih_fitur == '3':
            HapusData()
        elif pilih_fitur == '4':
            UbahData()
        else:
            print('[*] Fitur Tidak Tersedia')
        print()
        pilih_fitur = input("\t[*] Pilih Fitur: ")
        
    else:
        print('\t [*] PROGRAM SELESAI!')
            
    
main()