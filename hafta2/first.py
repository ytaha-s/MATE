ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
sehir = input("Yaşadığınız şehri giriniz: ")
print(f"{ad} {soyad}, {sehir} şehrinde yaşamaktadır.\n")



def indirim_hesapla():
    tutar = float(input("Fiyatsız tutarı giriniz (TL): "))
    indirim_yuzdesi = float(input("İndirim yüzdesini giriniz (%): "))
    
    indirim_tutari = tutar * (indirim_yuzdesi / 100)
    son_fiyat = tutar - indirim_tutari
    
    print(f"İndirim Tutarı: {indirim_tutari} TL")
    print(f"İndirimli Son Fiyat: {son_fiyat} TL\n")

indirim_hesapla()



dogum_yili = int(input("Doğum yılınızı giriniz: "))
mevcut_yil = 2026
yas = mevcut_yil - dogum_yili

print(f"Yaşınız: {yas}")
if yas >= 18:
    print("Ehliyet alabilirsiniz.\n")
else:
    print("Ehliyet almak için yaşınız yetersiz.\n")



def harf_notu_hesapla():
    vize = float(input("Vize notunuzu giriniz: "))
    final = float(input("Final notunuzu giriniz: "))
    
    ortalama = (vize * 0.40) + (final * 0.60)
    
    if ortalama >= 90:
        harf_notu = "AA"
    elif ortalama >= 85:
        harf_notu = "BA"
    elif ortalama >= 80:
        harf_notu = "BB"
    elif ortalama >= 75:
        harf_notu = "CB"
    elif ortalama >= 70:
        harf_notu = "CC"
    elif ortalama >= 65:
        harf_notu = "DC"
    elif ortalama >= 60:
        harf_notu = "DD"
    elif ortalama >= 50:
        harf_notu = "FD"
    else:
        harf_notu = "FF"
        
    print(f"Ortalamanız: {ortalama:.2f}")
    print(f"Harf Notunuz: {harf_notu}\n")

harf_notu_hesapla()
