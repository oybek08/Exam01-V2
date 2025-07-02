def fayl_turi(fayl_nomi):
    return f"Fayl turi: {fayl_nomi.strip().split('.')[-1]}"

print(fayl_turi("logo.svg"))