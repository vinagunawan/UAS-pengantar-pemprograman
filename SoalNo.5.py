import mysql.connector
import os
from prettytable import PrettyTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="tabel mahasiswa"
)


def tambah():
    cursor = db.cursor()
    os.system('cls')
    Nama = input('Masukkan Nama: ')
    NIM = input('Masukkan Nim: ')
    if len(NIM) != 8:
        print('nim salah')
        tambah()
        quit()
    Program_studi = input('Masukkan Program Studi: ')

    sql = "insert into DataMahasiswa (Nama,NIM,Program_studi) values(%s,%s,%s)"
    val = (Nama, NIM, Program_studi)
    cursor.execute(sql, val)
    db.commit()
    print("Data ditambahkan")


def ubah():
    cursor = db.cursor()
    update = input('Pilih data mahasiswa yang akan diubah (berdasarkan id): ')
    os.system('cls')
    Nama = input('Masukkan Nama baru: ')
    NIM = input('Masukkan Nim baru (6 digit tanpa titik): ')
    if len(NIM) != 8:
        print('nim salah')
        tambah()
        quit()
    Program_studi = input('Masukkan Program Studi baru: ')

    sql = "UPDATE data SET Nama=%s,NIM=%s,Program_studi=%s WHERE id=%s"
    val = (Nama, NIM, Program_studi, update)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil diubah")


def hapus():
    cursor = db.cursor()
    delete = input('Masukkan ID Mahasiswa yang akan dihapus: ')
    sql = "DELETE FROM data WHERE id=%s" % delete
    cursor.execute(sql)
    db.commit()
    print('Data berhasil dihapus')


def menu():
    cursor = db.cursor()
    sql = "SELECT * FROM DataMahasiswa"
    cursor.execute(sql)
    hasil = cursor.fetchall()
    t = PrettyTable(['id', 'Nama', 'NIM', 'Program_studi'])
    os.system('cls')
    for row in hasil:
        t.add_row(row)
    print(t)

    print('DAFTAR PERINTAH')
    print('1.Tambah Data')
    print('2.Ubah Data')
    print('3.Hapus Data')
    print('Ketik exit jika ingin keluar')
    menu = input('Pilih Menu(1/2/3/exit): ')

    if menu == '1':
        tambah()
    if menu == '2':
        ubah()
    if menu == '3':
        hapus()
    elif menu == 'exit':
        os.system('cls')
        quit()


if __name__ == "__main__":
    while(True):
        menu()
