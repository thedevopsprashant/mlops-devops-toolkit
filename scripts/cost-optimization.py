import subprocess

def find_idle_nodes():
    cmd = "kubectl top nodes"
    output = subprocess.getoutput(cmd)

    print("\n=== Kubernetes Cost Optimization Report ===\n")

    for line in output.splitlines()[1:]:
        columns = line.split()

        cpu = columns[1].replace("m", "")
        memory = columns[3].replace("%", "")

        if int(memory) < 20:
            print(f"Underutilized Node: {columns[0]}")

if __name__ == "__main__":
    find_idle_nodes()
