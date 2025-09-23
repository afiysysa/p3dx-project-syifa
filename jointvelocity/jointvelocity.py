import matplotlib.pyplot as plt
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

print("Program dimulai...")

# --- 1. KONEKSI DAN KONTROL ROBOT ---
client = RemoteAPIClient()
sim = client.require('sim')

# Pastikan simulasi dihentikan sebelum memulai
sim.stopSimulation()
time.sleep(1) # Jeda agar server siap

try:
    # Dapatkan handle untuk robot dan motornya
    robot_handle = sim.getObject('/PioneerP3DX')
    left_motor_handle = sim.getObject('/PioneerP3DX/leftMotor')
    right_motor_handle = sim.getObject('/PioneerP3DX/rightMotor')
    print("Handle untuk robot dan motor berhasil didapatkan.")
except Exception as e:
    print(f"Error: Gagal mendapatkan handle. Pastikan ada P3DX di scene. Detail: {e}")
    quit()

# Siapkan list untuk menyimpan data
timestamps = []
x_positions = []
y_positions = []
yaw_angles = []

# Mulai simulasi
sim.startSimulation()
print("Simulasi dimulai. Melacak pergerakan robot...")

# Atur kecepatan motor untuk membuat robot bergerak melengkung
sim.setJointTargetVelocity(left_motor_handle, 2.0)
sim.setJointTargetVelocity(right_motor_handle, 1.8)

# --- 2. PELACAKAN (TRACKING) DATA POSE ---
start_time = time.time()
simulation_duration = 70 # detik

try:
    while time.time() - start_time < simulation_duration:
        # Dapatkan posisi (x, y, z)
        pos = sim.getObjectPosition(robot_handle, sim.handle_world)
        # Dapatkan orientasi (alpha, beta, gamma/yaw)
        orient = sim.getObjectOrientation(robot_handle, sim.handle_world)
        
        # Simpan data ke dalam list
        current_time = time.time() - start_time
        timestamps.append(current_time)
        x_positions.append(pos[0])
        y_positions.append(pos[1])
        yaw_angles.append(orient[2]) # Yaw adalah elemen ketiga (gamma)
        
        time.sleep(0.05) # Atur frekuensi sampling

finally:
    # Pastikan robot berhenti dan simulasi dihentikan
    sim.setJointTargetVelocity(left_motor_handle, 0)
    sim.setJointTargetVelocity(right_motor_handle, 0)
    sim.stopSimulation()
    print("Pelacakan selesai. Simulasi dihentikan.")

# --- 3. PEMBUATAN PLOT ---
print("Membuat plot dari data yang direkam...")

# Konversi list ke numpy array untuk kemudahan
t = np.array(timestamps)
x = np.array(x_positions)
y = np.array(y_positions)
yaw = np.array(yaw_angles)
yaw_deg = np.rad2deg(yaw) # Konversi yaw ke derajat

# --- Plot Temporal ---
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
fig.suptitle('Temporal Plots of P3DX Pose', fontsize=16)

axs[0].plot(t, x, color='blue')
axs[0].set_ylabel('Position x (m)')
axs[0].grid(True)
axs[1].plot(t, y, color='green')
axs[1].set_ylabel('Position y (m)')
axs[1].grid(True)
axs[2].plot(t, yaw_deg, color='red')
axs[2].set_ylabel('Position yaw (deg)')
axs[2].set_xlabel('Time (sec)')
axs[2].grid(True)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('temporal_plot.png', dpi=300)
print("File 'temporal_plot.png' berhasil dibuat.")

# --- Plot Spasial ---
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Robot Path')
plt.plot(x[0], y[0], 'go', markersize=10, label='Start')
plt.plot(x[-1], y[-1], 'ro', markersize=10, label='End')
plt.title('Spatial Plot of P3DX Pose (X vs Y)')
plt.xlabel('Position x (m)')
plt.ylabel('Position y (m)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.savefig('spatial_plot.png', dpi=300)
print("File 'spatial_plot.png' berhasil dibuat.")