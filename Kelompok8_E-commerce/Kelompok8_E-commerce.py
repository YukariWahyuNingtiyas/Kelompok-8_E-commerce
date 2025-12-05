produk = {
    1: {"nama": "Buku Tulis",   "harga": 5000,  "stok": 20},
    2: {"nama": "Pulpen",       "harga": 3000,  "stok": 30},
    3: {"nama": "Penghapus",    "harga": 2000,  "stok": 25},
    4: {"nama": "Tipe-X",       "harga": 5000,  "stok": 15},
    5: {"nama": "Penggaris",    "harga": 10000, "stok": 10},
    6: {"nama": "Pensil",       "harga": 4000,  "stok": 35},
    7: {"nama": "Rautan",       "harga": 6000,  "stok": 18},
    8: {"nama": "Spidol",       "harga": 7000,  "stok": 22},
    9: {"nama": "Spidol Warna", "harga": 12000, "stok": 15},
    10: {"nama": "Notebook A5", "harga": 15000, "stok": 12},
    11: {"nama": "Map Kertas",  "harga": 3000,  "stok": 40},
    12: {"nama": "Map Plastik", "harga": 6000,  "stok": 25},
    13: {"nama": "Sticky Notes","harga": 8000,  "stok": 20},
    14: {"nama": "Binder Clip", "harga": 5000,  "stok": 30},
    15: {"nama": "Isi Staples", "harga": 4000,  "stok": 28},
    16: {"nama": "Stapler Mini","harga": 15000, "stok": 10},
    17: {"nama": "Kertas HVS A4","harga":35000, "stok": 20},
    18: {"nama": "Kertas Warna","harga": 12000, "stok": 14},
    19: {"nama": "Lem Kertas",  "harga": 5000,  "stok": 26}
}

keranjang = {}

def lihat_produk():
    print("\nDAFTAR PRODUK ALAT TULIS\n")
    print(f"{'ID':<3} | {'Nama Barang':<22} | {'Harga':>10} | {'Stok':>4}")

    for pid, data in produk.items():
        print(f"{pid:<3} | {data['nama']:<22} | Rp{data['harga']:>8} | {data['stok']:>4}")
    print()

def tambah_keranjang():
    lihat_produk()
    print("INPUT PEMBELIAN")

    while True:
        pilih = input("Masukkan ID produk: ").strip()
        if pilih.isdigit():
            pilih = int(pilih)
            break
        print("Input harus angka!")

    while True:
        jumlah = input("Masukkan jumlah beli: ").strip()
        if jumlah.isdigit():
            jumlah = int(jumlah)
            break
        print("Input harus angka!")

    if pilih not in produk:
        print("Produk tidak ditemukan!")
        return

    if jumlah <= 0:
        print("Jumlah minimal 1!")
        return

    if jumlah > produk[pilih]["stok"]:
        print("Stok tidak cukup!")
        return

    keranjang[pilih] = keranjang.get(pilih, 0) + jumlah
    print("Barang berhasil masuk keranjang\n")

def lihat_keranjang():
    if not keranjang:
        print("\nKeranjang kosong\n")
        return

    print("\nKERANJANG ANDA")
    print("ID | Nama Barang            | Jumlah | Total")

    for pid, jumlah in keranjang.items():
        p = produk[pid]
        total = p["harga"] * jumlah
        print(f"{pid:<3}| {p['nama']:<22} | {jumlah:<6} | Rp{total:,}")
    print()

def update_keranjang():
    lihat_keranjang()
    if not keranjang:
        return

    print("UPDATE KERANJANG")

    while True:
        pilih = input("ID produk yang ingin diupdate: ").strip()
        if pilih.isdigit():
            pilih = int(pilih)
            break
        print("Input harus angka!")

    if pilih not in keranjang:
        print("Produk tidak ada di keranjang!")
        return

    while True:
        baru = input("Masukkan jumlah baru: ").strip()
        if baru.isdigit():
            baru = int(baru)
        else:
            print("Input harus angka!")
            continue

        if baru <= 0:
            print("Jumlah minimal 1!")
            continue

        if baru > produk[pilih]["stok"]:
            print("Stok tidak cukup!")
            continue

        break

    keranjang[pilih] = baru
    print("Jumlah berhasil diperbarui!\n")

def hapus_keranjang():
    lihat_keranjang()
    if not keranjang:
        return

    print("HAPUS BARANG")

    while True:
        pid = input("Masukkan ID produk yang ingin dihapus: ").strip()
        if pid.isdigit():
            pid = int(pid)
            break
        print("Input harus angka!")

    if pid not in keranjang:
        print("Produk tidak ditemukan dalam keranjang!\n")
        return

    jumlah_sekarang = keranjang[pid]
    print(f"Jumlah dalam keranjang: {jumlah_sekarang}")

    print("\nPilih aksi:")
    print("1. Hapus seluruh produk ini")
    print("2. Hapus sebagian (kurangi jumlah)")

    while True:
        aksi = input("Pilih (1/2): ").strip()
        if aksi.isdigit():
            aksi = int(aksi)
            break
        print("Input harus angka!")

    if aksi == 1:
        keranjang.pop(pid)
        print("Produk berhasil dihapus seluruhnya\n")
        return

    elif aksi == 2:
        while True:
            kurang = input("Mengurangi jumlah: ").strip()
            if kurang.isdigit():
                kurang = int(kurang)
                break
            print("Input harus angka!")

        if kurang <= 0:
            print("Jumlah tidak boleh 0 atau negatif!")
            return

        if kurang > jumlah_sekarang:
            print("Jumlah yang ingin dihapus melebihi jumlah di keranjang!")
            print("Produk tidak bisa dihapus\n")
            return

        if kurang == jumlah_sekarang:
            keranjang.pop(pid)
            print("Produk dihapus seluruhnya")
        else:
            keranjang[pid] = jumlah_sekarang - kurang
            print(f"Jumlah sekarang menjadi: {keranjang[pid]}")
    else:
        print("Pilihan tidak tersedia!")

