
# Program untuk membuat akun dan login dengan username, password, dan saldo awal

import json
file_database = './database.json'

database = {}

def simpan_database():
    # Simpan dictionary ke dalam file
    with open(file_database, 'w') as file:
        json.dump(database, file)

def baca_database():
        # Baca dictionary dari file
        with open(file_database, 'r') as file:
            return json.load(file)

def transfer(from_username):
    # Load the account data from the database.json file
    with open('database.json', 'r') as file:
        akun = json.load(file)

    global database
    to_username =  input("Masukkan username tujuan: ")
    nominal = int(input("Masukkan nominal: "))
    if from_username not in database:
        print("Error: Username tujuan tidak ada.")
        return
    
    saldo_akun = database[from_username]['saldo']
    if saldo_akun < nominal:
        print("Error: Saldo anda tidak mencukupi.")
        return
    
    saldo_tujuan = database[to_username]['saldo']
    database[from_username]['saldo'] -= nominal
    database[to_username]['saldo'] += nominal
    
    # Update the database with the new account balances
    with open('database.json', 'w') as file:
        json.dump(database, file, indent=4)
    
    print("Transfer sukses!")

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
    global database
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print("Silakan login.")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # periksa apakah username dan pw sesuai dengan yang di database
        if username in database and database[username]['password'] == password:
            print("Login berhasil! Selamat datang, " + username + ". Saldo Anda: " + str(database[username]['saldo']))
            break
        else:
            attempts += 1
            print("Login gagal. Kesempatan tersisa:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Anda telah melebihi batas percobaan login. proses dibatalkan.")
    
    database = baca_database()
    print("1. Transfer")
    print("2. Buat akun baru")
    print("3. keluar")
    choice = input("(ketik 1/2/3)")
    if choice == "1" :
       from_username = username
       transfer(from_username)

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
    choice = input("(ketik 1/2/3)")
    if choice == "1" :
        login()
    elif choice == "2" :
        new_account()
    elif choice == "3" :
        exit()
    else :
        print("input error, silahkan pilih opsi 1/2/3")
        main()

main()
