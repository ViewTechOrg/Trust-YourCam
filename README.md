<h1 align="center"><code>Trust-YourCam</code></h1> <p align="center"> <img src="https://github.com/ViewTechOrg/Server/blob/main/Trust-YourCam/img/51a35c1d-9f24-489d-a32d-d1470f923d6a.png" width="590"><br><br>
  <img src="https://img.shields.io/static/v1?label=ViewTechTeam&color=green&message=+&logo=nano&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/static/v1?label=Author&color=green&message=viewTech+ORG&logo=nim&logoColor=white&style=for-the-badge"><br>
  <img src="https://img.shields.io/github/stars/ViewTechOrg/Trust-YourCam?logo=github&style=for-the-badge">
  <img src="https://img.shields.io/static/v1?label=Version&color=green&message=1.2.0&logo=Clockify&logoColor=white&style=for-the-badge"><br><br>
  <img src="https://img.shields.io/github/contributors/ViewTechOrg/Trust-YourCam?logo=apache&style=for-the-badge"><br>
  <img src="https://img.shields.io/static/v1?label=Termux&color=green&message=+&logo=Iterm2&logoColor=white&style=flat">
  <img src="https://img.shields.io/github/forks/ViewTechOrg/Trust-YourCam?logo=github&style=flat"><br>
<br><br>

  **Trust-YourCam** adalah alat uji keamanan berbasis web yang memanfaatkan teknik phishing dan social engineering untuk mengakses kamera pengguna secara diam-diam setelah izin diberikan. Aplikasi ini dirancang dengan antarmuka yang menarik dan meyakinkan, menyerupai aplikasi hiburan, untuk menguji kesadaran target terhadap ancaman keamanan digital. Setelah target memberikan izin kamera, sistem dapat mengambil foto secara otomatis menggunakan kamera depan, disertai efek visual dan suara untuk menyamarkan niat sebenarnya. Trust Your Cam ditujukan untuk keperluan edukasi, riset keamanan, dan pengujian kesadaran terhadap manipulasi sosial. Penggunaan di luar konteks etis dan hukum tidak dianjurkan dan menjadi tanggung jawab penuh pengguna.

### 📸 Data yang Dikumpulkan
- 📍 Lokasi Geografis: Melalui teknologi IP Lookup (akurasi tergantung ISP).
- 📷 Foto Kamera Depan: Diambil secara diam-diam jika akses diberikan.
- 🧾 Informasi Perangkat: Seperti jenis browser, sistem operasi, dan model perangkat.
### 🧩 Fitur Utama
- 🔗 Generate Link Unik: Buat tautan yang dapat dikustomisasi untuk setiap target.
- 🗺️ Pelacakan Lokasi Real-Time: Menampilkan data IP lookup, peta, dan waktu akses (fitur dalam pengembangan).
- 🎥 Foto Kamera Depan Otomatis: Mengambil dan mengunggah gambar secara otomatis setelah target memberi izin kamera.
- 📱 Deteksi Perangkat Otomatis: Mendeteksi sistem operasi, browser, dan model perangkat menggunakan User-Agent.

### Penggunaan
1. Jalankan tools Trust-YourCam DI TERMUX !!.
2. Buat link target dari antarmuka yang disediakan.
3. Sebarkan link ke target (melalui email, chat, dll).
4. pancing target untuk membuka nya (manipulasi)
5. Saat target membuka link dan memberikan akses kamera, data akan langsung terkirim ke server dan dapat dilihat melalui dashboard.

<h3>Klik tutorial</h3>
<details open><summary><strong>Command & Penggunaan <code>(pemula)</code></strong></summary>

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
make install
```
### 3. command tools Trust-YourCam
```bash
make build # untuk menjalankan script
make stop # untuk berhentikan program
make update # untuk update
```
</details><br>

<details open><summary><strong>Command & Penggunaan <code>(pro)</code></strong></summary>

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
export MOD="window"
bash Server
```
</details>

### Environment Variables (ENV) - Pengaturan Mode Trust-YourCam (pro)

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

### Contoh Penggunaan `Pro`

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
> Hasilnya, interface akan menampilkan nama session: Polygon

### 3. Shutdown Software / mematikan progamnya
untuk mematikan program setelah di gunakan bisa mengetikan perintah di bawah ini setelah di ctrl c di salah satu panel nya
```bash
make stop
```

### 📦 Teknologi yang Digunakan
- HTML/CSS/JS (Frontend)
- Webcam API
- IP Lookup API
- Node.js / PHP / Backend ringan & fleksibel (tergantung setup pengguna)

### 📄 Lisensi
Copyright © 2025 [ViewTechOrg OFC](https://github.com/ViewTechOrg)<br />
This project is [MIT License](https://github.com/ViewTechOrg/Trust-YourCam/blob/master/LICENSE) licensed.

## ✨ Kontributor

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Bayu12345677"><img src="https://avatars.githubusercontent.com/u/86620608?v=4" width="100px;" alt=""/><br /><sub><b>Bayu12345677</b </sub></a><br />💻 📢 🎨</td>
    <!-- Tambahan kontributor lainnya -->
         <td align="center"><a href="https://github.com/Xenzi-XN1"><img src="https://avatars.githubusercontent.com/u/82303963?v=4" width="100px;" alt=""/><br /><sub><b>Xenzi</b </sub></a><br />💻 🎨</td>
     <td align="center"><a href="https://github.com/Lubebansokhekel"><img src="https://avatars.githubusercontent.com/u/181061263?v=4" width="100px;" alt=""/><br /><sub><b>Galirus</b </sub></a><br />💻 🎨</td>
    <td align="center"><a href="https://github.com/fahadsyihab06"><img src="https://avatars.githubusercontent.com/u/133946867?v=4" width="100px;" alt=""/><br /><sub><b>TC20</b </sub></a><br />💻 🎨</td>
    <td align="center"><a href="https://github.com/Cyber404119"><img src="https://avatars.githubusercontent.com/u/192098761?v=4" width="100px;" alt=""/><br /><sub><b>Tony</b </sub></a><br />💻 🎨</td>
  </tr>
</table>
<!-- ALL-CONTRIBUTORS-LIST:END -->

## SOSIAL MEDIA
<div>
<a href="https://vm.tiktok.com/ZSr3aQB1W/" target="_blank">
  <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok">
</a><br>

<a href="https://www.youtube.com/@ViewTech_Or" target="_blank">
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
</a><br>

<a href="https://www.instagram.com/viewtech4484/" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
</a><br>
</div>

> Copyright C ViewTech Team 2025
