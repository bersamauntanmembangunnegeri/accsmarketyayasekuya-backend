# Instruksi Penggunaan Seed Data Dummy

Berikut adalah langkah-langkah untuk menggunakan `seed_data_dummy.sql` untuk mengisi database Anda dengan data dummy:

## 1. Pastikan `sqlite3` Terinstal
Pastikan Anda memiliki `sqlite3` terinstal di sistem Anda. Jika belum, Anda bisa menginstalnya dengan:

```bash
sudo apt-get update
sudo apt-get install sqlite3
```

## 2. Hapus Database Lama (Opsional, Disarankan)
Untuk memastikan database terisi dengan data dummy yang baru dan bersih, sangat disarankan untuk menghapus file database lama terlebih dahulu:

```bash
rm /home/ubuntu/accsmarketyayasekuya-backend/src/database/app.db
```

## 3. Impor Seed Data Dummy
Setelah database lama dihapus (atau jika Anda ingin menambahkan data dummy ke database yang sudah ada), jalankan perintah berikut dari direktori `/home/ubuntu/accsmarketyayasekuya-backend/src/database/`:

```bash
sqlite3 app.db < seed_data_dummy.sql
```

Perintah ini akan membuat database baru (`app.db`) jika belum ada, dan mengisinya dengan skema tabel serta data dummy dari `seed_data_dummy.sql`.

## 4. Jalankan Aplikasi Backend
Setelah data dummy diimpor, Anda bisa menjalankan aplikasi backend Anda seperti biasa:

```bash
cd /home/ubuntu/accsmarketyayasekuya-backend/src
python3 main.py
```

Database Anda sekarang akan terisi dengan data dummy yang telah dihasilkan.

## 5. Menggunakan Skrip `generate_dummy_data.py` (Alternatif)

Sebagai alternatif, Anda juga bisa menggunakan skrip `generate_dummy_data.py` secara langsung untuk mengisi database. Skrip ini akan secara otomatis menghapus data yang ada dan mengisi ulang dengan data dummy baru setiap kali dijalankan.

```bash
cd /home/ubuntu/accsmarketyayasekuya-backend/src/database
python3 generate_dummy_data.py
```

Metode ini lebih cepat jika Anda sering melakukan reset dan mengisi ulang database dengan data dummy.

