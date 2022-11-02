
# melakukan perulangan dari 0 sampai 10
for i in range(0, 10):
  # menampilkan variable i , (" " * 3) Artinya menambahkan spasi tiga kali lalu end => yaitu memulai baris baru setelah nilai terakhir
    print(i, " " * 3,  end='')

    # melakukan perulangan dari 1 sampai 10
    for j in range(1, 10):
        # menampilkan output j + i , (" " * 3) Artinya menambahkan spasi tiga kali lalu end => yaitu memulai baris baru setelah nilai terakhir
        print(j+i, " " * 3, end='')
    print()
