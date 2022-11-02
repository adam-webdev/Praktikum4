# menerima input yang diketik dan menyimpannya didalam variable
bilanganSatu = input("Masukan bilangan Pertama : ")
bilanganKedua = input("Masukan bilangan Kedua : ")

# mengkonversi input string ke integer karena method input() selalu mengembalikan type data string
bilanganSatu = int(bilanganSatu)
bilanganKedua = int(bilanganKedua)

# mengecek untuk menentukan bilangan terbesar dari kedua bilangan
if bilanganSatu > bilanganKedua:
    print("Bilangan ", bilanganSatu, "lebih besar dari bilangan", bilanganKedua)
else:
    print("Bilangan ", bilanganKedua, "lebih besar dari bilangan", bilanganSatu)
