import re
from collections import Counter

LOG_FILE = "application.log"

error_patterns = [
    r"ERROR",
    r"Timeout",
    r"Connection refused",
    r"CrashLoopBackOff",
    r"OOMKilled"
]

def analyze_logs():
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    detected = []

    for line in logs:
        for pattern in error_patterns:
            if re.search(pattern, line):
                detected.append(pattern)

    summary = Counter(detected)

    print("\n=== AI Ops Log Analysis Summary ===\n")

    for issue, count in summary.items():
        print(f"{issue}: {count} occurrences")

    if summary:
        print("\nSuggested Action:")
        print("- Check Kubernetes pod health")
        print("- Review memory and CPU usage")
        print("- Validate service connectivity")

if __name__ == "__main__":
    analyze_logs()
