class Data_diri:
    def _init_(self,nama,nim,kelas_siakad_jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_siakad = kelas_siakad
        self.jumlah_sks = jumlah_sks
        
    def display(self):
        print("Nama: ",self.nama)
        print("Nim: ",self.nim)
        print("Kelas_siakad: ",self.kelas_siakad)
        print("Jumlah_sks: ",self.jumlah_sks)
        
Data=Data_diri("Lilis Swastika",121140233
,"RD",22)
Data.display()