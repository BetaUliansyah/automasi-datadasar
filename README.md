# Automasi Data Dasar

Data Dasar DAU disediakan di alamat web http://www.djpk.kemenkeu.go.id/datadasar/dashboard Namun di laman web tersebut, kita hanya bisa mengambil data satu daerah saja. 

Untuk mendapatkan data seluruh daerah, setidaknya ada 4 metode:
1. Metode Copas satu per satu
2. Metode download file CSV satu per satu (klik lambang CSV di sebelah kanan halaman), lalu dikonsolidasi di Excel (menu Data, Consolidate)
3. Metode Padat Karya: minta bantuan mahasiswa dari kelas-kelas yang diampu untuk melakukan metode 1 atau 2 di atas, lalu dikonsolidasi di Excel (menu Data, Consolidate)
4. Metode Automasi, yang digunakan di source code ini.

## Cara Pembuatan
Simulasikan pengambilan data untuk satu daerah menggunakan Chrome, lalu cek variabel-variabel apa saja yang dikirim melalui POST dengan membuka fitur Inspect, Networks, Headers.
![inspect POST variables](img/Screen%20Shot%202019-12-26%20at%2010.09.34.png)

Lakukan looping di python dengan value nama-nama seluruh daerah di Indonesia sebagai iterasi.

## Cara Penggunaan
### A. Melalui Notebook
Salin kode python di repository ini ke Colab, dan jalankan dengan cara menekan tombol Run atau dengan menekan Ctrl - Enter. Tersedia link demo di bagian bawah tulisan ini.

### B. Melalui command line
Salin kode python ke file di komputer lokal Anda. Jalankan skrip python dengan perintah `python datadasar-dau2019.py`

Skrip akan berjalan beberapa menit sebelum mengeluarkan hasil.

## Demo
Silakan salin notebook berikut ini ke akun Colab Anda: http://bit.ly/BetaAutomasiDataDasarDAU 
Jalankan kode Python dengan menekan tombol Run atau Ctrl-Enter
