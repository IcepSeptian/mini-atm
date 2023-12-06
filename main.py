
# Program untuk membuat akun dan login dengan username, password, dan saldo awal
import datetime
import json
file_database = './database.json'

database = {}
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def simpan_database():
    # Simpan dictionary ke dalam file
    with open(file_database, 'w') as file:
        json.dump(database, file, indent=4)

def baca_database():
        # Baca dictionary dari file
        with open(file_database, 'r') as file:
            return json.load(file)

def ceksaldo(username):
    print(10*'=' + ' CEK SALDO ' +10*'='+'\n\n')

    print(f'sisa saldo anda sebesar :', {database[username]['saldo']})

    jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    while jawab != "y":
        print("input salah")
        jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    menu(username)

def tarik_tunai(username):
    global database
            
# periksa apakah username dan pw sesuai dengan yang di database
    database = baca_database()
    print('Silahkan Masukan/Pilih Nominal ')
    print('1. Rp. 100.000')
    print('2. Rp. 500.000')
    print('3. Rp. 1.000.000')
    print('4. Masukan Nominal ')
    print('5. Exit')
    tarik_tunai = int(input('Pilih Opsi Untuk Tarik Tunai:  '))
    if tarik_tunai == 1 :
        nominal = 100000
        database[username]['saldo'] -= 100000
        print(f'Saldo Anda Saat Ini Sebesar  Rp.', {database[username]['saldo']})
    elif tarik_tunai == 2 :
        nominal = 500000
        database[username]['saldo'] -= 500000
        print(f'Saldo Anda Saat Ini Sebesar  Rp..', {database[username]['saldo']})
    elif tarik_tunai == 3 :
        nominal = 1000000
        database[username]['saldo'] -= 1000000
        print(f'Saldo Anda Saat Ini Sebesar  Rp..', {database[username]['saldo']})
    elif tarik_tunai == 4 :
        tarik_tunai = int(input('Masukan Nominal  : Rp.'))
        nominal = tarik_tunai
        database[username]['saldo'] -= tarik_tunai
        print(f'Tarik Tunai Berhasil Sisa Saldo Anda Saat Ini Sebesar  Rp..', {database[username]['saldo']})
    elif tarik_tunai == 5 :
        menu(username)  
    else :
        print("input error,silahkan pilih opsi 1/2/3/4")

    tipe = "Tarik saldo"
    jumlah = -nominal
    
    simpan_transaksi(username, now, tipe, jumlah)

    simpan_database()

    jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    while jawab != "y":
        print("input salah")
        jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    menu(username)

def setor_tabungan(username):
    saldo = database[username]['saldo']
    print(f'Saldo Anda Saat Ini Sebesar Rp. {saldo}')
    print('Pilih Nominal Yang Ingin Anda Tambahkan')
    print('1. Rp. 50.000')
    print('2. Rp. 100.000')
    print('3. Rp. 150.000')
    print('4. Rp. 200.000')
    print('5. Nominal Lain')
    setor_tabungan = int(input('Pilih Nominal Yang Anda Inginkan'))
    if setor_tabungan == 1 :
        nominal = 50000
        saldo = saldo + 50000
        print(f'Saldo Anda Saat Ini Sebesar  Rp.{saldo}')
    elif setor_tabungan == 2 :
        nominal = 100000
        saldo = saldo + 100000
        print(f'Saldo Anda Saat Ini Sebesar  Rp.{saldo}')
    elif setor_tabungan == 3 :
        nominal = 150000
        saldo = saldo + 150000
        print(f'Saldo Anda Saat Ini Sebesar  Rp.{saldo}')
    elif setor_tabungan == 4 :
        nominal = 200000
        saldo = saldo + 200000
        print(f'Saldo Anda Saat Ini Sebesar  Rp.{saldo}')
    elif setor_tabungan == 5 :
        setor_tabungan = int(input('Masukan Nominal Yang Akan Anda Tambahkan : Rp.'))
        nominal = setor_tabungan
        saldo = saldo + setor_tabungan
        print(f'Saldo Anda Saat Ini Sebesar  Rp.{saldo}')
    
    database[username]['saldo'] = saldo

    tipe = "Setor saldo"
    jumlah = nominal
    
    simpan_transaksi(username, now, tipe, jumlah)

    simpan_database()

    jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    while jawab != "y":
        print("input salah")
        jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    menu(username)

