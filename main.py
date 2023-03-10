para = (int(input("Kuruş miktarını giriniz: ")))

if (para >= 100):
    kurus = (int(para // 100))
    para = (int(para % 100))
    print("{} adet 1 TL".format(kurus))

if (para >= 50):
    kurus = (int(para // 50))
    para = (int(para % 50))
    print("{} adet 50 KR".format(kurus))

if (para >= 20):
    kurus = (int(para // 25))
    para = (int(para % 25))
    print("{} adet 25 KR".format(kurus))

if (para >= 10):
    kurus = (int(para // 10))
    para = (int(para % 10))
    print("{} adet 10 KR".format(kurus))

if (para >= 5):
    kurus = (int(para // 5))
    para = (int(para % 5))
    print("{} adet 5 KR".format(kurus))

if (para >= 1):
    kurus = (int(para // 1))
    para = (int(para % 1))
    print("{} adet 1 KR".format(kurus))