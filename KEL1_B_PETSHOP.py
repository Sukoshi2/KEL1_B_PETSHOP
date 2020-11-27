import os
import time
print("LOADING.......0%")
time.sleep(4)
print("LOADING.......25%")
time.sleep(6)
print("LOADING.......75%")
time.sleep(4)
print("LOADING COMPLETE!!!")
time.sleep(1)
os.system("cls")
#Data-Data
class color:
   b = '\033[94m'
   g = '\033[92m'
   y = '\033[93m'
   r = '\033[91m'
   u = '\033[95m'
   e = '\033[0m'
   bold = '\033[1m'

username = ["Admin", "Pelanggan"]
password = ["112233", "123"]
sebagai = ["Admin", "Pelanggan"]

data_kucing = [["kucing anggora", 6, 7000000, "hewan"],
              ["kucing sphinx", 4, 1800000, "hewan"],
              ["kucing rusia b", 3, 23800000, "hewan"],
              ["kucing pbald", 2, 35000000, "hewan"],
              ["kucing persia", 4, 42000000, "hewan"],
              ["kucing savannah", 2, 350000000,"hewan"],
              ["kucing bengal", 5, 5000000, "hewan"]]


data_anjing = [["anjing lowchen", 2, 113000000, "hewan"],
              ["anjing irish", 4, 28000000, "hewan"],
              ["anjing pharaoh", 3, 71000000, "hewan"],
              ["anjing rott", 5, 57000000, "hewan"],
              ["anjing akita", 1, 64000000, "hewan"],
              ["anjing samoyed", 2, 143000000, "hewan"]]

data_makanan_h = [["makanan kucing", 100, 150000, "makanan hewan"],
                 ["makanan anjing", 200, 160000, "makanan hewan"]]

data_keperluan_h = [["kandang hewan UK kecil", 10, 500000,"keperluan hewan"],
                   ["kandang hewan UK besar", 7, 1500000, "keperluan hewan"]]

stock_baru = []

def data_baru():
    nama_stock = input(color.g + "Masukan nama stock baru :")
    jumlah_stock = int(input("Masukan jumlah stock baru :"))
    harga_stock = int(input("tentukan harga stock baru :"))
    jenis_stock = input("masukan jenis stock baru :" + color.e)
    stock_baru.append([nama_stock, jumlah_stock, harga_stock, jenis_stock])
    return stock_baru

