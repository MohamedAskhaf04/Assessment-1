import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 90

# Get metrics
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Check thresholds and alert
alerts = []

if cpu > CPU_THRESHOLD:
    alerts.append(f"ALERT: CPU usage is high! {cpu}%")

if mem > MEM_THRESHOLD:
    alerts.append(f"ALERT: Memory usage is high! {mem}%")

if disk > DISK_THRESHOLD:
    alerts.append(f"ALERT: Disk usage is high! {disk}%")

# Print alerts or status
if alerts:
    for alert in alerts:
        print(alert)
else:
    print("System is healthy ✅")
    
# Log metrics to a file
with open("system_health.log", "a") as f:
    f.write(f"{datetime.now()}: CPU={cpu}%, MEM={mem}%, DISK={disk}%\n")
