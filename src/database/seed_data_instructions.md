# Instruksi Penggunaan Seed Data

Berikut adalah langkah-langkah untuk menggunakan `seed_data.sql` untuk mengisi database Anda:

## 1. Pastikan `sqlite3` Terinstal
Pastikan Anda memiliki `sqlite3` terinstal di sistem Anda. Jika belum, Anda bisa menginstalnya dengan:

```bash
sudo apt-get update
sudo apt-get install sqlite3
```

## 2. Hapus Database Lama (Opsional)
Jika Anda ingin memulai dengan database yang bersih, Anda bisa menghapus file database lama:

```bash
rm /home/ubuntu/accsmarketyayasekuya-backend/src/database/app.db
```

## 3. Impor Seed Data
Untuk mengimpor seed data ke database, jalankan perintah berikut dari direktori `/home/ubuntu/accsmarketyayasekuya-backend/src/database/`:

```bash
sqlite3 app.db < /home/ubuntu/seed_data.sql
```

Pastikan Anda mengganti `/home/ubuntu/seed_data.sql` dengan path yang benar ke file seed data jika Anda memindahkannya.

## 4. Jalankan Aplikasi Backend
Setelah data diimpor, Anda bisa menjalankan aplikasi backend Anda seperti biasa:

```bash
cd /home/ubuntu/accsmarketyayasekuya-backend/src
python3 main.py
```

Database Anda sekarang akan terisi dengan data yang ada di `seed_data.sql`.

