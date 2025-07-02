def chipta_narxi(yosh, asosiy_narx=80000):
    if yosh <= 5:
        chegirma = 0.60
    elif 6 <= yosh <= 12:
        chegirma = 0.30
    elif yosh > 55:
        chegirma = 0.40
    else:
        chegirma = 0.0

    yakuniy_narx = asosiy_narx * (1 - chegirma)
    print(f"Yakuniy narx: {yakuniy_narx} so'm ({int(chegirma * 100)}% chegirma qo'llanildi)" if chegirma > 0 else f"Yakuniy narx: {asosiy_narx} so'm (chegirma qo'llanilmadi)")

chipta_narxi(10)