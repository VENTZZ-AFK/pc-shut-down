import os
import platform
import time

def shutdown_system(delay=5):
    print(f"your system is being terminated in {delay} seconds. have fun ;)")
    time.sleep(delay)

    os_type = platform.system()

    if os_type == "Windows":
        os.system("shutdown /s /t 0")
    elif os_type == "Linux" or os_type == "Darwin":  # Darwin = macOS
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported OS.")

if __name__ == "__main__":
    shutdown_system(delay=5)  # delay in seconds