class Mahasiswa:
    
    # atribut kelas
    jumlah_mahasiswa = 0
    nilai_ipk_minimal = 2.0
    
    def __init__(self, nama, jurusan, ipk):
        # atribut instance
        self.nama = nama
        self.jurusan = jurusan
        self.__ipk = ipk  # atribut private
        
        Mahasiswa.jumlah_mahasiswa += 1
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.__ipk}")
        
    # fungsi public
    def perbarui_ipk(self, ipk_baru):
        if ipk_baru >= Mahasiswa.nilai_ipk_minimal:
            self.__ipk = ipk_baru
            print("IPK berhasil diperbarui.")
        else:
            print("IPK tidak valid.")
    
    # fungsi protected
    def _fungsi_protected(self):
        print("Ini merupakan fungsi protected.")
    
    # fungsi private
    def __fungsi_private(self):
        print("Ini merupakan fungsi private.")

# membuat objek m1 dari kelas Mahasiswa
m1 = Mahasiswa("Deodry", "Informatika", 3.0)

# memanggil fungsi tampilkan_info pada objek m1
m1.tampilkan_info()

# mengubah nilai IPK pada objek m1
m1.perbarui_ipk(3.5)