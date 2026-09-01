import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("A6 synthetic CloudWatch metrics.csv")

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# -----------------------------
# Chart 1: Web VM CPU utilisation over time
# -----------------------------

cpu_df = df[
    (df["resource"] == "MediCore-Web-VM-01") &
    (df["metric_name"] == "CPUUtilization")
]

plt.figure(figsize=(12, 6))
plt.plot(cpu_df["timestamp"], cpu_df["value"])
plt.title("MediCore Web VM CPU Utilisation Over Time")
plt.xlabel("Date and Time")
plt.ylabel("CPU Utilisation (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("A6-01-cpu-utilisation-over-time.png")
plt.show()

# -----------------------------
# Chart 2: Failed SSH attempts per day
# -----------------------------

ssh_df = df[
    (df["resource"] == "MediCore-Web-VM-01") &
    (df["metric_name"] == "FailedSSHAttempts")
].copy()

ssh_df["date"] = ssh_df["timestamp"].dt.date

daily_ssh = ssh_df.groupby("date")["value"].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(daily_ssh["date"], daily_ssh["value"])
plt.title("Failed SSH Attempts Per Day")
plt.xlabel("Date")
plt.ylabel("Failed SSH Attempts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("A6-02-failed-ssh-attempts-per-day.png")
plt.show()

print("Charts created successfully.")