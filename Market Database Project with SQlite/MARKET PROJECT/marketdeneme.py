import time

from marketprojesi import *
from datetime import datetime

marketprojesi = Ürünler()


print("""
-----------------------------------

Market Projesine hoşgeldniz....

------------------------------------

1- Ürünleri Göster

2- Ürün Sorgula

3- Ürün Ekle

4- Ürün Sil

5- Fiyat Değiştirme

6- Stok Adedi Değiştirme

7- Son Kullanma Tarihi Sorgulama

8- Yapım yerini Değiştirme

9- Barkod değiştirme

10- Marka değiştirme

Çıkış yapmak için 'q' harfini giriniz....

------------------------------------
""")

while True :
    cevap =  input("Lütfen yapmak istediğiniz işlemi giriniz :  ")

    if cevap == "q":
        marketprojesi.baglantı_kes()
        print("Programdan çıkılıyor...")
        print("Programdan çıkıldı...")
        break

    elif cevap == "1":
        print("Ürünlerin bilgileri....")
        time.sleep(2)
        marketprojesi.ürünleri_göster()


    elif cevap == "2":
        while True:
            try:
                barkod = int(input("Lütfen sorgulamak istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")
        print("Ürün sorgulanıyor...")
        time.sleep(2)
        marketprojesi.ürün_sorgula(barkod)

    elif cevap == "3":
        while True:
            try:
                barkod = int(input("Barkod : "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        marka = input("Marka : ")

        while True:
            try:
                fiyat = float(input("Fiyat : "))
                break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        while True:
            try:
                stok_adedi = int(input("Stok adedi : "))
                break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        print("-------------")
        print("Tarih yazarken araya '-' koymayı unutmayınız\nBir boşluk bırakarak üretim saatini giriniz...")
        print("-------------")
        while True:
            try:
                tarih = str(input("Üretim tarihi(Yıl-Ay-Gün -- Saat:Dakika) : "))
                üretim_tarihi = datetime.strptime(tarih, "%Y-%m-%d  %H:%M")

                tarih2 = str(input("Son kullanım tarihi (Yıl-Ay-Gün -- Saat:Dakika) : "))
                son_kullanım_tarihi = datetime.strptime(tarih2, "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("Lütfen yönergelere dikkat ediniz....")


        üretim_yeri = input("Üretim yeri : ")

        ürün = Market(barkod,marka,fiyat,stok_adedi,üretim_tarihi,son_kullanım_tarihi,üretim_yeri)


        print("Ürün ekleniyor....")

        marketprojesi.ürün_ekle(ürün)
        time.sleep(2)
        print("Ürün eklendi....")

    elif cevap == "4":
        while True:
            try:
                barkod = int(input("Lütfen silmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        istek = input("Emin misiniz  E/H :")
        if istek == "E":
            print("Ürün siliniyor....")
            time.sleep(2)
            marketprojesi.ürün_sil(barkod)
            print("Ürün silindi...")
        else:
            print("Nasıl isterseniz...")
            break

    elif cevap == "5":
        while True:
            try:
                barkod = int(input("Lütfen fiyatını değiştirmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")
        marketprojesi.fiyat_değiştirme(barkod)
        print("Fiyat değiştiriliyor....")
        time.sleep(2)
        print("Fiyat değiştirildi....")

    elif cevap == "6":
        while True:
            try:
                barkod = int(input("Lütfen stok adedini değiştirmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")
        marketprojesi.stok_adedi_değiştirme(barkod)
        print("Stok adedi değiştiriliyor....")
        time.sleep(2)
        print("Stok adedi değiştirildi....")

    elif cevap == "7":
        while True:
            try:
                barkod = int(input("Lütfen tarihini sorgulamak istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")
        print("Tarih sorgulanıyor...")
        time.sleep(2)
        marketprojesi.tarih_sorgulama(barkod)

    elif cevap == "8":
        while True:
            try:
                barkod = int(input("Lütfen yapım yerini değiştirmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        marketprojesi.yapım_yeri_değiştirme(barkod)
        print("Yer değiştiriliyor....")
        time.sleep(2)
        print("Yer değiştirldi...")

    elif cevap == "9":
        while True:
            try:
                barkod = int(input("Lütfen barkodunu değiştirmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        marketprojesi.barkod_değiştirme(barkod)
        print("Barkod değiştiriliyor....")
        time.sleep(2)
        print("Barkod değiştirildi.....")

    elif cevap == "10":
        while True:
            try:
                barkod = int(input("Lütfen markasını değiştirmek istediğiniz ürünün barkodunu giriniz: "))
                if len(str(barkod)) > 13:
                    print("13 değerden fazla olamaz")
                elif len(str(barkod)) < 13:
                    print("13 değerden az olamaz")
                else:
                    break
            except ValueError:
                print("Lütfen sadece sayı giriniz....")

        marketprojesi.marka_değiştirme(barkod)
        print("Marka değiştiriliyor....")
        time.sleep(2)
        print("Marka değiştirildi....")

    else:
        print("Geçerli işlem giriniz...")