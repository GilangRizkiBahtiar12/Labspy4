x=["a","b","c","d","e"]
y=["g","h","i","j","k"]


y.append(x[1:3])
print("2 bagian list yang x di jadikan list y:", y)


y.append("Kami")
print("tambah y dengan sring:", y)


print("tambahkan list y dengan 3 nilai:", y+["l","m","n"])


z=y+x
print("gabungan list y dan x:", z)