#dictionary
#menyimpan pasangan kunci - nilai

kamus = {
    "nama" : "luffy",
    "buah iblis" : "nika",
    "status" : "alive"
}
print(kamus)

#nambah key dan value ke dictionary 
kamus["kru"] = "Mugiwara"

#menambah value pada bagian belakang value
kamus["nama"] += " 10"

#menghapus key-value pada dictionary
del kamus["status"]

#mengubah value
kamus["buah iblis"] = "gomu gomu"
print(kamus.values())
