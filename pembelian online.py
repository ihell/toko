data_product = {
    1:"Laptop",
    2:"Mouse",
    3:"Keyboard",
    4:"Monitor",
    5:"Mouse Pad"
}
daftar_harga = {
    1:"2000000",
    2:"60000",
    3:"700000",
    4:"1000000",
    5:"500000"
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit"
}
print("===========List Product===========")
for i in data_product:
    print("Id Product : ",i,"\t Nama Product : ",data_product[i],"\t Harga Product : ",daftar_harga[i])