def checkout():
    lihat_keranjang()
    if not keranjang:
        return

    print("CHECKOUT")
    print("Masukkan ID barang satu per satu. Ketik 0 jika selesai\n")

    valid_pilih = []

    while True:
        pid = input("Masukkan ID produk (0 untuk selesai): ").strip()
        if pid.isdigit():
            pid = int(pid)
        else:
            print("Input harus angka!")
            continue

        if pid == 0:
            break

        if pid not in keranjang:
            print("Produk tidak ada di keranjang!")
            continue

        if pid in valid_pilih:
            print("Produk sudah dipilih!")
            continue

        valid_pilih.append(pid)

    if not valid_pilih:
        print("Anda tidak memilih produk apa pun!")
        return

    total_semua = 0
    beli_data = {}

    for pid in valid_pilih:
        p = produk[pid]

        while True:
            jumlah = input(
                f"Masukkan jumlah untuk {p['nama']} (maks {keranjang[pid]}): "
            ).strip()

            if jumlah.isdigit():
                jumlah = int(jumlah)
                if 1 <= jumlah <= keranjang[pid]:
                    break
            print("Jumlah tidak valid!")

        beli_data[pid] = jumlah
        total_semua += jumlah * p["harga"]

    print("\nDATA PEMBELI")

    while True:
        nama = input("Nama lengkap: ").strip()
        if nama:
            break
        print("Nama tidak boleh kosong!")

    while True:
        no = input("Nomor telepon (12-13 digit): ").strip()
        if no.isdigit() and 12 <= len(no) <= 13:
            break
        print("Nomor telepon tidak valid!")

    while True:
        alamat = input("Alamat lengkap: ").strip()
        if alamat:
            break
        print("Alamat tidak boleh kosong!")

    print(f"\nTotal Harga Keseluruhan: Rp{total_semua:,}")
    print("\nMetode Pembayaran:")
    print("1. COD")
    print("2. Transfer Bank")

    while True:
        bayar = input("Pilih metode: ").strip()
        if bayar.isdigit():
            bayar = int(bayar)
            break
        print("Input harus angka!")

    metode = ""
    bayar_tf = ""
    tf_bayar = 0

    if bayar == 1:
        metode = "COD"

    elif bayar == 2:
        metode = "Transfer Bank"
        print("\nPilih Bank:")
        print("1. BRI\n2. BCA\n3. Mandiri\n4. BNI")

        bank_list = {1: "BRI", 2: "BCA", 3: "Mandiri", 4: "BNI"}

        while True:
            bank = input("Pilih bank: ").strip()

            if not bank.isdigit():
                print("Input harus angka!")
                continue

            bank = int(bank)

            if bank not in bank_list:
                print("Bank tidak tersedia! Silakan pilih ulang")
                continue

            bank = bank_list[bank]
            break

        while True:
            bayar_tf = input("Jumlah transfer: ").strip()

            if not bayar_tf.isdigit():
                print("Input harus angka!")
                continue

            tf_bayar = int(bayar_tf)

            if tf_bayar < total_semua:
                print("Uang kurang! Nominal harus pas")
                continue
            elif tf_bayar > total_semua:
                print("Uang berlebih! Nominal harus pas")
                continue
            else:
                break

    else:
        print("Metode tidak tersedia!")
        return

    for pid, jumlah in beli_data.items():
        produk[pid]["stok"] -= jumlah

    for pid in list(beli_data.keys()):
        if keranjang[pid] == beli_data[pid]:
            keranjang.pop(pid)
        else:
            keranjang[pid] -= beli_data[pid]

    print("\n---------------------------------------------")
    print("STRUK PEMBELIAN - E-COMMERCE ALAT TULIS")
    print("---------------------------------------------")
    print(f"Nama Pembeli   : {nama}")
    print(f"No Telepon     : {no}")
    print(f"Alamat         : {alamat}")
    print(f"Pembayaran     : {metode}\n")

    print(f"{'Barang':<20}{'Jumlah':<10}{'Subtotal'}")

    for pid, jumlah in beli_data.items():
        p = produk[pid]
        subtotal = jumlah * p["harga"]
        print(f"{p['nama']:<20}{jumlah:<10}Rp{subtotal:,}")

    print(f"\nTOTAL PEMBAYARAN : Rp{total_semua:,}")
    print("TERIMA KASIH TELAH BERBELANJA\n")

def menu():

    while True:
        print("E-COMMERCE ALAT TULIS")
        print("\n1. Lihat Produk")
        print("2. Tambah Keranjang")
        print("3. Lihat Keranjang")
        print("4. Update Keranjang")
        print("5. Hapus Keranjang")
        print("6. Checkout")
        print("7. Keluar")

        while True:
            pilih = input("Pilih menu: ").strip()
            if pilih.isdigit():
                pilih = int(pilih)
                break
            print("Input harus angka!")

        if pilih == 1: lihat_produk()
        elif pilih == 2: tambah_keranjang()
        elif pilih == 3: lihat_keranjang()
        elif pilih == 4: update_keranjang()
        elif pilih == 5: hapus_keranjang()
        elif pilih == 6: checkout()
        elif pilih == 7:
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Menu tidak tersedia!")

menu()
