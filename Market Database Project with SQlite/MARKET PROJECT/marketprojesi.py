import sqlite3
import time
from datetime import datetime


class Market():
    def __init__(self,barkod,marka,fiyat,stok_adedi,üretim_tarihi,son_kullanım_tarihi,yapım_yeri):
        self.barkod = barkod
        self.marka = marka
        self.fiyat = fiyat
        self.stok_adedi = stok_adedi
        self.üretim_tarihi = üretim_tarihi
        self.son_kullanım_tarihi = son_kullanım_tarihi
        self.yapım_yeri = yapım_yeri


    def __str__(self):
        return "Barkod : {}\nMarka = {}\nFiyat : {}\nStok Adedi : {}\nÜretim Tarihi : {}\nSon Kullanım Tarihi : {}\nYapım Yeri : {}".format(self.barkod,self.marka,self.fiyat,self.stok_adedi,self.üretim_tarihi,self.son_kullanım_tarihi,self.yapım_yeri)


class Ürünler():

    def __init__(self):

        self.baglantı_olustur()

    def baglantı_olustur(self):

        self.baglantı = sqlite3.connect("Süpermarket.db")

        self.cursor = self.baglantı.cursor()

        sorgu = "Create Table if not exists Market(barkod INT,marka TEXT,fiyat INT,stok_adedi INT,üretim_tarihi TEXT,son_kullanma_tarihi TEXT,yapım_yeri TEXT)"

        self.cursor.execute(sorgu)

        self.baglantı.commit()

    def baglantı_kes(self):
        self.baglantı.close()


    def ürünleri_göster(self):

        sorgu = "Select * From Market"

        self.cursor.execute(sorgu)

        data = self.cursor.fetchall()
        if len(data)==0:
            print("Markette ürün bulunmamaktadır.....")
        else:
            for i in data:
                ürün = Market(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(ürün)
                print("-----------------------------------")

    def ürün_sorgula(self,barkod):

        sorgu = "Select * From Market where barkod =?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()

        if len(data) ==0:
            print("Markette bu barkodda ürün bulunmamaktadır....")

        else:
            ürün = Market(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6])

            print(ürün)

    def ürün_ekle(self,ürün):

        sorgu = "Insert Into Market Values(?,?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(ürün.barkod,ürün.marka,ürün.fiyat,ürün.stok_adedi,ürün.üretim_tarihi,ürün.son_kullanım_tarihi,ürün.yapım_yeri,))

        self.baglantı.commit()

    def ürün_sil(self,barkod,):

            sorgu2 = "Delete From Market where barkod =?"

            self.cursor.execute(sorgu2, (barkod,))

            self.baglantı.commit()


    def fiyat_değiştirme(self,barkod):

        sorgu = "Select * From Market where barkod =?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()

        if len(data) == 0 :
            print("Markette ürün bulunmamaktadır...")

        else:
            fiyat = data[0][2]

            cevap = input("Azaltmak için 'azalt'--- Artırmak için 'artır' yazınız... Cevap : ")

            if cevap == "artır":
                istek = float(input("Ne kadar artırmak istiyorsunuz: "))

                fiyat += istek

            elif cevap == "azalt":
                istek = float(input("Ne kadar azaltmak istiyorsunuz: "))

                fiyat -= istek

            else:
                print("Sadece azaltma ve artırma işlemi yapabilirsiniz...")


        sorgu2 = "Update Market set fiyat = ? where barkod = ?"

        self.cursor.execute(sorgu2,(fiyat,barkod,))

        self.baglantı.commit()

    def stok_adedi_değiştirme(self,barkod,):

        sorgu = "Select * From Market where barkod=?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Markette ürün bulunmamaktadır....")

        else:
            stok_adedi = data[0][3]

            cevap = input("Azaltmak için 'azalt'--- Artırmak için 'artır' yazınız "
                          "Cevap : ")

            if cevap == "artır":
                istek = int(input("Ne kadar artırmak istiyorsunuz: "))

                stok_adedi += istek

            elif cevap == "azalt":
                istek = int(input("Ne kadar azaltmak istiyorsunuz: "))

                stok_adedi -= istek

            else:
                print("Sadece azaltma ve artırma işlemi yapabilirsiniz...")

        sorgu2 = "Update Market set stok_adedi =? where barkod=?"

        self.cursor.execute(sorgu2,(stok_adedi,barkod,))
        self.baglantı.commit()

    def tarih_sorgulama(self,barkod):

        sorgu = "Select * From Market where barkod=?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()


        if len(data) == 0 :
            print("Markette ürün bulunmamaktadır....")

        else:
            tarih = data[0][5]

            su_an = datetime.now()

            if str(su_an) > tarih :
                print("--------------------------")
                print("Bu ürünün son kullanma tarihi geçmiştir....")
                print("Firmamız bu sorundan dolayı sizden özür diliyor , hemen kaldırıyoruz ürünü!!")
                print("---------------------------")

            else:
                print("Rahatlıkla tüketebelirsiniz....")



    def yapım_yeri_değiştirme(self,barkod):

        sorgu = "Select * From Market where barkod=?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()

        if len(data) == 0 :
            print("Markette bu barkoda sahip bir ürün bulunmamaktadır....")

        else:

            yapım_yeri =  data[0][6]

            yeni_yer = input("Lütfen yeni yeri giriniz :  ")

            yapım_yeri = yeni_yer

            sorgu2 = "Update Market set yapım_yeri=? where barkod=?"

            self.cursor.execute(sorgu2,(yapım_yeri,(barkod,)))

            self.baglantı.commit()

    def barkod_değiştirme(self,girilecekbarkod):

        sorgu = "Select * From Market where barkod=?"

        self.cursor.execute(sorgu,(girilecekbarkod,))

        data = self.cursor.fetchall()

        if len(data) ==0:
            print("Markette bu barkoda sahip ürün bulunmamaktadır....")

        else:
            barcode = data[0][0]

            while True:
                try:
                    barkod = int(input("Lütfen yeni barkodu giriniz: "))
                    if len(str(barkod)) > 13:
                        print("13 değerden fazla olamaz")
                    elif len(str(barkod)) < 13:
                        print("13 değerden az olamaz")
                    else:
                        break
                except ValueError:
                    print("Lütfen sadece sayı giriniz...")




            barkod = barcode
            sorgu2 = "Update Market set barkod=? where barkod=?"

            self.cursor.execute(sorgu2,(barkod,girilecekbarkod,))

            self.baglantı.commit()

    def marka_değiştirme(self,barkod):

        sorgu = "Select * From Market where barkod=?"

        self.cursor.execute(sorgu,(barkod,))

        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Markette bu barkoda sahip ürün bulunmamaktadır....")

        else:
            marka = data[0][1]

            yeni_marka = input("Yeni markayı giriniz : ")

            marka = yeni_marka

            sorgu2 = "Update Market set marka=? where barkod=?"

            self.cursor.execute(sorgu2,(marka,barkod,))

            self.baglantı.commit()