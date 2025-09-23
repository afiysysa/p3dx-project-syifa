#%%
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

print("Program Started")

client = RemoteAPIClient()
sim = client.require('sim')
sim.setStepping(False)
sim.startSimulation()

w1_Handle = sim.getObject("/rightMotor")
w2_Handle = sim.getObject("/leftMotor")

#%%
d_xyyaw = []
d_t = []

bod_ang_pos = 0.0
bod_pos_x = 0.0
bod_pos_y = 0.0
t_prv = 0.0

sim.addLog(1,"get vel start")
time.sleep(2)
start_time = time.time()
while True:
    t_now = time.time() - start_time
    if t_now > 5:
        break;
    # get angular velocity
    w1_ang_vel = sim.getJointVelocity(w1_Handle)
    w2_ang_vel = sim.getJointVelocity(w2_Handle)
    # get linear velocity
    w1_lin_vel = w1_ang_vel*0.195/2 #diameter of P3DX wheel is 195mm
    w2_lin_vel = w2_ang_vel*0.195/2
    # get body velocity
    bod_lin_vel = (w1_lin_vel + w2_lin_vel)/2
    bod_ang_vel = (w1_lin_vel - w2_lin_vel)/(0.381/2)
    # get orientation
    t_diff = t_now-t_prv
    bod_ang_pos = bod_ang_pos + bod_ang_vel*t_diff
    # get planar velocity and position
    plan_vel_x = bod_lin_vel*math.cos(bod_ang_pos)
    plan_vel_y = bod_lin_vel*math.sin(bod_ang_pos)
    bod_pos_x = bod_pos_x + plan_vel_x*t_diff
    bod_pos_y = bod_pos_y + plan_vel_y*t_diff

    # save
    d_xyyaw.append([bod_pos_x,
                    bod_pos_y,
                    bod_ang_pos])
    d_t.append(t_now)

    t_prv = t_now
    sim.addLog(1,f"x,y,yaw="
                f"{bod_pos_x:.2f}m,{bod_pos_y:.2f}m,{math.degrees(bod_ang_pos):.2f}deg")

sim.addLog(1,"sim com ended")

# convert to np array
dat_xyyaw=np.array(d_xyyaw)
dat_t=np.array(d_t)

dat_xyyaw[:,2] = np.atan2(np.sin(dat_xyyaw[:,2]), np.cos(dat_xyyaw[:,2]))

#%% plot
plt.figure(figsize=(8, 6))
plt.plot(dat_xyyaw[:,0], dat_xyyaw[:,1], color='royalblue', linewidth=2, label='$^Ox_B$')
plt.scatter(dat_xyyaw[0,0], dat_xyyaw[0,1], marker='o', s=100, color='red', label='Start')
plt.scatter(dat_xyyaw[-1,0], dat_xyyaw[-1,1], marker='x', s=100, color='green', label='End')
plt.axis('equal')
plt.xlabel('$^Ox_B$ (m)', fontsize=12)
plt.ylabel('$^Oy_B$ (m)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# save
now = datetime.now()
filename = now.strftime("%y%m%d%H%M_A") + ".png"
plt.savefig(filename, format='png')
print(f"Plot saved successfully as '{filename}'")

# ------------------------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
# --- Plot 1: x pos ---
ax1.plot(dat_t, dat_xyyaw[:,0], color='royalblue', linewidth=2)
ax1.set_ylabel('$^Ox_B$ (m)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.plot(dat_t, dat_xyyaw[:,1], color='forestgreen', linewidth=2)
ax2.set_ylabel('$^Oy_B$ (m)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)

ax3.plot(dat_t, np.degrees(dat_xyyaw[:,2]), color='firebrick', linewidth=2)
ax3.set_xlabel('Time (s)', fontsize=12)
ax3.set_ylabel('$\\theta$ (deg)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

# save
now = datetime.now()
filename = now.strftime("%y%m%d%H%M_B") + ".png"
plt.savefig(filename, format='png')
print(f"Plot saved successfully as '{filename}'")
# %%