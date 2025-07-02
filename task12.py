def tugash_indexi_top(matn, soz):
    start_index = matn.find(soz)
    if start_index == -1:
        return -1 
    return start_index + len(soz)

matn = "Men HTML va CSS urganmoqdaman"
soz = "CSS"
chiqish = tugash_indexi_top(matn, soz)
print(chiqish) 