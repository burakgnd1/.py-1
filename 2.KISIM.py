class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None
        self.onceki = None

class TekBaglantiliListe:
    def __init__(self):
        self.bas = None

    def basa_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        yeni_dugum.sonraki = self.bas
        self.bas = yeni_dugum

    def sona_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:
            self.bas = yeni_dugum
            return
        gecici = self.bas
        while gecici.sonraki:
            gecici = gecici.sonraki
        gecici.sonraki = yeni_dugum

    def ortaya_ekle(self, n, veri):
        gecici = self.bas
        sayac = 0
        while gecici and sayac < n:
            gecici = gecici.sonraki
            sayac += 1
        if gecici:
            yeni_dugum = Dugum(veri)
            yeni_dugum.sonraki = gecici.sonraki
            gecici.sonraki = yeni_dugum

    def ara(self, veri):
        gecici = self.bas
        while gecici:
            if gecici.veri == veri:
                return True
            gecici = gecici.sonraki
        return False

    def bastan_sil(self):
        if self.bas:
            self.bas = self.bas.sonraki

    def sondan_sil(self):
        if not self.bas:
            return
        if not self.bas.sonraki:
            self.bas = None
            return
        gecici = self.bas
        while gecici.sonraki and gecici.sonraki.sonraki:
            gecici = gecici.sonraki
        gecici.sonraki = None

    def dugum_sil(self, veri):
        if not self.bas:
            return
        if self.bas.veri == veri:
            self.bas = self.bas.sonraki
            return
        gecici = self.bas
        while gecici.sonraki and gecici.sonraki.veri != veri:
            gecici = gecici.sonraki
        if gecici.sonraki:
            gecici.sonraki = gecici.sonraki.sonraki

    def dugum_sayisi(self):
        sayac = 0
        gecici = self.bas
        while gecici:
            sayac += 1
            gecici = gecici.sonraki
        return sayac

    def listele(self):
        sonuc = []
        gecici = self.bas
        while gecici:
            sonuc.append(gecici.veri)
            gecici = gecici.sonraki
        return sonuc

class CiftBaglantiliListe:
    def __init__(self):
        self.bas = None
        self.son = None

    def basa_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:
            self.bas = self.son = yeni_dugum
        else:
            yeni_dugum.sonraki = self.bas
            self.bas.onceki = yeni_dugum
            self.bas = yeni_dugum

    def sona_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:
            self.bas = self.son = yeni_dugum
        else:
            self.son.sonraki = yeni_dugum
            yeni_dugum.onceki = self.son
            self.son = yeni_dugum

    def ortaya_ekle(self, n, veri):
        if not self.bas:
            return
        gecici = self.bas
        sayac = 0
        while gecici and sayac < n:
            gecici = gecici.sonraki
            sayac += 1
        if gecici:
            yeni_dugum = Dugum(veri)
            yeni_dugum.sonraki = gecici.sonraki
            yeni_dugum.onceki = gecici
            if gecici.sonraki:
                gecici.sonraki.onceki = yeni_dugum
            gecici.sonraki = yeni_dugum
            if yeni_dugum.sonraki is None:
                self.son = yeni_dugum

    def ara(self, veri):
        gecici = self.bas
        while gecici:
            if gecici.veri == veri:
                return True
            gecici = gecici.sonraki
        return False

    def bastan_sil(self):
        if not self.bas:
            return
        if self.bas == self.son:
            self.bas = self.son = None
        else:
            self.bas = self.bas.sonraki
            self.bas.onceki = None

    def sondan_sil(self):
        if not self.son:
            return
        if self.bas == self.son:
            self.bas = self.son = None
        else:
            self.son = self.son.onceki
            self.son.sonraki = None

    def dugum_sil(self, veri):
        gecici = self.bas
        while gecici:
            if gecici.veri == veri:
                if gecici.onceki:
                    gecici.onceki.sonraki = gecici.sonraki
                if gecici.sonraki:
                    gecici.sonraki.onceki = gecici.onceki
                if gecici == self.bas:
                    self.bas = gecici.sonraki
                if gecici == self.son:
                    self.son = gecici.onceki
                return
            gecici = gecici.sonraki

    def dugum_sayisi(self):
        sayac = 0
        gecici = self.bas
        while gecici:
            sayac += 1
            gecici = gecici.sonraki
        return sayac

    def listele(self):
        sonuc = []
        gecici = self.bas
        while gecici:
            sonuc.append(gecici.veri)
            gecici = gecici.sonraki
        return sonuc

