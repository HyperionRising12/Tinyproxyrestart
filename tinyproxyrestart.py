import subprocess
import time

def restart_tinyproxy():
    try:
        subprocess.run(['sudo', 'service', 'tinyproxy', 'restart'], check=True)
        print("Tinyproxy restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        restart_tinyproxy()
        time.sleep(120)
