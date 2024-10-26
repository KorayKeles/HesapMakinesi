## Ana program çalıştırma dosyası
from PyQt6.QtWidgets import QApplication # uygulama metodunu ekledik
from _tasarim import Form # oluşturduğumuz Form sınıfını ekledik

uygulama = QApplication([])
pencere = Form()  # oluşturulan Formu değişkene atadık
pencere.show()  # pencereyi göster
uygulama.exec() # uygulamayı çalıştır