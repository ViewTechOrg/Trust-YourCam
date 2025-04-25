* <h1 align="center">Trust-YourCam</h1> <p align="center"> <img src="https://github.com/ViewTechOrg/Server/blob/main/img/Trust-YourCam/WhatsApp%20Image%202025-04-25%20at%2011.09.13.jpeg" width="590"><br>
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
   <img src="https://img.shields.io/static/v1?label=ViewTechTeam&color=green&message=+&logo=nano&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/static/v1?label=Author&color=green&message=viewTech+ORG&logo=nim&logoColor=white&style=for-the-badge"><br>
  <img src="https://img.shields.io/github/stars/ViewTechOrg/Trust-YourCam?logo=github&style=for-the-badge">
  <img src="https://img.shields.io/static/v1?label=Version&color=green&message=0.0.1&logo=Clockify&logoColor=white&style=for-the-badge"><br><br>
  <img src="https://img.shields.io/static/v1?label=Termux&color=green&message=+&logo=Iterm2&logoColor=white&style=flat">
  <img src="https://img.shields.io/github/forks/ViewTechOrg/Trust-YourCam?logo=github&style=flat"><br>
  <img src="https://img.shields.io/github/contributors/ViewTechOrg/Trust-YourCam?logo=apache&style=for-the-badge">
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
> Hasilnya, interface akan menampilkan nama session: Polygon


###📦 Teknologi yang Digunakan
- HTML/CSS/JS (Frontend)
- Webcam API
- IP Lookup API
- Node.js / PHP / Backend ringan & fleksibel (tergantung setup pengguna)

### 📄 Lisensi
MIT License. Lihat file LICENSE untuk detail.

## ✨ Kontributor

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"><img src="https://avatars.githubusercontent.com/u/86620608?v=4?s=100" width="100px;" alt="Speedrun"/><br /><sub><b>Speedrun</b></sub></a><br /><a href="https://github.com/ViewTechOrg/Trust-YourCam/commits?author=Bayu12345677" title="Code">💻</a> <a href="#design-Bayu12345677" title="Design">🎨</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

> Copyright C ViewTech Team 2025

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!