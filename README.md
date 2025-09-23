
# Proyek Simulasi Robot Pioneer P3DX

Selamat datang di repositori proyek simulasi robot Pioneer P3DX saya. Repositori ini berfungsi sebagai kumpulan berbagai eksperimen dan implementasi algoritma robotika menggunakan simulator CoppeliaSim yang dikontrol secara eksternal oleh skrip Python.

Setiap folder di dalam repositori ini mewakili sebuah proyek atau studi kasus yang berbeda, mengeksplorasi aspek-aspek spesifik dari sistem robot otonom.

---

## Teknologi yang Digunakan
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CoppeliaSim](https://img.shields.io/badge/CoppeliaSim-E67E22?style=for-the-badge&logo=linux-foundation&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-1B2F3E?style=for-the-badge&logo=matplotlib&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## Daftar Proyek

### 1. Pelacakan dan Visualisasi Pose (Pose Tracking & Visualization)
- **Folder**: `[./pose-visualization/](pose-visualization/)`
- **Deskripsi**: Proyek ini mendemonstrasikan alur kerja lengkap untuk mengontrol pergerakan robot P3DX, melacak data posisinya (x, y) dan orientasinya (yaw) secara *real-time*, kemudian memvisualisasikan data tersebut ke dalam plot temporal dan spasial menggunakan Matplotlib.

### 2. Pengukuran Kecepatan Sendi (Joint Velocity)
- **Folder**: `[./joint-velocity/](joint-velocity/)`
- **Deskripsi**: Eksperimen untuk membaca dan menampilkan kecepatan sudut (*angular velocity*) dari motor kiri dan kanan robot P3DX secara *real-time*. Data ditampilkan langsung di terminal.

### 3. Pengukuran Odometri (Odometry Measurement)
- **Folder**: `[./odometry/](odometry/)`
- **Deskripsi**: *(Akan datang)* Implementasi perhitungan odometri untuk mengestimasi posisi robot hanya berdasarkan data perputaran roda.

### 4. Pembacaan Sensor (Sensor Reading)
- **Folder**: `[./sensors/](sensors/)`
- **Deskripsi**: *(Akan datang)* Proyek untuk mengambil dan memproses data dari sensor virtual pada P3DX, seperti sensor ultrasonik atau vision sensor.

---

## Instalasi dan Setup Umum

1.  **Prasyarat**:
    - CoppeliaSim Edu
    - Python 3.8+
2.  **Clone Repositori**:
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    cd [NAMA_REPOSITORI]
    ```
3.  **Siapkan Lingkungan Python**:
    - Direkomendasikan untuk membuat *virtual environment*:
      ```bash
      python -m venv venv
      source venv/bin/activate  # Linux/macOS
      # .\venv\Scripts\activate  # Windows
      ```
4.  **Instal Dependensi**:
    - File `requirements.txt` mungkin tersedia di beberapa folder proyek.
      ```bash
      pip install -r requirements.txt
      ```

## Cara Menjalankan Proyek
Setiap proyek memiliki instruksi spesifik di dalam foldernya masing-masing. Namun, alur kerja umumnya adalah:
1.  Buka file scene `.ttt` yang relevan di CoppeliaSim.
2.  Jalankan skrip Python utama dari terminal (pastikan `venv` sudah aktif).
