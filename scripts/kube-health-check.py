import subprocess

def check_pods():
    cmd = "kubectl get pods --all-namespaces"
    result = subprocess.getoutput(cmd)

    print("\n=== Kubernetes Health Report ===\n")

    for line in result.splitlines():
        if "CrashLoopBackOff" in line or "Error" in line:
            print(f"[ALERT] {line}")

if __name__ == "__main__":
    check_pods()
