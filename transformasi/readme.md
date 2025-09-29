# Simulasi Transformasi Koordinat Homogen

Sebuah skrip Python sederhana dengan antarmuka baris perintah (*Command-Line Interface*) untuk menghitung dan mensimulasikan transformasi koordinat homogen 3D. Proyek ini dibuat sebagai bagian dari tugas mata kuliah Sistem Robot Otonom.

Skrip ini memungkinkan pengguna untuk menghitung posisi baru dari sebuah titik setelah sistem koordinatnya mengalami rotasi di sekitar sumbu Z dan translasi.



---

## ## Fitur
* **Menu Interaktif**: Antarmuka berbasis CLI yang mudah digunakan untuk memilih berbagai skenario.
* [cite_start]**Kasus Terdefinisi**: Menyelesaikan 3 kasus perhitungan yang telah ditentukan sesuai dengan tugas perkuliahan. [cite: 394, 395, 396, 400, 401, 402]
* **Input Manual**: Opsi untuk memasukkan koordinat titik dan sudut rotasi secara manual untuk eksperimen.
* **Penjelasan Langkah-demi-Langkah**: Menampilkan output yang merinci setiap tahap perhitungan, termasuk Matriks Rotasi, Matriks Transformasi, dan hasil akhir.

---

## ## Prasyarat
* Python 3.x
* Library NumPy

---

## ## Cara Menjalankan

1.  **Clone Repositori**
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    cd [NAMA_FOLDER_PROYEK]
    ```

2.  **Instal Dependensi**
    Disarankan untuk menggunakan *virtual environment*.
    ```bash
    # Instal NumPy
    pip install numpy
    ```

3.  **Jalankan Skrip**
    Eksekusi skrip utama dari terminal:
    ```bash
    python nama_skrip_anda.py
    ```
4.  **Gunakan Menu**
    Setelah dijalankan, menu akan muncul. Masukkan angka `1` hingga `5` untuk memilih opsi yang diinginkan dan tekan Enter.


Author : Aasy-Syifa Mahardika Ghofur 5022221111