import numpy as np

def solve_transformation(point_U, rotation_gamma_deg, translation_t):
    try:
        #Konversi derajat ke radian
        gamma_rad = np.radians(rotation_gamma_deg)
        #buat matriks rotasi
        c = np.cos(gamma_rad)
        s = np.sin(gamma_rad)
        Rz = np.array([
            [c, -s, 0],
            [s,  c, 0],
            [0,  0, 1]
        ])
        
        #buat matriks transformasi homogen 4x4
        t = np.array(translation_t).reshape(3, 1)
        T = np.identity(4)
        T[:3, :3] = Rz
        T[:3, 3] = t.flatten()
        
        #perhitungan akhir dg koordinat homogen
        point_U_homo = np.append(point_U, 1)
        point_B_homo = T @ point_U_homo
        point_B = point_B_homo[:3]

        print("\nHASIL PERHITUNGAN :")
        print("Matriks Rotasi (Rz):\n", np.round(Rz, 3))
        print("\nMatriks Transformasi (T):\n", np.round(T, 3))
        print(f"\nTitik Awal (U)   : {point_U}")
        print(f"Hasil Akhir (B)  : {np.round(point_B, 3)}")
        print("---------------------------\n")

    except Exception as e:
        print(f"Terjadi error dalam perhitungan: {e}")

def display_menu():
    """Fungsi untuk menampilkan menu pilihan."""
    print("\nTransformasi koordinat homogen")
    print("1. Kerjakan Kasus 1 (P=(2,0,0), 	γ=90)")
    print("2. Kerjakan Kasus 2 (P=(0,2,0), 	γ=90)")
    print("3. Kerjakan Kasus 3 (P=(2,0,2), 	γ=-180)")
    print("4. Input Manual")
    print("5. Keluar")

# --- LOOP UTAMA PROGRAM ---
while True:
    display_menu()
    choice = input("Pilih opsi (1-5): ")

    if choice == '1':
        print("\n--- Kasus 1 ---")
        solve_transformation(point_U=[2, 0, 0], rotation_gamma_deg=90, translation_t=[0, 0, 0])
    
    elif choice == '2':
        print("\n--- Kasus 2 ---")
        solve_transformation(point_U=[0, 2, 0], rotation_gamma_deg=90, translation_t=[0, 0, 0])

    elif choice == '3':
        print("\n--- Kasus 3 ---")
        solve_transformation(point_U=[2, 0, 2], rotation_gamma_deg=-180, translation_t=[0, 0, 0])

    elif choice == '4':
        print("\n--- Input Manual ---")
        try:
            print("jika input manual, translasi(tx, ty, tz) dianggap 0")
            px = float(input("Masukkan koordinat Px: "))
            py = float(input("Masukkan koordinat Py: "))
            pz = float(input("Masukkan koordinat Pz: "))
            gamma = float(input("Masukkan sudut rotasi gamma (derajat): "))
            tx, ty, tz = 0, 0, 0
            
            solve_transformation(point_U=[px, py, pz], rotation_gamma_deg=gamma, translation_t=[tx, ty, tz])
        except ValueError:
            print("Error: Input harus berupa angka. Silakan coba lagi.")
            
    elif choice == '5':
        print("Keluar dari program. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka dari 1 hingga 5.")