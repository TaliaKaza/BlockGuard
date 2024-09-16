import time
import random

def monitor_transactions():
    """
    Simulated function to monitor suspicious blockchain transactions.
    Alerts on large transfers and unusual wallet activity.
    """
    suspicious_activities = [
        "Large transfer detected",
        "Multiple small transfers from single wallet",
        "Rapid consecutive transactions",
        "Unusual token swap volume",
        "Possible front-running activity"
    ]
    while True:
        alert = random.choice(suspicious_activities)
        print(f"[Alert] {alert}")
        time.sleep(random.randint(10, 30))

if __name__ == "__main__":
    print("BlockGuard started monitoring...")
    monitor_transactions()
