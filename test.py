import requests
import time
import random

URL = "https://vehicle-iot-server.onrender.com/predict"

def send_data(ax, ay, az, speed):
    data = {
        "ax": ax,
        "ay": ay,
        "az": az,
        "speed": speed,
        "lat": 13.0827 + random.uniform(-0.001, 0.001),
        "lon": 80.2707 + random.uniform(-0.001, 0.001)
    }

    try:
        res = requests.post(URL, json=data)
        print("Sent:", data)
        print("Response:", res.json())
        print("-" * 50)
    except Exception as e:
        print("Error:", e)


print("🚗 Starting Simulation...")

# ---------- NORMAL DRIVING ----------
print("\n🟢 NORMAL DRIVING")
for _ in range(5):
    send_data(
        ax=random.uniform(0.1, 0.5),
        ay=random.uniform(0.1, 0.3),
        az=9.8,
        speed=random.uniform(20, 40)
    )
    time.sleep(2)


# ---------- HARSH ACCELERATION ----------
print("\n🚀 HARSH ACCELERATION")
for _ in range(3):
    send_data(
        ax=random.uniform(2.5, 3.5),
        ay=0.2,
        az=9.8,
        speed=random.uniform(30, 60)
    )
    time.sleep(2)


# ---------- NORMAL ----------
print("\n🟢 BACK TO NORMAL")
for _ in range(5):
    send_data(
        ax=random.uniform(0.1, 0.5),
        ay=random.uniform(0.1, 0.3),
        az=9.8,
        speed=random.uniform(20, 40)
    )
    time.sleep(2)


# ---------- HARSH BRAKING ----------
print("\n🛑 HARSH BRAKING")
for _ in range(3):
    send_data(
        ax=random.uniform(-3.5, -2.5),
        ay=0.1,
        az=9.8,
        speed=random.uniform(5, 20)
    )
    time.sleep(2)


print("\n⏳ Waiting for inactivity (trip end)...")
time.sleep(15)  # IMPORTANT → triggers trip end

print("\n✅ Simulation Complete")