class DaireselBaglantiliListe:
    def __init__(self):
        self.bas = None

    def basa_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:
            self.bas = yeni_dugum
            yeni_dugum.sonraki = yeni_dugum
        else:
            gecici = self.bas
            while gecici.sonraki != self.bas:
                gecici = gecici.sonraki
            yeni_dugum.sonraki = self.bas
            self.bas = yeni_dugum
            gecici.sonraki = self.bas

    def sona_ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if not self.bas:
            self.bas = yeni_dugum
            yeni_dugum.sonraki = self.bas
        else:
            gecici = self.bas
            while gecici.sonraki != self.bas:
                gecici = gecici.sonraki
            gecici.sonraki = yeni_dugum
            yeni_dugum.sonraki = self.bas

    def ortaya_ekle(self, n, veri):
        if not self.bas:
            return
        gecici = self.bas
        sayac = 0
        while gecici.sonraki != self.bas and sayac < n:
            gecici = gecici.sonraki
            sayac += 1
        yeni_dugum = Dugum(veri)
        yeni_dugum.sonraki = gecici.sonraki
        gecici.sonraki = yeni_dugum

    def ara(self, veri):
        if not self.bas:
            return False
        gecici = self.bas
        while True:
            if gecici.veri == veri:
                return True
            gecici = gecici.sonraki
            if gecici == self.bas:
                break
        return False

    def bastan_sil(self):
        if not self.bas:
            return
        if self.bas.sonraki == self.bas:
            self.bas = None
        else:
            gecici = self.bas
            while gecici.sonraki != self.bas:
                gecici = gecici.sonraki
            self.bas = self.bas.sonraki
            gecici.sonraki = self.bas

    def sondan_sil(self):
        if not self.bas:
            return
        if self.bas.sonraki == self.bas:
            self.bas = None
        else:
            gecici = self.bas
            while gecici.sonraki.sonraki != self.bas:
                gecici = gecici.sonraki
            gecici.sonraki = self.bas

    def dugum_sil(self, veri):
        if not self.bas:
            return
        if self.bas.veri == veri:
            self.bastan_sil()
            return
        gecici = self.bas
        while gecici.sonraki != self.bas and gecici.sonraki.veri != veri:
            gecici = gecici.sonraki
        if gecici.sonraki.veri == veri:
            gecici.sonraki = gecici.sonraki.sonraki

    def dugum_sayisi(self):
        if not self.bas:
            return 0
        sayac = 1
        gecici = self.bas.sonraki
        while gecici != self.bas:
            sayac += 1
            gecici = gecici.sonraki
        return sayac

    def listele(self):
        if not self.bas:
            return []
        sonuc = []
        gecici = self.bas
        while True:
            sonuc.append(gecici.veri)
            gecici = gecici.sonraki
            if gecici == self.bas:
                break
        return sonuc

class Yigin:
    def __init__(self):
        self.elemanlar = []

    def ekle(self, veri):
        self.elemanlar.append(veri)

    def cikar(self):
        if not self.elemanlar:
            return None
        return self.elemanlar.pop()

    def ters_cevir(self):
        gecici_yigin = Yigin()
        while self.elemanlar:
            gecici_yigin.ekle(self.cikar())
        self.elemanlar = gecici_yigin.elemanlar

    def listele(self):
        return self.elemanlar


def menu():
    tek_baglantili_liste = TekBaglantiliListe()
    cift_baglantili_liste = CiftBaglantiliListe()
    dairesel_baglantili_liste = DaireselBaglantiliListe()
    yigin = Yigin()

    while True:
        print("\n--- Ana Menü ---")
        print("1. Tekli Bağlantılı Liste")
        print("2. Çiftli Bağlantılı Liste")
        print("3. Dairesel Bağlantılı Liste")
        print("4. Yığın")
        print("0. Çıkış")

        secim = int(input("Seçiminiz: "))

        if secim == 1:
            tek_baglantili_liste_menu(tek_baglantili_liste)
        elif secim == 2:
            cift_baglantili_liste_menu(cift_baglantili_liste)
        elif secim == 3:
            dairesel_baglantili_liste_menu(dairesel_baglantili_liste)
        elif secim == 4:
         yigin_menu(yigin)
        elif secim == 0:
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")    

