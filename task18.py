def juft_toq_soni(sonlar):
    juft = 0
    toq = 0
    for son in sonlar:
        if son % 2 == 0:
            juft += 1
        else:
            toq += 1
    print(f"Juft: {juft}, Toq: {toq}")

sonlar = [10, 13, 15, 8, 22, 7]
juft_toq_soni(sonlar)