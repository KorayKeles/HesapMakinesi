## Kendi yazacağımız metotların bulunduğu dosya

from PyQt6.QtWidgets import *
from tasarim import Ui_Form

## QMainWindow: Form içinde tanımlanan diğer buton,label,textbox gibi
## araçları kapsayan anapencere formu. Burayı Bizim formumuz miras alıyor

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bilgi = Ui_Form()  # Qt Designer ile oluşturulan tasarıma erişim
        self.bilgi.setupUi(self)

        # Girilen sayılar için bir liste
        self.sayilar = []

        # Tablo yapılandırması
        self.bilgi.tbl_sayilar.setColumnCount(1)  # Tek sütun
        self.bilgi.tbl_sayilar.setHorizontalHeaderLabels(["Sayılar"])  # Sütun başlığı
        self.bilgi.tbl_sayilar.horizontalHeader().setStretchLastSection(True)  # Sütun genişliği otomatik

        # "Yeni Sayı Ekle" ve "Son Sayıyı Kaldır" butonlarına tıklama olaylarını bağla
        self.bilgi.btn_yeni_sayi.clicked.connect(self.yeni_sayi_ekle)
        self.bilgi.btn_son_sayi_kaldir.clicked.connect(self.son_sayi_kaldir)

        # İşlem butonlarını tıklama olaylarına bağla
        self.bilgi.btn_topla.clicked.connect(self.topla)
        self.bilgi.btn_cikar.clicked.connect(self.cikar)
        self.bilgi.btn_carp.clicked.connect(self.carp)
        self.bilgi.btn_bol.clicked.connect(self.bol)

    def yeni_sayi_ekle(self):
        """txt_sayi1 alanındaki sayıyı alır ve listeye ekler, tbl_sayilar'da gösterir."""
        try:
            sayi = float(self.bilgi.txt_sayi1.text())  # Yeni girilen sayıyı al
            self.sayilar.append(sayi)  # Listeye ekle

            # tbl_sayilar tablosuna yeni satır ekle
            satir_sayisi = self.bilgi.tbl_sayilar.rowCount()
            self.bilgi.tbl_sayilar.insertRow(satir_sayisi)  # Yeni satır ekle
            self.bilgi.tbl_sayilar.setItem(satir_sayisi, 0, QTableWidgetItem(str(sayi)))  # Sayıyı ekle

            # txt_sayi1'i yeni sayı girişi için boşalt
            self.bilgi.txt_sayi1.clear()
        
        except ValueError:
            QMessageBox.warning(self, "Geçersiz Giriş", "Lütfen geçerli bir sayı girin.")

    def son_sayi_kaldir(self):
        """Listeye eklenmiş son sayıyı kaldırır ve tbl_sayilar tablosunda günceller."""
        if self.sayilar:
            self.sayilar.pop()  # Son sayıyı listeden çıkar

            # tbl_sayilar tablosundan son satırı kaldır
            satir_sayisi = self.bilgi.tbl_sayilar.rowCount()
            self.bilgi.tbl_sayilar.removeRow(satir_sayisi - 1)

    def topla(self):
        sonuc = sum(self.sayilar)
        self.bilgi.lineSonuc.setText(str(sonuc))

    def cikar(self):
        if self.sayilar:
            sonuc = self.sayilar[0]
            for sayi in self.sayilar[1:]:
                sonuc -= sayi
            self.bilgi.lineSonuc.setText(str(sonuc))

    def carp(self):
        if self.sayilar:
            sonuc = 1
            for sayi in self.sayilar:
                sonuc *= sayi
            self.bilgi.lineSonuc.setText(str(sonuc))

    def bol(self):
        try:
            if self.sayilar:
                sonuc = self.sayilar[0]
                for sayi in self.sayilar[1:]:
                    if sayi == 0:
                        raise ZeroDivisionError("Bölen sıfır olamaz.")
                    sonuc /= sayi
                self.bilgi.lineSonuc.setText(str(sonuc))
        except ZeroDivisionError as e:
            QMessageBox.critical(self, "HATA", str(e))