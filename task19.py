def undosh_soni(harflar):
    undoshlar = "bcdfghjklmnpqrstvwxyz"
    sana = 0
    for harf in harflar:
        if harf.lower() in undoshlar:
            sana += 1
    print(sana)

letters = ["s", "a", "l", "A", "m"]
undosh_soni(letters)