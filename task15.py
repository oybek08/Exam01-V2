def bolinishni_tekshir(son):
    if son % 4 == 0:
        print(f"{son} soni 4 ga bo'linadi")
    else:
        print(f"{son} soni 4 ga bo'linmaydi")
        
    if son % 6 == 0:
        print(f"{son} soni 6 ga bo'linadi")
    else:
        print(f"{son} soni 6 ga bo'linmaydi")

bolinishni_tekshir(24)