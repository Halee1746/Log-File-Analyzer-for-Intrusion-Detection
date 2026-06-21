failed_count = {}
total_failed = 0
with open("sample_log.txt", "r") as file:
    logs = file.readlines()
print("=== Log File Analysis Report ===\n")
for line in logs:
    if "LOGIN_FAILED" in line:
        total_failed += 1
        parts = line.split("IP:")
        ip = parts[1].split(" ")[0]
        if ip in failed_count:
            failed_count[ip] += 1
        else:
            failed_count[ip] = 1
print("Total Failed Login Attempts:", total_failed)
print("\nSuspicious IP Activity:")
for ip, count in failed_count.items():
    print(ip, "->", count, "failed attempts")
print("\nPossible Brute Force Alerts:")
alert_found = False
for ip, count in failed_count.items():
    if count >= 3:
        print("ALERT:", ip, "has", count, "failed login attempts")
        alert_found = True
if not alert_found:
    print("No brute force attack detected.")