def transfer_saldo(dari_username):

    baca_database()
    
    ke_username =  input("Masukkan username tujuan: ")
    while ke_username not in database:
        print("Username tujuan tidak ada.")
        ke_username =  input("Masukkan username tujuan: ")
        
    nominal = int(input("Masukkan nominal: "))
    saldo_akun = database[dari_username]['saldo']
    if saldo_akun < nominal:
        print("Saldo anda tidak mencukupi.")
        nominal = int(input("Masukkan nominal: "))
    
    saldo_tujuan = database[ke_username]['saldo']
    database[dari_username]['saldo'] -= nominal
    database[ke_username]['saldo'] += nominal
    
    tipe = "transfer"
    jumlah = -nominal
    
    simpan_transaksi(dari_username, now, tipe, jumlah)
    
    simpan_database()  
    print("Transfer sukses!")
    print("Sisa saldo anda Rp.", database[dari_username]['saldo'])
    
    jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    while jawab != "y":
        print("input salah")
        jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    menu(dari_username)
    
def simpan_transaksi(username, now, tipe, jumlah):
    database[username]['riwayat_transaksi'] = {'tanggal': now, 'tipe': tipe, 'nominal': jumlah}
    simpan_database()
    
def riwayat_transaksi(username):
    print(database[username]['riwayat_transaksi']['tanggal'])
    print("Jenis transaksi:", database[username]['riwayat_transaksi']['tipe'])
    print("Nominal:", database[username]['riwayat_transaksi']['nominal'])
    jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    while jawab != "y":
        print("input salah")
        jawab = str(input("Ketik (y) untuk kembali ke menu. "))
    menu(username)
    
def create_account():
    global database
    print("Selamat datang! Silakan buat akun baru.")
    username = input("Masukkan username: ")

    # apakah username sudah ada di database
    while username in database:
        print("Maaf, username sudah digunakan. Silakan pilih username lain.")
        username = input("Masukkan username: ")

    password = input("Masukkan password: ")
    konfirmasi_password = input("Konfirmasi password: ")

    # mencocokkan pw dan konfirmasi pw
    while password != konfirmasi_password:
        print("Password tidak cocok. Silakan coba lagi.")
        password = input("Masukkan password: ")
        konfirmasi_password = input("Konfirmasi password: ")

    # menginput informasi pw dan saldo awal ke database sesuai username
    database[username] = {'password': password, 'saldo': 10000}
    print("Akun berhasil dibuat. Saldo awal: 10000. Silakan login.")
    simpan_database()

def login():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print("Silakan login.")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # periksa apakah username dan pw sesuai dengan yang di database
        if username in database and database[username]['password'] == password:
            print("Login berhasil!") 
            menu(username)
            break
        else:
            attempts += 1
            print("Login gagal. Kesempatan tersisa:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Anda telah melebihi batas percobaan login. proses dibatalkan.")
       
def menu(username):
    global database
    print("Selamat datang, " + username)
    database = baca_database()
    print("1. Cek saldo")
    print("2. Setor saldo")
    print("3. Tarik saldo")
    print("4. Transfer saldo")
    print("5. Riwayat transaksi")
    print("6. Keluar")
    choice = input("Ketik (1/2/3/4/5/6) ")
    if choice == "1" :
        ceksaldo(username)
    if choice == "2" :
        setor_tabungan(username)
    if choice == "3" :
        tarik_tunai(username)
    if choice == "4" :
        from_username = username
        transfer_saldo(from_username)
    if choice == "5" :
        riwayat_transaksi(username)
    if choice == "6" :
        jwb = str(input("Anda yakin ingin keluar? (y/t) "))
        while jwb != "y" and jwb != "t" :
            print("input salah")
            jwb = str(input("Anda yakin ingin keluar? (y/t) "))
        if jwb == "y" :
            main()
        if jwb == "t" :
            menu(username)
            
def new_account():
    global database
    jumlah_akun = int(input("Berapa banyak akun yang ingin Anda buat? "))

    for _ in range(jumlah_akun):
        create_account()
    main()

import sys
def exit():
    sys.exit()

def main():
    global database
    database = baca_database()
    print("Selamat datang di mini ATM, Silahkan pilih login atau buat akun baru.")
    print("1. Login")
    print("2. Buat akun baru")
    print("3. keluar")
    choice = input("(ketik 1/2/3) ")
    if choice == "1" :
        login()
    elif choice == "2" :
        new_account()
    elif choice == "3" :
        exit()
    else :
        print("input error, silahkan pilih opsi 1/2/3 ")
        main()

main()