def tek_baglantili_liste_menu(tek_baglantili_liste):
    while True:
        print("\n--- Tekli Bağlantılı Liste ---")
        print("1. Başa Ekle")
        print("2. Sona Ekle")
        print("3. Ortaya Ekle")
        print("4. Ara")
        print("5. Baştan Sil")
        print("6. Sondan Sil")
        print("7. Listeyi Göster")
        print("0. Ana Menüye Dön")

        secim = int(input("Seçiminiz: "))
        if secim == 1:
            veri = input("Eklenecek veri: ")
            tek_baglantili_liste.basa_ekle(veri)
        elif secim == 2:
            veri = input("Eklenecek veri: ")
            tek_baglantili_liste.sona_ekle(veri)
        elif secim == 3:
            n = int(input("Hangi düğümden sonra: "))
            veri = input("Eklenecek veri: ")
            tek_baglantili_liste.ortaya_ekle(n, veri)
        elif secim == 4:
            veri = input("Aranacak veri: ")
            bulundu = tek_baglantili_liste.ara(veri)
            print("Bulundu" if bulundu else "Bulunamadı")
        elif secim == 5:
            tek_baglantili_liste.bastan_sil()
        elif secim == 6:
            tek_baglantili_liste.sondan_sil()
        elif secim == 7:
            print("Liste: ", tek_baglantili_liste.listele())
        elif secim == 0:
            break
        else:
            print("Geçersiz seçim!")

def cift_baglantili_liste_menu(cift_baglantili_liste):
    while True:
        print("\n--- Çiftli Bağlantılı Liste ---")
        print("1. Başa Ekle")
        print("2. Sona Ekle")
        print("3. Ortaya Ekle")
        print("4. Ara")
        print("5. Baştan Sil")
        print("6. Sondan Sil")
        print("7. Listeyi Göster")
        print("0. Ana Menüye Dön")

        secim = int(input("Seçiminiz: "))
        if secim == 1:
          veri = input("Eklenecek veri: ")
          cift_baglantili_liste.basa_ekle(veri)
        elif secim == 2:
            veri = input("Eklenecek veri: ")
            cift_baglantili_liste.sona_ekle(veri)
        elif secim == 3:
            n = int(input("Hangi düğümden sonra: "))
            veri = input("Eklenecek veri: ")
            cift_baglantili_liste.ortaya_ekle(n, veri)
        elif secim == 4:
            veri = input("Aranacak veri: ")
            bulundu = cift_baglantili_liste.ara(veri)
            print("Bulundu" if bulundu else "Bulunamadı")
        elif secim == 5:
            cift_baglantili_liste.bastan_sil()
        elif secim == 6:
            cift_baglantili_liste.sondan_sil()
        elif secim == 7:
            print("Liste: ", cift_baglantili_liste.listele())
        elif secim == 0:
            break
        else:
            print("Geçersiz seçim!")

def dairesel_baglantili_liste_menu(dairesel_baglantili_liste):
    while True:
        print("\n--- Dairesel Bağlantılı Liste ---")
        print("1. Başa Ekle")
        print("2. Sona Ekle")
        print("3. Ortaya Ekle")
        print("4. Ara")
        print("5. Baştan Sil")
        print("6. Sondan Sil")
        print("7. Listeyi Göster")
        print("0. Ana Menüye Dön")

        secim = int(input("Seçiminiz: "))
        if secim == 1:
            veri = input("Eklenecek veri: ")
            dairesel_baglantili_liste.basa_ekle(veri)
        elif secim == 2:
            veri = input("Eklenecek veri: ")
            dairesel_baglantili_liste.sona_ekle(veri)
        elif secim == 3:
            n = int(input("Hangi düğümden sonra: "))
            veri = input("Eklenecek veri: ")
            dairesel_baglantili_liste.ortaya_ekle(n, veri)
        elif secim == 4:
            veri = input("Aranacak veri: ")
            bulundu = dairesel_baglantili_liste.ara(veri)
            print("Bulundu" if bulundu else "Bulunamadı")
        elif secim == 5:
            dairesel_baglantili_liste.bastan_sil()
        elif secim == 6:
            dairesel_baglantili_liste.sondan_sil()
        elif secim == 7:
            print("Liste: ", dairesel_baglantili_liste.listele())
        elif secim == 0:
            break
        else:
            print("Geçersiz seçim!")            

def yigin_menu(yigin):
    while True:
        print("\n--- Yığın ---")
        print("1. Eleman Ekle")
        print("2. Eleman Çıkar")
        print("3. Yığını Ters Çevir")
        print("4. Yığını Göster")
        print("0. Ana Menüye Dön")

        secim = int(input("Seçiminiz: "))
        if secim == 1:
            veri = input("Eklenecek veri: ")
            yigin.ekle(veri)
        elif secim == 2:
            cikarilan = yigin.cikar()
            if cikarilan is None:
                print("Yığın boş!")
            else:
                print("Çıkarılan veri:", cikarilan)
        elif secim == 3:
            yigin.ters_cevir()
        elif secim == 4:
            print("Yığın:", yigin.listele())
        elif secim == 0:
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    menu()