#Menu Admin
def menu_admin():
    batas_input = 10
    while True:
        print(color.b + "||===========================================||")
        print("||               MENU ADMIN                  ||")
        print("||===========================================||")       
        print("||    1. Tambahkan stock                     ||")
        print("||    2. masukan stock baru                  ||")
        print("||    3. Lihat stock                         ||")
        print("||    4. Perbarui jumlah stock               ||")
        print("||    5. Hapus stock                         ||")
        print("||    6. Logout                              ||")
        print("||===========================================||" + color.e)
              
        pilihan1 = input(color.g + "Masukkan pilihan : " + color.e)
        
        if (pilihan1 == "1" or pilihan1 == "tambahkan stock" or pilihan1 == "Tambahkan stock"):
            if (batas_input > 0):
                NS_tam  = input(color. u + "Nama : ")
                JuS_tam = int(input("Jumlah : "))
                HS_tam = int(input("Harga : "))
                JeS_tam = input("Jenis : " + color.e)
                print(color.b + "||===========================================||")
                print("||    1. Kucing                              ||")
                print("||    2. Anjing                              ||")
                print("||    3. Makanan hewan                       ||")
                print("||    4. Keperluan hewan                     ||")
                print("||    5. Stock baru                          ||")
                print("||===========================================||" + color.e)
                data_toko_b = input(color.g + "masukan data yang ingin diperbarui atau di tambahkan :" + color.e)
                
                if (data_toko_b == "kucing" or data_toko_b == "Kucing" or data_toko_b == "1"):
                  data_kucing.append([NS_tam, JuS_tam, HS_tam, JeS_tam])
                  data_kucing.sort()
                  print(color.y + "data kucing berhasil diperbarui" + color.e)
                        
                elif (data_toko_b == "anjing" or data_toko_b == "Anjing" or data_toko_b == "2"):
                  data_anjing.append([NS_tam, JuS_tam, HS_tam, JeS_tam])
                  data_anjing.sort()
                  print(color.y + "data anjing berhasil diperbarui" + color.e)
                        
                elif (data_toko_b == "makanan hewan" or data_toko_b == "Makanan hewan" or data_toko_b == "3"):
                  data_makanan_h.append([NS_tam, JuS_tam, HS_tam, JeS_tam])
                  data_makanan_h.sort()
                  print(color.y + "data makanan hewan berhasil diperbarui" + color.e)
                        
                elif (data_toko_b == "keperluan hewan" or data_toko_b == "Keperluan hewan" or data_toko_b == "4"):
                  data_keperluan_h.append([NS_tam, JuS_tam, HS_tam, JeS_tam])
                  data_keperluan_h.sort()
                  print(color.y + "data keperluan hewan berhasil diperbarui" + color.e)
                        
                elif (data_toko_b == "stock baru" or data_toko_b == "Stock baru" or data_toko_b == "5"):
                  stock_baru.append([NS_tam, JuS_tam, HS_tam, JeS_tam])
                  stock_baru.sort()
                  print(color.y + "data stock baru berhasil diperbarui" + color.e)
                        
                else:
                  print(color.r + "saat ini hanya data diatas yang tersedia" + color.e)

                batas_input -= 1
                print(color.y + "berhasil menambahkan!")
                print("||========= Kembali ke menu Admin ===========||")
                print("||===========================================||" + color.e)
            else:
                print(color.r + "Maaf batas input hanya itu" + color.e)
            time.sleep(3)
            os.system("cls")
            print(color.y + "||========= Kembali ke menu Admin ===========||")
            print("||===========================================||" + color.e)

        elif (pilihan1 == "2" or pilihan1 == "masukan stock baru" or pilihan1 == "Masukan stock baru"):
            a = data_baru()
            print(a)
            print(color.y + "||===== stock baru berhasil di masukkan =====||" + color.e)
            time.sleep(3)
            os.system("cls")
            print(color.y + "||===========================================||")  
            print("||          Kembali ke menu Admin            ||")
            print("||===========================================||" + color.e)
            
        elif (pilihan1 == "3" or pilihan1 == "lihat stock" or pilihan1 == "Lihat stock"):
            print(color.b + "||===========================================||")
            print("||    1. Kucing                              ||")
            print("||    2. Anjing                              ||")
            print("||    3. Makanan hewan                       ||")
            print("||    4. Keperluan hewan                     ||")
            print("||    5. Stock baru                          ||")
            print("||===========================================||" + color.e)
            lihat_data = input(color.g + "masukan data yang ingin di lihat :" + color.e)
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            if (lihat_data == "kucing" or lihat_data == "Kucing" or lihat_data == "1"):
              for i in range(len(data_kucing)):
                for j in range(len(data_kucing[i])):
                    print(data_kucing[i][j], end = "\t\t\t ")
                print()
            elif (lihat_data == "anjing" or lihat_data == "Anjing" or lihat_data == "2"):
              for i in range(len(data_anjing)):
                for j in range(len(data_anjing[i])):
                    print(data_anjing[i][j], end = "\t\t\t ")
                print()
            elif (lihat_data == "makanan hewan" or lihat_data == "Makanan hewan" or lihat_data == "3"):
              for i in range(len(data_makanan_h)):
                for j in range(len(data_makanan_h[i])):
                    print(data_makanan_h[i][j], end = "\t\t\t ")
                print()
            elif (lihat_data == "keperluan hewan" or lihat_data == "Keperluan hewan" or lihat_data == "4"):
              for i in range(len(data_keperluan_h)):
                for j in range(len(data_keperluan_h[i])):
                    print(data_keperluan_h[i][j], end = "\t\t\t ")
                print()
            elif (lihat_data == "stock baru" or lihat_data == "Stock baru" or lihat_data == "5"):
              for i in range(len(stock_baru)):
                for j in range(len(stock_baru[i])):
                    print(stock_baru[i][j], end = "\t\t\t ")
                print()
            else:
                print(color.r + "saat ini hanya data diatas yang tersedia!" + color.e)
            time.sleep(10)
            os.system("cls")
            print(color.e + color.y + "||===========================================||")
            print("||          Kembali ke menu Admin            ||")
            print("||===========================================||" + color.e)
        elif (pilihan1 == "4" or pilihan1 == "Perbarui jumlah stock" or pilihan1 == "perbarui jumlah stock"):
            print(color.b + "||===========================================||")
            print("||    1. Kucing                              ||")
            print("||    2. Anjing                              ||")
            print("||    3. Makanan hewan                       ||")
            print("||    4. Keperluan hewan                     ||")
            print("||    5. Stock baru                          ||")
            print("||===========================================||" + color.e)
            tambah_jumlah = input(color.g + "masukan data yang ingin di tambah jumlah stocknya :" + color.e)
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            if (tambah_jumlah == "kucing" or tambah_jumlah == "Kucing" or tambah_jumlah == "1"):
              for i in range(len(data_kucing)):
                for j in range(len(data_kucing[i])):
                    print(data_kucing[i][j], end = "\t\t\t ")
                print()
              cek_barang1 = len(data_kucing) - 1
              N_barang1 = input(color.e + color.g + "Masukkan jenis kucing: ")
              while (cek_barang1 >= 0):
                  if (N_barang1 == data_kucing[cek_barang1][0]):
                    break
                  else:
                    cek_barang1 -= 1
              if (cek_barang1 >= 0):
                 PJ_barang = int(input("Masukkan jumlah kucing: " + color.e))
                 data_kucing[cek_barang1][1] = PJ_barang
                 print(color.y + "data jumlah kucing berhasil di perbarui" + color.e)
              else:
                  print(color.r + "Maaf nama kucing yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah == "anjing" or tambah_jumlah == "Anjing" or tambah_jumlah == "2"):
              for i in range(len(data_anjing)):
                for j in range(len(data_anjing[i])):
                    print(data_anjing[i][j], end = "\t\t\t ")
                print()
              cek_barang1 = len(data_anjing) - 1
              N_barang1 = input(color.e + color.g + "Masukkan jenis anjing: ")
              while (cek_barang1 >= 0):
                  if (N_barang1 == data_anjing[cek_barang1][0]):
                    break
                  else:
                    cek_barang1 -= 1
              if (cek_barang1 >= 0):
                 PJ_barang = int(input("Masukkan jumlah anjing: " + color.e))
                 data_anjing[cek_barang1][1] = PJ_barang
                 print(color.y + "data jumlah anjing berhasil di perbarui" + color.e)
              else:
                  print(color.r + "Maaf jenis anjing yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah == "makanan hewan" or tambah_jumlah == "Makanan hewan" or tambah_jumlah == "3"):
              for i in range(len(data_makanan_h)):
                for j in range(len(data_makanan_h[i])):
                    print(data_makanan_h[i][j], end = "\t\t\t ")
                print()
              cek_barang1 = len(data_makanan_h) - 1
              N_barang1 = input(color.e + color.g + "Masukkan nama makanan hewan: ")
              while (cek_barang1 >= 0):
                  if (N_barang1 == data_makanan_h[cek_barang1][0]):
                    break
                  else:
                    cek_barang1 -= 1
              if (cek_barang1 >= 0):
                 PJ_barang = int(input("Masukkan jumlah makanan: " + color.e))
                 data_makanan_h[cek_barang1][1] = PJ_barang
                 print(color.y + "data jumlah makanan hewan berhasil di perbarui" + color.e)
              else:
                  print(color.r + "Maaf makanan hewan yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah == "keperluan hewan" or tambah_jumlah == "Keperluan hewan" or tambah_jumlah == "4"):
              for i in range(len(data_keperluan_h)):
                for j in range(len(data_keperluan_h[i])):
                    print(data_keperluan_h[i][j], end = "\t\t\t ")
                print()
              cek_barang1 = len(data_keperluan_h) - 1
              N_barang1 = input(color.e + color.g + "Masukkan jenis keperluan hewan: ")
              while (cek_barang1 >= 0):
                  if (N_barang1 == data_keperluan_h[cek_barang1][0]):
                    break
                  else:
                    cek_barang1 -= 1
              if (cek_barang1 >= 0):
                 PJ_barang = int(input("Masukkan jumlah keperluan hewan: " + color.e))
                 data_keperluan_h[cek_barang1][1] = PJ_barang
                 print(color.y + "data jumlah keperluan hewan berhasil di perbarui" + color.e)
              else:
                  print(color.r + "Maaf keperluan hewan yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah == "stock baru" or tambah_jumlah == "Stock baru" or tambah_jumlah == "5"):
              for i in range(len(stock_baru)):
                for j in range(len(stock_baru[i])):
                    print(stock_baru[i][j], end = "\t\t\t ")
                print()
              cek_barang1 = len(stock_baru) - 1
              N_barang1 = input(color.e + color.g + "Masukkan nama stock baru: ")
              while (cek_barang1 >= 0):
                  if (N_barang1 == stock_baru[cek_barang1][0]):
                    break
                  else:
                    cek_barang1 -= 1
              if (cek_barang1 >= 0):
                 PJ_barang = int(input("Masukkan jumlah stock baru: " + color.e))
                 stock_baru[cek_barang1][1] = PJ_barang
                 print(color.y + "data jumlah stock berhasil di perbarui" + color.e)
              else:
                  print(color.r + "Maaf stock baru yang dimasukkan tidak ada" + color.e)
            else:
                print(color.r + "data salah!" + color.e)
            time.sleep(3)
            os.system("cls")
            print(color.e + color.y + "||===========================================||")
            print("||          Kembali ke menu Admin            ||")
            print("||===========================================||" + color.e)
        elif (pilihan1 == "5" or pilihan1 == "Hapus stock" or pilihan1 == "hapus stock"):
          print(color.b + "||===========================================||")
          print("||  Silahkan pilih data yang ingin di hapus  ||")
          print("||===========================================||")
          print("||    1. Kucing                              ||")
          print("||    2. Anjing                              ||")
          print("||    3. Makanan hewan                       ||")
          print("||    4. Keperluan hewan                     ||")
          print("||    5. Stock baru                          ||")
          print("||===========================================||" + color.e)
          hapus_data = input(color.g + "masukan nama data yang ingin di hapus :" + color.e)
          if (hapus_data == "kucing" or hapus_data == "1" or hapus_data == "Kucing"):
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_kucing)):
                for j in range(len(data_kucing[i])):
                    print(data_kucing[i][j], end = "\t\t\t ")
                print()
            a1 = 3
            cek_barang2 = len(data_kucing) - 1
            N_barang2 = input(color.e + color.g + "Masukkan salah satu nama kucing yang ingin di hapus: " + color.e)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_kucing[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                  while a1 >= 0:
                    data_kucing[cek_barang2].pop(a1)
                    a1 -= 1
                  data_kucing.sort()
                  del data_kucing[0]
                  print(color.y + "berhasil menghapus kucing" + color.e)
            else:
                 print(color.r + "Maaf nama kucing yang anda masukkan tidak ada" + color.e)
          elif (hapus_data == "anjing" or hapus_data == "Anjing" or hapus_data == "2"):
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_anjing)):
                for j in range(len(data_anjing[i])):
                    print(data_anjing[i][j], end = "\t\t\t ")
                print()
            a1 = 3
            cek_barang2 = len(data_anjing) - 1
            N_barang2 = input(color.e + color.g + "Masukkan salah satu nama anjing yang ingin di hapus: " + color.e)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_anjing[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                  while a1 >= 0:
                    data_anjing[cek_barang2].pop(a1)
                    a1 -= 1
                  data_anjing.sort()
                  del data_anjing[0]
                  print(color.y + "berhasil menghapus anjing" + color.e)
            else:
                 print(color.r + "Maaf nama anjing yang anda masukkan tidak ada" + color.e)
          elif (hapus_data == "makanan hewan" or hapus_data == "Makanan hewan" or hapus_data == "3"):
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_makanan_h)):
                for j in range(len(data_makanan_h[i])):
                    print(data_makanan_h[i][j], end = "\t\t\t ")
                print()
            a1 = 3
            cek_barang2 = len(data_makanan_h) - 1
            N_barang2 = input(color.e + color.g + "Masukkan salah satu makanan hewan apa yang ingin di hapus: " + color.e)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_makanan_h[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                  while a1 >= 0:
                    data_makanan_h[cek_barang2].pop(a1)
                    a1 -= 1
                  data_makanan_h.sort()
                  del data_makanan_h[0]
                  print(color.y + "berhasil menghapus makanan hewan" + color.e)
            else:
                 print(color.r + "Maaf makananan hewan yang anda masukkan tidak ada" + color.e)
          elif (hapus_data == "keperluan hewan" or hapus_data == "Keperluan hewan" or hapus_data == "4"):
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_keperluan_h)):
                for j in range(len(data_keperluan_h[i])):
                    print(data_keperluan_h[i][j], end = "\t\t\t ")
                print()
            a1 = 3
            cek_barang2 = len(data_keperluan_h) - 1
            N_barang2 = input(color.e + color.g + "Masukkan salah satu keperluan hewan yang ingin dihapus: " + color.e)
            while (cek_barang2 >= 0):
                if (N_barang2 == data_keperluan_h[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                  while a1 >= 0:
                    data_keperluan_h[cek_barang2].pop(a1)
                    a1 -= 1
                  data_keperluan_h.sort()
                  del data_keperluan_h[0]
                  print(color.y + "berhasil menghapus barang keperluan hewan" + color.e)
            else:
                 print(color.r + "Maaf barang keperluan hewan yang anda masukkan tidak ada" + color.e)
          elif (hapus_data == "stock baru" or hapus_data == "Stock baru" or hapus_data == "5"):
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(stock_baru)):
                for j in range(len(stock_baru[i])):
                    print(stock_baru[i][j], end = "\t\t\t ")
                print()
            a1 = 3
            cek_barang2 = len(stock_baru) - 1
            N_barang2 = input(color.e + color.g + "Masukkan nama salah satu stock baru yang ingin dihapus: " + color.e)
            while (cek_barang2 >= 0):
                if (N_barang2 == stock_baru[cek_barang2][0]):
                    break
                else:
                    cek_barang2 -= 1
            if (cek_barang2 >= 0):
                  while a1 >= 0:
                    stock_baru[cek_barang2].pop(a1)
                    a1 -= 1
                  stock_baru.sort()
                  del stock_baru[0]
                  print(color.y + "berhasil menghapus stock baru" + color.e)
            else:
                 print(color.r + "Maaf stock baru yang anda masukkan tidak ada" + color.e)
          else:
              print(color.r + "saat ini hanya ada data yang diatas" + color.e)
          time.sleep(3)
          os.system("cls")
          print(color.e + color.y + "||===========================================||")
          print("||          Kembali ke menu Admin            ||")
          print("||===========================================||" + color.e)
        elif (pilihan1 == "6" or pilihan1 == "logout" or pilihan1 == "Logout"):
            print(color.y + "||===========================================||")
            print("||          telah berhasil logout!!          ||")
            print("||===========================================||" + color.e)
            break
        else:
            print(color.r + "Maaf, menu yang anda pilih tidak tersedia" + color.e)
        time.sleep(3)
        os.system("cls")
            
            


#Menu Pelanggan
def menu_pelanggan():
    while True:
        print(color.b + "||===========================================||")
        print("||               MENU PELANGGAN              ||")
        print("||===========================================||")       
        print("||    1. Beli Stock                          ||")
        print("||    2. Logout                              ||")
        print("||===========================================||" + color.e)
        pilihan2 = input(color.g + "Masukkan pilihan beli atau logout : " + color.e)
        if (pilihan2 == "1" or pilihan2 == "beli stock" or pilihan2 == "Beli stock"):
          print(color.b + "||===========================================||")
          print("||    disini tersedia hewan dan lain-lain    ||")
          print("||===========================================||")
          print("||    1. Kucing                              ||")
          print("||    2. Anjing                              ||")
          print("||    3. Makanan hewan                       ||")
          print("||    4. Keperluan hewan                     ||")
          print("||    5. Stock baru                          ||")
          print("||===========================================||" + color.e)
          yg_dijual = input(color.g + "anda mau beli apa? :" + color.e)
          if (yg_dijual == "1" or yg_dijual == "kucing" or yg_dijual == "Kucing"):
            print(color.bold + "ini adalah beberapa kucing yang dijual")
            print("Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_kucing)):
                for j in range(len(data_kucing[i])):
                    print(data_kucing[i][j], end = "\t\t\t ")
                print()
            cek_barang3 = len(data_kucing) - 1
            B_barang = input(color.e + color.g + "Masukkkan nama kucing yang mau anda beli: " + color.e)
            while (cek_barang3 >= 0):
                if (B_barang == data_kucing[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_kucing[cek_barang3][0]):
                JB_barang = int(input(color.g + "Masukkan jumlah kucing yang dibeli: " + color.e))
                if (JB_barang <= 0):
                    print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                elif (JB_barang <= data_kucing[cek_barang3][1]):
                    T_harga = JB_barang * data_kucing[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.y + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!")
                    time.sleep(1)
                    os.system("cls")
                    print("Berikut ini adalah Struk Pembayaran" + color.e)
                    time.sleep(2)
                    print(color.y + "||===========================================||")
                    print("||              PETSHOP Hada                 ||")
                    print("||            Struk Pembayaran               ||")
                    print("||Nama stock  : ", B_barang)
                    print("||Jumlah stock: ", JB_barang)
                    print("||Total harga : Rp. ", T_harga)
                    print("||===========================================||" + color.e)
                    time.sleep(5)
                    os.system("cls")
                    print(color.y + "||===========================================||")
                    print("||     Silahkan ke kasir untuk pembayaran    ||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    time.sleep(3)
                    os.system("cls")
                else:
                    print(color.r + "Maaf jumlah kucing yang tersedia tidak cukup" + color.e)
            else:
                print(color.r + "Maaf jenis kucing yang anda masukkan tidak ada" + color.e)

          elif (yg_dijual == "2" or yg_dijual == "anjing" or yg_dijual == "Anjing"):
            print(color.bold + "ini adalah beberapa anjing yang dijual")
            print("Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_anjing)):
                for j in range(len(data_anjing[i])):
                    print(data_anjing[i][j], end = "\t\t\t ")
                print()
            cek_barang3 = len(data_anjing) - 1
            B_barang = input(color.e + color.g + "Masukkkan nama anjing yang mau anda beli: " + color.e)
            while (cek_barang3 >= 0):
                if (B_barang == data_anjing[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_anjing[cek_barang3][0]):
                JB_barang = int(input(color.g + "Masukkan jumlah anjing yang dibeli: " + color.e))
                if (JB_barang <= 0):
                    print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                elif (JB_barang <= data_anjing[cek_barang3][1]):
                    T_harga = JB_barang * data_anjing[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.y + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!")
                    time.sleep(1)
                    os.system("cls")
                    print("Berikut ini adalah Struk Pembayaran" + color.e)
                    time.sleep(2)
                    print(color.y + "||===========================================||")
                    print("||              PETSHOP Hada                 ||")
                    print("||            Struk Pembayaran               ||")
                    print("||Nama stock  : ", B_barang)
                    print("||Jumlah stock: ", JB_barang)
                    print("||Total harga : Rp. ", T_harga)
                    print("||===========================================||" + color.e)
                    time.sleep(5)
                    os.system("cls")
                    print(color.y + "||===========================================||")
                    print("||     Silahkan ke kasir untuk pembayaran    ||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    time.sleep(3)
                    os.system("cls")
                else:
                    print(color.r + "Maaf jumlah anjing yang tersedia tidak cukup" + color.e)
            else:
                print(color.r + "Maaf anjing yang anda masukkan tidak ada" + color.e)

          elif (yg_dijual == "3" or yg_dijual == "makanan hewan" or yg_dijual == "Makanan hewan"):
            print(color.bold + "ini adalah makanan hewan yang dijual")
            print("Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_makanan_h)):
                for j in range(len(data_makanan_h[i])):
                    print(data_makanan_h[i][j], end = "\t\t\t ")
                print()
            cek_barang3 = len(data_makanan_h) - 1
            B_barang = input(color.e + color.g + "Masukkkan jenis makanan hewan yang mau anda beli: " + color.e)
            while (cek_barang3 >= 0):
                if (B_barang == data_makanan_h[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_makanan_h[cek_barang3][0]):
                JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                if (JB_barang <= 0):
                    print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                elif (JB_barang <= data_makanan_h[cek_barang3][1]):
                    T_harga = JB_barang * data_makanan_h[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.y + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!")
                    time.sleep(1)
                    os.system("cls")
                    print("Berikut ini adalah Struk Pembayaran" + color.e)
                    time.sleep(2)
                    print(color.y + "||===========================================||")
                    print("||              PETSHOP Hada                 ||")
                    print("||            Struk Pembayaran               ||")
                    print("||Nama stock  : ", B_barang)
                    print("||Jumlah stock: ", JB_barang)
                    print("||Total harga : Rp. ", T_harga)
                    print("||===========================================||" + color.e)
                    time.sleep(5)
                    os.system("cls")
                    print(color.y + "||===========================================||")
                    print("||     Silahkan ke kasir untuk pembayaran    ||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    time.sleep(3)
                    os.system("cls")
                else:
                    print(color.r + "Maaf jumlah makanan hewan yang tersedia tidak cukup" + color.e)
            else:
                print(color.r + "Maaf makanan hewan yang anda masukkan tidak ada" + color.e)

          elif (yg_dijual == "4" or yg_dijual == "keperluan hewan" or yg_dijual == "Keperluan hewan"):
            print(color.bold + "ini adalah berberapa keperluan hewan yang dijual")
            print("Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(data_keperluan_h)):
                for j in range(len(data_keperluan_h[i])):
                    print(data_keperluan_h[i][j], end = "\t\t\t ")
                print()
            cek_barang3 = len(data_keperluan_h) - 1
            B_barang = input(color.e + color.g + "Masukkkan keperluan hewan yang mau anda beli: " + color.e)
            while (cek_barang3 >= 0):
                if (B_barang == data_keperluan_h[cek_barang3][0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == data_keperluan_h[cek_barang3][0]):
                JB_barang = int(input(color.g + "Masukkan jumlah keperluan hewan yang dibeli: " + color.e))
                if (JB_barang <= 0):
                    print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                elif (JB_barang <= data_keperluan_h[cek_barang3][1]):
                    T_harga = JB_barang * data_keperluan_h[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.y + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!")
                    time.sleep(1)
                    os.system("cls")
                    print("Berikut ini adalah Struk Pembayaran" + color.e)
                    time.sleep(2)
                    print(color.y + "||===========================================||")
                    print("||              PETSHOP Hada                 ||")
                    print("||            Struk Pembayaran               ||")
                    print("||Nama stock  : ", B_barang)
                    print("||Jumlah stock: ", JB_barang)
                    print("||Total harga : Rp. ", T_harga)
                    print("||===========================================||" + color.e)
                    time.sleep(5)
                    os.system("cls")
                    print(color.y + "||===========================================||")
                    print("||     Silahkan ke kasir untuk pembayaran    ||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    time.sleep(3)
                    os.system("cls")
                else:
                    print(color.r + "Maaf jumlah keperluan hewan yang tersedia tidak cukup" + color.e)
            else:
                print(color.r + "Maaf barang keperluan hewan yang anda masukkan tidak ada" + color.e)
          elif (yg_dijual == "5" or yg_dijual == "stock baru" or yg_dijual == "Stock baru"):
            print(color.bold + "ini adalah beberapa stock baru yang dijual")
            print("Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            for i in range(len(stock_baru)):
                for j in range(len(stock_baru[i])):
                    print(stock_baru[i][j], end = "\t\t\t ")
                print()
            cek_barang3 = len(stock_baru) - 1
            B_barang = input(color.e + color.g + "Masukkkan stock baru yang mau anda beli: " + color.e)
            while (cek_barang3 >= 0):
                if (B_barang == stock_baru[0]):
                    break
                else:
                    cek_barang3 -= 1
            if (B_barang == stock_baru[cek_barang3][0]):
                JB_barang = int(input(color.g + "Masukkan jumlah stock terbaru yang dibeli: " + color.e))
                if (JB_barang <= 0):
                    print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                elif (JB_barang <= stock_baru[cek_barang3][1]):
                    T_harga = JB_barang * stock_baru[cek_barang3][2]
                    time.sleep(2)
                    os.system("cls")
                    print(color.y + "Pesanan anda sedang di proses..0%")
                    time.sleep(3)
                    print("Pesanan anda sedang di proses..50%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..75%")
                    time.sleep(2)
                    print("Pesanan anda sedang di proses..100%!!")
                    time.sleep(1)
                    os.system("cls")
                    print("Berikut ini adalah Struk Pembayaran" + color.e)
                    time.sleep(2)
                    print(color.y + "||===========================================||")
                    print("||              PETSHOP Hada                 ||")
                    print("||            Struk Pembayaran               ||")
                    print("||Nama stock  : ", B_barang)
                    print("||Jumlah stock: ", JB_barang)
                    print("||Total harga : Rp. ", T_harga)
                    print("||===========================================||" + color.e)
                    time.sleep(5)
                    os.system("cls")
                    print(color.y + "||===========================================||")
                    print("||     Silahkan ke kasir untuk pembayaran    ||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    time.sleep(3)
                    os.system("cls")
                else:
                    print(color.r + "Maaf jumlah stock baru yang tersedia tidak cukup" + color.e)
            else:
                print(color.r + "Maaf stock terbaru yang anda masukkan tidak ada" + color.e)
          else:
            print(color.r + "saat ini hanya itu saja yang kami jual" + color.e)

        elif (pilihan2 == "2" or pilihan2 == "logout" or pilihan2 == "Logout"):
            print(color.y + "||===========================================||")
            print("||          telah berhasil logout!!          ||")
            print("||===========================================||" + color.e)
            break

        else:
            print(color.r + "Maaf menu yang anda pilih tidak tersedia" + color.e)
        time.sleep(3)
        os.system("cls")
                      
                
#Menu login
while True:
    print(color.u + "||===========================================||")
    print("||                   LOGIN                   ||" + color.e)
    cek = len(username) - 1
    print(color.u + "||===========================================||")
    print("||     Silahkan masukan username             ||" + color.e)
    cek_username = input(color.g + "Username: " + color.e)
    print(color.u + "||     Silahkan masukan password             ||" + color.e)
    cek_password = input(color.g + "Password: " + color.e)
    print(color.u + "||===========================================||" + color.e)
    while (cek >= 0):
        if (cek_username == username[cek]):
            if (cek_password == password[cek]):
                break
            else:
                cek -= 1
        else:
            cek -= 1
            
    if (cek == -1):
        print(color.r + "Maaf username atau password yang anda masukkan salah")
        print("Silahkan masukan username atau password dengan benar!" + color.e)
        time.sleep(3)
        os.system("cls")

    elif (sebagai[cek] == "Admin"):
        print(color.y + "||===========================================||")
        print("||     Awali hari kerjamu dengan senyuman    ||")
        print("||            Selamat bekerja!!              ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")
        menu_admin()
        print(color.y + "||===========================================||")
        print("||               Terimakasih                 ||")
        print("||           Kembali ke menu login           ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")
    elif (sebagai[cek] == "Pelanggan"):
        print(color.y + "||===========================================||")
        print("||       Selamat Datang di PETSHOP Hada      ||")
        print("||           Selamat berbelanja!!            ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")
        menu_pelanggan()
        print(color.y + "||===========================================||")
        print("||       Terima kasih telah berbelanja       ||")
        print("||          Selamat datang kembali!          ||")
        print("||           Kembali ke menu login           ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")